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
            <v-btn size="large" color="deep-purple-accent-2" class="white--text mt-6 mr-2" @click="send"
                style="min-width: 150px;">
                Itinerary Overview
            </v-btn>

            <!-- Call method to save trip to database here-->
            <router-link to="/SavedTrips">
                <v-btn size="large" color="deep-purple-accent-2" class="white--text mt-6 ml-2"
                    style="min-width: 150px;">
                    Close
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
            //trip_id: '',
            savedTrip: [],
        };
    },

    created() {
        const activities = this.$store.state.tripObject.activities;
        const landmarks = this.$store.state.tripObject.landmarks;
        const foods = this.$store.state.tripObject.foods;
        const shops = this.$store.state.tripObject.shops;
        const hotels = this.$store.state.tripObject.hotels;

        const data = {
            activities,
            landmarks,
            foods,
            shops,
            hotels,
        };

        axios.post('http://localhost:8000/api/restaurant_photo_data', data)
            .then(response => {
                console.log("Food Pictures", response.data); // Log response from Python server
                this.$store.commit('updateFoodPictures', response.data);
            })
            .catch(error => {
                console.error('Error sending data to Python server (restaurant):', error);
            });

        axios.post('http://localhost:8000/api/activity_photo_data', data)
            .then(response => {
                console.log("Activity Pictures", response.data); // Log response from Python server
                this.$store.commit('updateActivityPictures', response.data);

            })
            .catch(error => {
                console.error('Error sending data to Python server (activity):', error);
            });

        axios.post('http://localhost:8000/api/landmark_photo_data', data)
            .then(response => {
                console.log("Landmark Pictures", response.data); // Log response from Python server
                this.$store.commit('updateLandmarkPictures', response.data);
            })
            .catch(error => {
                console.error('Error sending data to Python server (landmark):', error);
            });

        axios.post('http://localhost:8000/api/shopping_photo_data', data)
            .then(response => {
                console.log("Shopping Pictures", response.data); // Log response from Python server
                this.$store.commit('updateShopPictures', response.data);
            })
            .catch(error => {
                console.error('Error sending data to Python server (shopping):', error);
            });

        axios.post('http://localhost:8000/api/hotel_photo_data', data)
            .then(response => {
                console.log("Hotel Pictures", response.data); // Log response from Python server
                this.$store.commit('updateHotelPictures', response.data);
            })
            .catch(error => {
                console.error('Error sending data to Python server (hotel):', error);
            });






        // Retrieve Trip Details
        const activityPictures = this.$store.state.activityPictures;
        const landmarkPictures = this.$store.state.landmarkPictures;
        const restaurantPictures = this.$store.state.foodPictures;
        const shopPictures = this.$store.state.shopPictures;
        const hotelPictures = this.$store.state.hotelPictures;

        const tripObject = this.$route.params.tripObject;
        const trip_id = this.$store.state.tripObject.id;
        this.fetchSavedTripDetails(trip_id);
        setTimeout(() => {
            console.log("1 second has passed!");
            // Add your desired action to be executed after 1 second here
            const selectedActivities = this.savedTrip.activities;
            const selectedLandmarks = this.savedTrip.landmarks;
            const selectedFoods = this.savedTrip.foods;
            const selectedShops = this.savedTrip.shops;
            const selectedHotel = this.savedTrip.hotels;
            console.log("Saved activities from database from savedItinerary2: ", this.savedTrip.activities);
            console.log("Activities from vuex: ", this.$store.state.tripObject.activities);



            //const selectedActivities = this.$store.state.tripObject.activities;
            //const selectedLandmarks = this.$store.state.tripObject.landmarks;
            //const selectedFoods = this.$store.state.tripObject.foods;
            //const selectedShops = this.$store.state.tripObject.shops;
            //const selectedHotel = this.$store.state.tripObject.hotels;
            const selectedHotelString = selectedHotel.join(', '); // Use a comma and a space as the separator
            console.log(selectedHotelString)
            console.log("Trip id from savedItinerary2: ", trip_id);
            // console.log("This is the activities array: " + selectedActivities)
            // console.log("This is the hotel array: " + selectedHotel)
            const hotelPictureString = hotelPictures.join(', ');


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

            const parseTitleFromString = (str) => {
                const parts = str.split(':');
                return parts[0].trim();
            };

            // Separating the titles from the descriptions
            const activityTitles = getActivityTitles(selectedActivities);
            const landmarkTitles = getActivityTitles(selectedLandmarks);
            const foodTitles = getActivityTitles(selectedFoods);
            const shopTitles = getActivityTitles(selectedShops);
            const hotelTitles = parseTitleFromString(selectedHotelString);

            // Round robin sort for all of the pictures
            const sortedPictures = getRoundRobinSlice([activityPictures, landmarkPictures, restaurantPictures, shopPictures]);
            sortedPictures.unshift(hotelPictureString);
            console.log("Sorted Pictures: ", sortedPictures);

            const sortedArray = getRoundRobinSlice([selectedActivities, selectedLandmarks, selectedFoods, selectedShops]);
            sortedArray.unshift(selectedHotelString);
            console.log(sortedArray);

            const combinedArray = removeTitles(sortedArray);


            const combinedTitles = getRoundRobinSlice([activityTitles, landmarkTitles, foodTitles, shopTitles]);
            combinedTitles.unshift(hotelTitles);
            // console.log("Combined Description: " + combinedArray)
            // console.log("Combined Titles: " + combinedTitles)
            console.log("Sorted array without titles: " + combinedArray);

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
            let photoIndex = -1;

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
                        image: sortedPictures[photoIndex += 1]
                    }))
                };
                // Update the current index
                this.itinerary.push(daySection);
            }
        }, 500);


    },




    mounted() {
        // console.log("HEY!!!")
        // const tripObject = this.$route.params.tripObject;
        const tripObject = this.$store.state.tripObject;

        // console.log("This is the saved object: " + tripObject)
        // console.log("activities: " + this.$store.state.tripObject.activities)

    },
    methods: {
        send() {
            // const tripObjectCopy = JSON.parse(JSON.stringify(this.$store.state.tripObject));
            // console.log(tripObjectCopy);  // Ensure the copy has the expected data

            // // Push to the new route
            // this.$router.push({ name: 'SavedItinerary', params: { tripObject: tripObjectCopy } }).catch(err => {
            //     console.error(err);
            // }).then(() => {
            //     // Force reload the page to reset everything
            //     window.location.reload();
            // });
            this.$store.state.tripObject.activities = this.selectedActivities;
            this.$store.state.tripObject.foods = this.selectedFoods;
            this.$store.state.tripObject.landmarks = this.selectedLandmarks;
            this.$store.state.tripObject.shops = this.selectedShops;
            this.$store.state.tripObject.hotels = this.selectedHotels;

            const new_selections = {
                activities: this.selectedActivities,
                foods: this.selectedFoods,
                landmarks: this.selectedLandmarks,
                shops: this.selectedShops,
                hotels: this.selectedHotels,
            };
            //console.log(tripObjectCopy);  // Ensure the copy has the expected data
            //console.log("Vuex tripObject: ", this.$store.state.tripObject);

            axios.put(`http://localhost:8000/api/update_trip_selections/${this.$store.state.tripObject.id}`, new_selections)
                .then(response => {
                    console.log('New selections saved to database.', response.data);
                    console.log('Snackbar', showSelectionChangesSnackbar);
                })
                .catch(error => {
                    console.error('Error saving changes to database:', error);
                    // Handle error
                });
            setTimeout(() => {
                window.location = '/SavedItinerary'; // Directly navigate to home and refresh
            }, 1000);

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
        fetchSavedTripDetails(trip_id) {
            const jwtToken = Cookies.get('login_token');
            //const url = '/fetch_saved_itinerary/<trip_id>'
            // console.log("Token works: " + jwtToken);
            axios.get(`http://localhost:8000/api/fetch_saved_itinerary/${trip_id}`, {
                headers: {
                    Authorization: `Bearer ${jwtToken}` // Include the JWT token in the Authorization header
                }
            })
                .then(response => {
                    this.savedTrip = response.data.savedTrip;
                    console.log('Saved trip from database in savedItinerary2: ', this.savedTrip);
                })
                .catch(error => {
                    console.error('Error fetching saved trip:', error);
                });
        },
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