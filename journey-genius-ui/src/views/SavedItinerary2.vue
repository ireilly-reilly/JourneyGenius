<template>
    <v-container fluid class="no-border">
        <v-snackbar v-model="showSnackbar" color="deep-purple-accent-2" top>
            <span class="text-center">Trip Saved Successfully</span>
        </v-snackbar>
        <v-row>
            <v-col v-for="(day, index) in itinerary" :key="index" cols="12">
                <v-card class="activity-card" style="display: flex; flex-direction: column; height: 100%;">
                    <v-card-title :class="['headline', fontSizeClass(index)]">
                        <v-icon v-if="timelineIcon(index)" :class="['mr-2', iconColorClass(index)]">
                            {{ timelineIcon(index) }}
                        </v-icon>
                        {{ day.title }}
                    </v-card-title>
                    <br>
                    <br>
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
import Cookies from 'js-cookie';
export default {
    data() {

        return {
            itinerary: [],
            showSnackbar: false,
            // itinerary: [
            //     {
            //         title: 'Day 1 - Tuesday, December 13',
            //         activities: [
            //             {
            //                 name: 'Check into your Hotel',
            //                 description: 'You\'ve selected Hotel Nikko San Francisco at 222 Mason St, San Francisco, CA 94102, USA. Head to your hotel to check in and settle in comfortably!',
            //                 image: require('@/assets/hotel.jpeg'),
            //             },
            //             {
            //                 name: 'Golden State Bridge',
            //                 description: 'An absolute classic, the Golden Gate Bridge is one of the most recognizable landmarks in the world. Head to viewpoints like Battery Spencer or the Golden Gate Overlook for breathtaking shots.',
            //                 image: require('@/assets/goldenstatebridge2.jpeg'),
            //             },
            //             {
            //                 name: 'Lunch at Local Restaurant',
            //                 description: 'Swan Oyster Depot (1517 Polk St) - A historic seafood counter that serves fresh and delicious seafood. It\'s a popular spot,so be prepared for a wait.',
            //                 image: require('@/assets/swanOyster.jpeg'),
            //             },
            //         ],
            //     },
            //     {
            //         title: 'Day 2 - Wednesday, February 14',
            //         activities: [
            //             {
            //                 name: 'Botanical Garden at Strybing Arboretum',
            //                 description: 'Located in Golden Gate Park, this garden showcases a wide variety of plants from around the world in a beautifully landscaped setting.',
            //                 image: require('@/assets/garden.jpeg'),
            //             },
            //             {
            //                 name: 'Tea Hut (280 Golden Gate Ave)',
            //                 description: 'A Chinatown favorite, Tea Hut serves a variety of teas, including boba, fruit teas, and slushies.',
            //                 image: require('@/assets/boba2.jpeg'),
            //             },
            //             {
            //                 name: 'Union Square',
            //                 description: 'Known as the city\'s premier shopping destination, Union Square is home to flagship stores of major brands such as Macy\'s, Saks Fifth Avenue, Neiman Marcus, and Apple. You\'ll also find a variety of luxury boutiques and department stores in the surrounding area.',
            //                 image: require('@/assets/unionsquare2.jpeg'),
            //             },
            //             {
            //                 name: 'Fisherman\'s Wharf',
            //                 description: 'This popular tourist destination offers a mix of souvenir shops, specialty stores, and waterfront markets. It\'s a lively area with a variety of shopping options.',
            //                 image: require('@/assets/wharf2.jpeg'),
            //             },
            //             {
            //                 name: 'Ghirardelli Square (900 North Point St)',
            //                 description: 'While primarily known for its chocolate shops, Ghirardelli Square also houses boutique stores, galleries, and restaurants. It\'s a great place to shop while enjoying views of the bay.',
            //                 image: require('@/assets/gs.jpeg'),
            //             },
            //             {
            //                 name: 'Sailing on the Bay',
            //                 description: 'Charter a sailboat or join a sailing tour to experience the beauty of San Francisco from the water.',
            //                 image: require('@/assets/ferry.jpeg'),
            //             }

            //         ],
            //     },
            //     {
            //         title: 'Day 3 - Thursday, February 15',
            //         activities: [
            //             {
            //                 name: 'Haight-Ashbury',
            //                 description: 'If you\'re into vintage and alternative fashion, head to Haight-Ashbury. This historic neighborhood is known for its eclectic mix of shops, including vintage clothing stores and quirky boutiques.',
            //                 image: require('@/assets/HaightAshbury.jpeg'),
            //             },
            //             {
            //                 name: 'Hiking in the Marin Headlands',
            //                 description: 'Explore the network of hiking trails in the Marin Headlands for stunning views of the Golden Gate Bridge, the Pacif ic Ocean, and the San Francisco skyline.',
            //                 image: require('@/assets/MarinHeadlands.jpg'),
            //             },
            //             {
            //                 name: 'Beach Day at Ocean Beach',
            //                 description: 'Enjoy a day at Ocean Beach, located on the western edge of the city. It\'s a great spot for a beach walk, picnics, and watching the sunset over the Pacific.',
            //                 image: require('@/assets/sfbeach.jpeg'),
            //             },
            //             {
            //                 name: 'Rich Table (199 Gough St)',
            //                 description: 'A Michelin-starred restaurant that offers creative and seasonal dishes in a relaxed and inviting setting.',
            //                 image: require('@/assets/food.jpeg'),
            //             },
            //             {
            //                 name: 'Flight Back Home',
            //                 description: 'Enjoy a smooth transition from the vibrant cityscape to the comfort of air travel as you drive to San Francisco International Airport (SFO), winding through iconic streets before arriving at the modern terminals for your journey home.',
            //                 image: require('@/assets/sfo2.jpeg'),
            //             }
            //         ],
            //     }

            //     // Add more days as needed
            // ],
        };
    },
    // created() {

    //     const tripObject = this.$route.params.tripObject;

    //     const dateRangeString = this.$store.state.tripObject.dates;
    //     // console.log(dateRangeString)

    //     // Parse date range
    //     const [startDateString, endDateString] = dateRangeString.split(" - ");

    //     // Parse start and end dates
    //     const startDate = this.parseDateString(startDateString);
    //     const endDate = this.parseDateString(endDateString);

    //     // Calculate the trip duration
    //     const daysDifference = this.calculateTripDuration(startDate, endDate);
    //     // console.log(daysDifference)

    //     const selectedActivities = this.$store.state.tripObject.activities;
    //     const selectedLandmarks = this.$store.state.tripObject.landmarks;
    //     // console.log("Selected Landmarks: " + selectedLandmarks)

    //     const selectedFoods = this.$store.state.tripObject.foods;
    //     const selectedShops = this.$store.state.tripObject.shops;
    //     console.log("Activities: " + selectedActivities + "\nLandmarks: " + selectedLandmarks + "\nFoods: " + selectedFoods + "\nShops: " + selectedShops)


    //     console.log("Days difference: " + daysDifference)
    //     console.log(selectedActivities.length + " " + selectedLandmarks.length + " " + selectedFoods.length + " " + selectedShops.length)

    //     // Calculate the number of items per day for each type
    //     const activitiesPerDay = Math.ceil(selectedActivities.length / daysDifference);
    //     const landmarksPerDay = Math.ceil(selectedLandmarks.length / daysDifference);
    //     const foodsPerDay = Math.ceil(selectedFoods.length / daysDifference);
    //     const shopsPerDay = Math.ceil(selectedShops.length / daysDifference);
    //     console.log("Activities per day: " + activitiesPerDay + "\nLandmarks: " + landmarksPerDay + "\nFoods: " + foodsPerDay + "\nShops: " + shopsPerDay)

    //     // Initialize indexes for slicing
    //     let activityIndex = 0;
    //     let landmarkIndex = 0;
    //     let foodIndex = 0;
    //     let shopIndex = 0;


    //     // Generate itinerary sections for each day
    //     for (let i = 0; i < daysDifference; i++) {
    //         const currentDate = new Date(startDate);
    //         currentDate.setDate(startDate.getDate() + i);
    //         const dayTitle = `Day ${i + 1} - ${this.formatDate(currentDate)}`;

    //         // Slice items for the day, using modulo to reset index to beginning if end of list is reached
    //         const dayActivities = selectedActivities.slice(activityIndex, activityIndex + activitiesPerDay);
    //         const dayLandmarks = selectedLandmarks.slice(landmarkIndex, landmarkIndex + landmarksPerDay);
    //         const dayFoods = selectedFoods.slice(foodIndex, foodIndex + foodsPerDay);
    //         const dayShops = selectedShops.slice(shopIndex, shopIndex + shopsPerDay);

    //         // Update indexes for the next iteration, without wrapping around
    //         activityIndex += activitiesPerDay;
    //         landmarkIndex += landmarksPerDay;
    //         foodIndex += foodsPerDay;
    //         shopIndex += shopsPerDay;

    //         // Ensure the indexes do not exceed the total number of items
    //         activityIndex = Math.min(activityIndex, selectedActivities.length);
    //         landmarkIndex = Math.min(landmarkIndex, selectedLandmarks.length);
    //         foodIndex = Math.min(foodIndex, selectedFoods.length);
    //         shopIndex = Math.min(shopIndex, selectedShops.length);


    //         const daySection = {
    //             title: dayTitle,
    //             activities: [
    //                 ...dayActivities.map(activity => ({
    //                     name: activity.name,
    //                     description: dayActivities,
    //                     image: activity.image,
    //                 })),
    //                 ...dayLandmarks.map(landmark => ({
    //                     name: landmark.name,
    //                     description: dayLandmarks,
    //                     image: landmark.image,
    //                 })),
    //                 ...dayFoods.map(food => ({
    //                     name: food.name,
    //                     description: dayFoods,
    //                     image: food.image,
    //                 })),
    //                 ...dayShops.map(shop => ({
    //                     name: shop.name,
    //                     description: dayShops,
    //                     // description: shop.description,
    //                     image: shop.image,
    //                 })),
    //             ],
    //         };
    //         this.itinerary.push(daySection);
    //     }
    // },


    created() {
    const tripObject = this.$route.params.tripObject;
    const dateRangeString = this.$store.state.tripObject.dates;

    // Parse date range
    const [startDateString, endDateString] = dateRangeString.split(" - ");
    const startDate = this.parseDateString(startDateString);
    const endDate = this.parseDateString(endDateString);

    // Calculate the trip duration
    const daysDifference = this.calculateTripDuration(startDate, endDate);

    const selectedActivities = this.$store.state.tripObject.activities;;
    const selectedLandmarks = this.$store.state.tripObject.landmarks;
    const selectedFoods = this.$store.state.tripObject.foods;
    const selectedShops = this.$store.state.tripObject.shops;

    // Calculate the number of items per day for each type
    const activitiesPerDay = Math.ceil(selectedActivities.length / daysDifference);
    const landmarksPerDay = Math.ceil(selectedLandmarks.length / daysDifference);
    const foodsPerDay = Math.ceil(selectedFoods.length / daysDifference);
    const shopsPerDay = Math.ceil(selectedShops.length / daysDifference);

    // Initialize indexes for slicing
    let activityIndex = 0;
    let landmarkIndex = 0;
    let foodIndex = 0;
    let shopIndex = 0;

    // Generate itinerary sections for each day
    for (let i = 0; i < daysDifference; i++) {
        const currentDate = new Date(startDate);
        currentDate.setDate(startDate.getDate() + i);
        const dayTitle = `Day ${i + 1} - ${this.formatDate(currentDate)}`;

        // Slice items for the day, using modulo to reset index to beginning if end of list is reached
        const dayActivities = this.getRoundRobinSlice(selectedActivities, activityIndex, activitiesPerDay);
        const dayLandmarks = this.getRoundRobinSlice(selectedLandmarks, landmarkIndex, landmarksPerDay);
        const dayFoods = this.getRoundRobinSlice(selectedFoods, foodIndex, foodsPerDay);
        const dayShops = this.getRoundRobinSlice(selectedShops, shopIndex, shopsPerDay);

        // Update indexes for the next iteration, without wrapping around
        activityIndex = (activityIndex + activitiesPerDay) % selectedActivities.length;
        landmarkIndex = (landmarkIndex + landmarksPerDay) % selectedLandmarks.length;
        foodIndex = (foodIndex + foodsPerDay) % selectedFoods.length;
        shopIndex = (shopIndex + shopsPerDay) % selectedShops.length;

        const daySection = {
            title: dayTitle,
            activities: [
                ...dayActivities.map(activity => ({
                    name: activity.name,
                    description: dayActivities,
                    image: activity.image,
                    // name: activity.name,
                    // description: activity.description,
                    // image: activity.image,
                })),
                ...dayLandmarks.map(landmark => ({
                    name: landmark.name,
                    description: dayLandmarks,
                    image: landmark.image,
                })),
                ...dayFoods.map(food => ({
                    name: food.name,
                    description: dayFoods,
                    image: food.image,
                })),
                ...dayShops.map(shop => ({
                    name: shop.name,
                    description: dayShops,
                    image: shop.image,
                })),
            ],
        };
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
        getRoundRobinSlice(arr, startIndex, count) {
        const length = arr.length;
        const slice = [];
        for (let i = 0; i < count; i++) {
            slice.push(arr[(startIndex + i) % length]);
        }
        return slice;
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
    overflow: hidden;
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