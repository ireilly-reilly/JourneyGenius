<template>
    <v-container fluid class="no-border">
        <v-snackbar v-model="showSnackbar" color="deep-purple-accent-2" top>
            <span class="text-center">Trip Saved Successfully</span>
        </v-snackbar>
        <v-row>
            <v-col v-for="(day, index) in itinerary" :key="index" cols="12">
                <v-card class="activity-card" style="display: flex; flex-direction: column; height: 100%;">
                    <br>
                    <v-card-title :class="['headline', fontSizeClass(index)]">
                        <v-icon v-if="timelineIcon(index)" :class="['mr-2', iconColorClass(index)]">
                            {{ timelineIcon(index) }}
                        </v-icon>
                        {{ day.title }}
                    </v-card-title>

                    <br>
                    <v-row style="flex: 1;">
                        <v-col v-for="(activity, activityIndex) in day.activities" :key="activityIndex" cols="12"
                            md="4">
                            <v-card class="activity-box" style="flex: 1;">
                                <!-- Set a fixed height for the images -->
                                <v-img :src="activity.image" alt="Activity Image" class="activity-img-with-border"
                                    style="object-fit: cover; width: 100%; height: 100%;"></v-img>
                                <v-card-title>{{ activity.name }}</v-card-title>
                                <v-card-text class="description-height">{{ activity.description }}</v-card-text>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
    </v-container>


    <!-- Two buttons on the bottom -->
    <v-row justify="center" class="mt-4">
        <v-col cols="12" md="8" class="text-center">
            <router-link to="/GeneratedItinerary">
                <v-btn size="large" color="deep-purple-accent-2" class="white--text mt-6 mr-2" @click="previousStep"
                    style="min-width: 150px;">
                    Go Back
                </v-btn>
            </router-link>

            <!-- Call method to save trip to database here-->
            <router-link to="/SavedTrips">
                <v-btn size="large" color="deep-purple-accent-2" class="white--text mt-6 ml-2" @click="saveTrip"
                    style="min-width: 150px;">
                    Save Trip
                </v-btn>
            </router-link>
        </v-col>
    </v-row>
</template>

<script>
import axios from 'axios';
// import { get } from 'core-js/core/dict';
import Cookies from 'js-cookie';
export default {
    data() {

        return {
            itinerary: [],
            showSnackbar: false,

        };
    },

    created() {

        // Retrieve Trip Details
        const tripObject = this.$route.params.tripObject;
        const selectedActivities = this.$store.state.tripObject.activities;
        const selectedLandmarks = this.$store.state.tripObject.landmarks;
        const selectedFoods = this.$store.state.tripObject.foods;
        const selectedShops = this.$store.state.tripObject.shops;
        // console.log("This is the activities array: " + selectedActivities)

        // Round robin sorting function
        const getRoundRobinSlice = arrays => {
            let index = 0;
            let output = [];

            while (arrays.some(array => array.length > 0)) {
                for (let i = 0; i < arrays.length; i++) {
                    if (arrays[i].length > 0) {
                        output.push(arrays[i].shift());
                    }
                }
            }

            return output;
        };

        // Function used to parse the titles from the descriptions
        const getActivityTitles = (activities) => {
            return activities.map(activity => {
                const title = activity.split(':')[0]; // Split at ":" and get the first part
                return title.trim(); // Remove any leading or trailing whitespace
            });
        };

        // Function to remove titles from each string in the array
        const removeTitles = (array) => {
            return array.map((item) => {
                // Split the string at the first occurrence of ":"
                const parts = item.split(':');
                // Return the second part of the split string (the description) trimmed of any leading or trailing whitespace
                return parts.length > 1 ? parts.slice(1).join(':').trim() : item.trim();
            });
        };

        // Separating the titles from the descriptions
        const activityTitles = getActivityTitles(selectedActivities);
        const landmarkTitles = getActivityTitles(selectedLandmarks);
        const foodTitles = getActivityTitles(selectedFoods);
        const shopTitles = getActivityTitles(selectedShops);


        const sortedArray = getRoundRobinSlice([selectedActivities, selectedLandmarks, selectedFoods, selectedShops]);
        const combinedArray = removeTitles(sortedArray);
        const combinedTitles = getRoundRobinSlice([activityTitles, landmarkTitles, foodTitles, shopTitles]);
        // console.log("Combined Description: " + combinedArray)
        // console.log("Combined Titles: " + combinedTitles)
        console.log("Sorted array without titles: " + combinedArray)

        const dateRangeString = this.$store.state.tripObject.dates;

        // Parse date range
        const [startDateString, endDateString] = dateRangeString.split(" - ");
        const startDate = this.parseDateString(startDateString);
        const endDate = this.parseDateString(endDateString);

        // Calculate the trip duration
        const daysDifference = this.calculateTripDuration(startDate, endDate);

        // Calculate the number of descriptions per day
        let descriptionsPerDay = Math.floor(combinedArray.length / daysDifference);
        let remainingDescriptions = combinedArray.length % daysDifference;

        // Initialize index outside of the loop
        let currentIndex = -1;

        // Loop through each day
        for (let i = 0; i < daysDifference; i++) {
            const currentDate = new Date(startDate);
            currentDate.setDate(startDate.getDate() + i);
            const dayTitle = `Day ${i + 1} - ${this.formatDate(currentDate)}`;

            // Calculate the number of descriptions for this day
            let descriptionsForThisDay = descriptionsPerDay;
            if (remainingDescriptions > 0) {
                descriptionsForThisDay++;
                remainingDescriptions--;
            }

            // Slice the descriptions for this day
            const descriptionsForDay = combinedArray.slice(0, descriptionsForThisDay);

            // Remove the sliced descriptions from the combinedArray
            combinedArray.splice(0, descriptionsForThisDay);



            const daySection = {
                title: dayTitle,
                activities: descriptionsForDay.map(description => ({
                    name: combinedTitles[currentIndex += 1],
                    description: description,
                    image: require('@/assets/boba2.jpeg') // Add your image logic here
                }))
            };
            // Update the current index
            this.itinerary.push(daySection);
        }


    },




    mounted() {
        // console.log("HEY!!!")
        const tripObject = this.$route.params.tripObject;
        // console.log("This is the saved object: " + tripObject)
        // console.log("activities: " + this.$store.state.tripObject.activities)

    },
    methods: {
        getRoundRobinSlice(arrays) {
            let index = 0;
            let output = [];

            while (arrays.some(array => array.length > 0)) {
                for (let i = 0; i < arrays.length; i++) {
                    if (arrays[i].length > 0) {
                        output.push(arrays[i].shift());
                    }
                }
            }

            return output;
        },





        getTimelineColor(index) {
            // Define colors for each day
            const colors = ['primary', 'info', 'success', 'error', 'warning'];
            return colors[index % colors.length];
        },
        getTimelineIcon(index) {
            // Define icons for each day
            const icons = ['mdi-hiking', 'mdi-map-marker', 'mdi-spa', 'mdi-food', 'mdi-coffee'];
            return icons[index % icons.length];
        },
        // getUserDatabaseID() {
        //     const jwtToken = Cookies.get('login_token');
        //     const url = 'http://localhost:8000/api/get_user_id'
        //     axios.get(url, { headers: { Authorization: `Bearer ${jwtToken}` } })
        //         .then(response => {
        //             userId = response.data.user_id;
        //             console.log('User ID:', userId);
        //             return userId;
        //         })
        //         .catch(error => {
        //             console.error('Error getting user ID:', error);
        //             return null; // Return null in case of an error
        //         });
        // },
        formatDate(date) {
            // Format the date into "Month Day, Year" format
            const options = { month: 'long', day: 'numeric', year: 'numeric' };
            return date.toLocaleDateString(undefined, options);
        },
        parseDateString(dateString) {
            // Parse the date string into month, day, and year
            const parts = dateString.split(" ");
            const month = parts[0];
            const day = parseInt(parts[1].replace(",", ""));
            const year = parseInt(parts[2]);

            // Return a Date object
            return new Date(year, this.getMonthIndex(month), day);
        },
        getMonthIndex(monthName) {
            // Helper function to get the index of a month in JavaScript Date object
            const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
            return months.indexOf(monthName);
        },
        calculateTripDuration(startDate, endDate) {
            // Convert start and end dates to Date objects
            const startDateObj = new Date(startDate);
            const endDateObj = new Date(endDate);

            // Calculate the difference in milliseconds between the two dates
            const timeDifference = endDateObj.getTime() - startDateObj.getTime();

            // Convert milliseconds to days and add 1 to account for same-day trips
            const daysDifference = Math.ceil(timeDifference / (1000 * 3600 * 24)) + 1;

            return daysDifference;
        },
        saveTrip() {
            console.log("From saveTrip() function: ")

            //Get userID from cookies
            const userID = Cookies.get('database_id');
            console.log("Current user id:");
            console.log(userID);

            //Gathering data from vuex storage
            const activities = this.$store.state.activities;
            const landmarks = this.$store.state.landmarks;
            const foods = this.$store.state.foods;
            const shops = this.$store.state.shops;
            const hotels = this.$store.state.hotels;
            const datesData = this.$store.state.datesData;
            const budget = this.$store.state.budget;
            const stateData = this.$store.state.stateData;
            const city = this.$store.state.city;
            const lat = this.$store.state.lat;
            const long = this.$store.state.long;
            const cityDescription = this.$store.state.cityDescription;
            const citySlogan = this.$store.state.citySlogan;
            const latitude = this.$store.state.lat;
            const longitude = this.$store.state.long;

            //Condensing to sendable form
            const tripData = {
                userID,
                activities,
                landmarks,
                foods,
                shops,
                hotels,
                datesData,
                budget,
                stateData,
                city,
                lat,
                long,
                cityDescription,
                citySlogan
            };
            console.log("Trip Data from vuex in ready to send:")
            console.log(tripData)

            // Send data to Python backend
            axios.post('http://localhost:8000/api/save_trip_to_user', tripData)
                .then(response => {
                    console.log('Trip saved successfully:', response.data);
                    this.showSnackbar = true;
                    // Optionally, you can perform any further actions here
                })
                .catch(error => {
                    console.error('Error saving trip:', error);
                });
        },
        // Other methods for itinerary display, if any
    },
    computed: {
        fontSizeClass() {
            return (index) => {
                // Define font sizes for each day
                const fontSizes = ['text-h4', 'text-h4', 'text-h4']; // Adjust sizes as needed
                return fontSizes[index % fontSizes.length];
            };
        },
        iconColorClass() {
            return (index) => {
                // Define icon colors for each day
                const colors = ['primary', 'info', 'success', 'error', 'warning'];
                return colors[index % colors.length];
            };
        },
        timelineIcon() {
            return (index) => {
                // Define icons for each day
                const icons = ['mdi-hiking', 'mdi-map-marker', 'mdi-spa', 'mdi-food', 'mdi-coffee'];
                return icons[index % icons.length];
            };
        }
    }
};
</script>


<style scoped>
.description-height {
    height: 175px;
    /* Set a fixed height for the descriptions */
    white-space: normal;
    overflow: hidden;
    text-overflow: ellipsis;
    /* Hide overflow content if the description is longer */
    display: -webkit-box;
    -webkit-line-clamp: 3;
    /* Limit the number of lines to show */
    -webkit-box-orient: vertical;
}

.activity-img-with-border {
    border: 1px solid #ddd;
    /* Add a border for visual separation */
}

/* Additional styling for responsiveness, if needed */
@media (max-width: 600px) {}
</style>