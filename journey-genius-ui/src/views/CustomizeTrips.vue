<template>
    <v-app>
        <v-container>

            <v-snackbar v-model="showSelectionChangesSnackbar" color="deep-purple-accent-2" top>
                <span class="centered-text">Trip selections changed successfully.</span>
            </v-snackbar>

            <!-- Header -->
            <v-row justify="center" class="mt-4">
                <v-col cols="12" md="8" class="text-center">
                    <!-- User Selections changed snackbar -->

                    <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">
                        Plan Your Next Adventure in
                    </h2>
                    <h1 style="font-size: 3.5rem;" class="headline text-deep-purple-accent-2">
                        <!-- {{ cityData }}, {{ fullName }} -->
                        {{ this.$store.state.tripObject.city }}, {{ this.$store.state.tripObject.state }}
                    </h1>
                    <h1 style="font-size: 1rem;" class="headline text-deep-purple-accent-2">
                        <!-- Planned for {{ combinedDates }} with a {{ budgetString }} budget trip. -->
                        Planned for {{ this.$store.state.tripObject.dates }} with a {{
                            this.$store.state.tripObject.budget }} budget trip.
                    </h1>
                    <p style="margin-top: 10px;">
                        The activities you select will form your final itinerary. You are required to check at least one
                        box
                        in
                        every category. Once you are content with the activities that have piqued your interest, proceed
                        to
                        the
                        next step.
                    </p>
                    <br />
                    <hr />

                </v-col>
            </v-row>

            <!-- Category: Choose the Activities that Peak Your Interest -->
            <v-row justify="center" class="mt-4">
                <v-col cols="12" md="8">
                    <h2 class="headline text-deep-purple-accent-2">Choose the Activities that Peak Your Interest</h2>
                    <br>
                    <v-row dense>
                        <v-col v-for="(activity, index) in activities" :key="index" cols="12">
                            <v-checkbox v-model="selectedActivities" @change="updateSelectedActivities"
                                :value="activity" :label="Array.isArray(activity) ? activity.join(', ') : activity"
                                color="deep-purple-accent-2" class="mb-1"></v-checkbox>
                        </v-col>

                    </v-row>
                    <v-col class="d-flex justify-center">
                        <!-- <v-btn @click="redirectToMoreActivitiesPage" color="deep-purple-accent-2">See More Activities</v-btn> -->
                        <div v-if="showActivitiesError" class="error-message">{{ activitiesErrorMessage }}</div>

                    </v-col>
                </v-col>
            </v-row>

            <!-- Category: Iconic Landmarks and Photo Opportunities -->
            <v-row justify="center" class="mt-4">
                <v-col cols="12" md="8">
                    <h2 class="headline text-deep-purple-accent-2">Iconic Landmarks and Photo Opportunities</h2>
                    <br>
                    <v-row dense>
                        <v-col v-for="(landmark, index) in landmarks" :key="index" cols="12">
                            <v-checkbox v-model="selectedLandmarks" @change="updateSelectedLandmarks" :value="landmark"
                                :label="Array.isArray(landmark) ? landmark.join(', ') : landmark"
                                color="deep-purple-accent-2" class="mb-1"></v-checkbox>
                        </v-col>
                    </v-row>
                    <v-col class="d-flex justify-center">
                        <!-- <v-btn @click="redirectToMoreLandmarksPage" color="deep-purple-accent-2">See More Landmarks</v-btn> -->
                        <div v-if="showLandmarksError" class="error-message">{{ landmarksErrorMessage }}</div>
                    </v-col>
                </v-col>
            </v-row>

            <!-- Category: What do You want to Eat? -->
            <v-row justify="center" class="mt-4" dense>
                <v-col cols="12" md="8">
                    <h2 class="headline text-deep-purple-accent-2">What Do You Want to Eat?</h2>
                    <br>
                    <v-row dense>
                        <v-col v-for="(food, index) in foods" :key="index" cols="12">
                            <v-checkbox v-model="selectedFoods" @change="updateSelectedFoods" :value="food"
                                :label="Array.isArray(food) ? food.join(', ') : food" color="deep-purple-accent-2"
                                class="mb-1"></v-checkbox>
                        </v-col>
                    </v-row>
                    <v-col class="d-flex justify-center">
                        <!-- <v-btn @click="redirectToMoreDiningPage" color="deep-purple-accent-2">See More Dining Options</v-btn> -->
                        <div v-if="showFoodError" class="error-message">{{ foodErrorMessage }}</div>
                    </v-col>
                </v-col>
            </v-row>


            <!-- Category: Shopping Spots -->
            <v-row justify="center" class="mt-4">
                <v-col cols="12" md="8">
                    <h2 class="headline text-deep-purple-accent-2">Shopping Spots</h2>
                    <br>
                    <v-row dense>
                        <v-col v-for="(shop, index) in shops" :key="index" cols="12">
                            <v-checkbox v-model="selectedShops" @change="updateSelectedShops" :value="shop"
                                :label="Array.isArray(shop) ? shop.join(', ') : shop" color="deep-purple-accent-2"
                                class="mb-1"></v-checkbox>
                        </v-col>
                    </v-row>
                    <v-col class="d-flex justify-center">
                        <!-- <v-btn @click="redirectToMoreShoppingPage" color="deep-purple-accent-2">See More Retail Stores</v-btn> -->
                        <div v-if="showShoppingError" class="error-message">{{ shoppingErrorMessage }}</div>
                    </v-col>
                </v-col>
            </v-row>

            <!-- Category: Hotel Spots -->
            <v-row justify="center" class="mt-4">
                <v-col cols="12" md="8">
                    <h2 class="headline text-deep-purple-accent-2">Where Will You Be Staying?</h2>
                    <br>
                    <v-row dense>
                        <v-col v-for="(hotel, index) in hotels" :key="index" cols="12">
                            <v-checkbox v-model="selectedHotels" @change="updateSelectedHotels" :value="hotel"
                                :label="Array.isArray(hotel) ? hotel.join(', ') : hotel" color="deep-purple-accent-2"
                                class="mb-1"></v-checkbox>
                        </v-col>
                    </v-row>
                    <v-col class="d-flex justify-center">
                        <!-- <v-btn @click="redirectToMoreShoppingPage" color="deep-purple-accent-2">See More Retail Stores</v-btn> -->
                        <div v-if="showHotelError" class="error-message">{{ hotelErrorMessage }}</div>
                    </v-col>
                </v-col>
            </v-row>
        </v-container>

        <!-- Two buttons on the bottom -->
        <v-row justify="center" class="mt-4">
            <v-col cols="12" md="8" class="text-center">
                <hr />

                <v-btn size="large" color="deep-purple-accent-2" class="white--text mt-6 mr-2"
                    @click="showConfirmationDialog" style="min-width: 150px;">
                    Cancel Changes
                </v-btn>

                <v-dialog v-model="dialogVisible" max-width="650">
                    <v-card>
                        <v-card-title class="headline"
                            style="padding-left: 25px; padding-top: 15px;">Confirmation</v-card-title>
                        <v-card-text>
                            Would you like to return to the itinerary overview page? Any unsaved changes will be lost.
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="deep-purple-accent-2" text @click="dialogVisible = false">No</v-btn>
                            <v-btn color="red darken-1" text @click="goBack">Yes</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>

                <!-- <router-link to="/GeneratedItinerary"> -->
                <v-btn size="large" color="deep-purple-accent-2" class="white--text mt-6 ml-2" @click="updateTravelInfo"
                    style="min-width: 150px;">
                    Save Changes
                </v-btn>
                <!-- </router-link> -->
            </v-col>
        </v-row>
    </v-app>
</template>

<script>
import { defineComponent } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import { mapState, mapMutations } from 'vuex';
import axios from 'axios';
import LoadingScreenShort from '@/components/LoadingScreenShort.vue';


export default defineComponent({
    data() {
        return {
            showSelectionChangesSnackbar: false,

            activities: [],
            landmarks: [],
            foods: [],
            shops: [],
            hotels: [],
            selectedActivities: [],
            selectedLandmarks: [],
            selectedFoods: [],
            selectedShops: [],
            selectedHotels: [],

            cityData: [],
            startDateData: [],
            endDateData: [],
            budgetData: [],

            savedDates: [],

            state: [],
            stateMap: {
                AL: 'Alabama',
                AK: 'Alaska',
                AZ: 'Arizona',
                AR: 'Arkansas',
                CA: 'California',
                CO: 'Colorado',
                CT: 'Connecticut',
                DE: 'Delaware',
                FL: 'Florida',
                GA: 'Georgia',
                HI: 'Hawaii',
                ID: 'Idaho',
                IL: 'Illinois',
                IN: 'Indiana',
                IA: 'Iowa',
                KS: 'Kansas',
                KY: 'Kentucky',
                LA: 'Louisiana',
                ME: 'Maine',
                MD: 'Maryland',
                MA: 'Massachusetts',
                MI: 'Michigan',
                MN: 'Minnesota',
                MS: 'Mississippi',
                MO: 'Missouri',
                MT: 'Montana',
                NE: 'Nebraska',
                NV: 'Nevada',
                NH: 'New Hampshire',
                NJ: 'New Jersey',
                NM: 'New Mexico',
                NY: 'New York',
                NC: 'North Carolina',
                ND: 'North Dakota',
                OH: 'Ohio',
                OK: 'Oklahoma',
                OR: 'Oregon',
                PA: 'Pennsylvania',
                RI: 'Rhode Island',
                SC: 'South Carolina',
                SD: 'South Dakota',
                TN: 'Tennessee',
                TX: 'Texas',
                UT: 'Utah',
                VT: 'Vermont',
                VA: 'Virginia',
                WA: 'Washington',
                WV: 'West Virginia',
                WI: 'Wisconsin',
                WY: 'Wyoming',
            },

            dialogVisible: false,

            activitiesErrorMessage: "",
            showActivitiesError: false,
            landmarksErrorMessage: "",
            showLandmarksError: false,
            foodErrorMessage: "",
            showFoodError: false,
            shoppingErrorMessage: "",
            showShoppingError: false,
            hotelErrorMessage: "",
            showHotelError: false,

            isLoading: false,
        };
    },
    methods: {
        formatDate(date) {
            const options = { month: 'long', day: 'numeric', year: 'numeric' };
            return new Date(date).toLocaleDateString('en-US', options);
        },
        showConfirmationDialog() {
            this.dialogVisible = true;
        },
        goBack() {
            this.$router.push("/SavedItinerary");
        },

        //////////////////////////////// ISAAC!!! THIS IS THE SECTION WHERE YOU HAVE TO UPDATE THE USER SELECTION /////////////////////////////////////////////////////////
        // Should change the saved trip object

        updateSelectedActivities() {
            this.$store.commit('updateActivities', this.selectedActivities);
            console.log("Activities stored in Vuex: " + this.$store.state.activities);
        },
        updateSelectedLandmarks() {
            this.$store.commit('updateLandmarks', this.selectedLandmarks);
            console.log("Landmarks stored in Vuex: " + this.$store.state.landmarks);
        },
        updateSelectedFoods() {
            this.$store.commit('updateFoods', this.selectedFoods);
            console.log("Restaurants stored in Vuex: " + this.$store.state.foods);
        },
        updateSelectedShops() {
            this.$store.commit('updateShops', this.selectedShops);
            console.log("Shopping Spots stored in Vuex: " + this.$store.state.shops);
        },
        updateSelectedHotels() {
            this.$store.commit('updateHotels', this.selectedHotels);
            console.log("Hotels stored in Vuex: " + this.$store.state.hotels);
        },


        updateTravelInfo() {
            let isValid = true; // Assume input is valid unless proven otherwise

            // Check if at least one activity is selected
            if (this.selectedActivities.length === 0) {
                this.activitiesErrorMessage = "Please select at least one activity.";
                // console.log("No work!")
                this.showActivitiesError = true;
                isValid = false;
            } else {
                this.showActivitiesError = false;
            }

            if (this.selectedLandmarks.length === 0) {
                this.landmarksErrorMessage = "Please select at least one landmark.";
                // console.log("No work!")
                this.showLandmarksError = true;
                isValid = false;
            } else {
                this.showLandmarksError = false;
            }

            if (this.selectedFoods.length === 0) {
                this.foodErrorMessage = "Please select at least one dining option.";
                // console.log("No work!")
                this.showFoodError = true;
                isValid = false;
            } else {
                this.showFoodError = false;
            }

            if (this.selectedShops.length === 0) {
                this.shoppingErrorMessage = "Please select at least one shopping spot.";
                // console.log("No work!")
                this.showShoppingError = true;
                isValid = false;
            } else {
                this.showShoppingError = false;
            }

            if (this.selectedHotels.length === 0) {
                this.hotelErrorMessage = "Please select a housing option.";
                // console.log("No work!")
                this.showHotelError = true;
                isValid = false;
            } else {
                this.showHotelError = false;
            }

            // If any input is not valid, exit the method
            if (!isValid) {
                return;
            }

            // Loading Screen
            // this.isLoading = true;
            //const newTripObject = this.$store.state.tripObject;

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
            const updatedObject = {
                id: this.$store.state.tripObject.id,
                city: this.$store.state.tripObject.city,
                city_description: this.$store.state.tripObject.city_description,
                activities: this.$store.state.tripObject.activities,
                landmarks: this.$store.state.tripObject.landmarks,
                foods: this.$store.state.tripObject.foods,
                shops: this.$store.state.tripObject.shops,
                hotels: this.$store.state.tripObject.hotels,
                state: this.$store.state.tripObject.state,
                dates: this.$store.state.tripObject.dates,
                budget: this.$store.state.tripObject.budget,
                latitude: this.$store.state.tripObject.latitude,
                longitude: this.$store.state.tripObject.longitude,
                city_slogan: this.$store.state.tripObject.city_slogan,
                generated_activities: this.$store.state.tripObject.generated_activities,
                generated_hotels: this.$store.state.tripObject.generated_hotels,
                generated_shops: this.$store.state.tripObject.generated_shops,
                generated_foods: this.$store.state.tripObject.generated_foods,
                generated_landmarks: this.$store.state.tripObject.generated_landmarks,
            };
            // this.$store.commit('updateTripObject', this.updatedObject);
            // console.log(this.updatedObject)

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
            this.showSelectionChangesSnackbar = true;
            this.$router.push({ name: 'SavedItinerary', params: { tripObject: this.$store.state.tripObject } });
        }

    },
    mounted() {

        this.selectedActivities = this.$store.state.tripObject.activities;
        this.selectedFoods = this.$store.state.tripObject.foods;
        this.selectedLandmarks = this.$store.state.tripObject.landmarks;
        this.selectedShops = this.$store.state.tripObject.shops;
        this.selectedHotels = this.$store.state.tripObject.hotels;
        // console.log('Selected activities from customize trip mounted: ', this.selectedActivities);
        // console.log('Selected foods from customize trip mounted: ', this.selectedFoods);
        // console.log('Selected landmarks from customize trip mounted: ', this.selectedLandmarks);
        // console.log('Selected shops from customize trip mounted: ', this.selectedShops);
        // console.log('Selected hotels from customize trip mounted: ', this.selectedHotels);
        // const activityData = JSON.parse(this.$route.query.activityData);
        // if (activityData && activityData.recommended_places) {
        //     this.activities = activityData.recommended_places;
        // }

        // const landmarkData = JSON.parse(this.$route.query.landmarkData);
        // if (landmarkData && landmarkData.recommended_places) {
        //     this.landmarks = landmarkData.recommended_places;
        // }

        // const restaurantData = JSON.parse(this.$route.query.restaurantData);
        // if (restaurantData && restaurantData.recommended_places) {
        //     this.foods = restaurantData.recommended_places;
        // }

        // const shoppingData = JSON.parse(this.$route.query.shoppingData);
        // if (shoppingData && shoppingData.recommended_places) {
        //     this.shops = shoppingData.recommended_places;
        // }

        // const hotelData = JSON.parse(this.$route.query.hotelData);
        // if (hotelData && hotelData.recommended_places) {
        //     this.hotels = hotelData.recommended_places;
        // }

        // const cityData = JSON.parse(this.$route.query.cityData);
        // this.cityData = cityData; 

        // const state = JSON.parse(this.$route.query.stateData);
        // this.state = state;

        // const budgetData = JSON.parse(this.$route.query.budgetData);
        // this.budgetData = budgetData;

        // const startDateData = JSON.parse(this.$route.query.startDateData);
        // this.startDateData = startDateData;

        // const endDateData = JSON.parse(this.$route.query.endDateData);
        // this.endDateData = endDateData;
    },
    created() {

        // THIS IS ALL OF THE USER SELECTED OPTIONS
        // const tripObject = this.$route.params.tripObject;
        // const activityData = this.$store.state.tripObject.activities;
        // const landmarkData = this.$store.state.tripObject.landmarks;
        // const restaurantData = this.$store.state.tripObject.foods;
        // const shoppingData = this.$store.state.tripObject.shops;
        // const hotelData = this.$store.state.tripObject.hotels;

        // THIS IS ALL OF THE SAVED GENERATED OPTIONS
        const tripObject = this.$route.params.tripObject;
        const activityData = this.$store.state.tripObject.generated_activities;
        const landmarkData = this.$store.state.tripObject.generated_landmarks;
        const restaurantData = this.$store.state.tripObject.generated_foods;
        const shoppingData = this.$store.state.tripObject.generated_shops;
        const hotelData = this.$store.state.tripObject.generated_hotels;


        this.activities = activityData;
        this.landmarks = landmarkData;
        this.foods = restaurantData;
        this.shops = shoppingData;
        this.hotels = hotelData;
    },



    computed: {
        budgetString() {
            if (this.budgetData === 1) {
                this.$store.commit('updateBudget', "cheap");
                console.log("Budget stored in Vuex: " + this.$store.state.budget); // Log the activities stored in Vuex
                return "cheap";
            } else if (this.budgetData === 2) {
                this.$store.commit('updateBudget', "medium");
                console.log("Budget stored in Vuex: " + this.$store.state.budget); // Log the activities stored in Vuex
                return "medium";
            } else if (this.budgetData === 3) {
                this.$store.commit('updateBudget', "expensive");
                console.log("Budget stored in Vuex: " + this.$store.state.budget); // Log the activities stored in Vuex
                return "expensive";
            } else {
                return "Unknown";
            }
        },
        combinedDates() {
            if (this.startDateData && this.endDateData) {
                const startDateFormat = this.formatDate(this.startDateData);
                const endDateFormat = this.formatDate(this.endDateData);
                const datesData = `${startDateFormat} - ${endDateFormat}`;

                this.$store.commit('updateDates', datesData);
                console.log("Dates data stored in Vuex: " + datesData);

                return `${startDateFormat} - ${endDateFormat}`;
            }
            return '';
        },
        fullName() {
            const stateData = this.stateMap[this.state] || this.state;
            this.$store.commit('updateState', stateData);
            console.log("State data stored in Vuex: " + stateData);
            return this.stateMap[this.state] || this.state;
        },

    },
    components: {
        LoadingScreenShort,
    },

});
</script>

<style>
.mb-1 .v-label {
    font-size: 18px;
}

.error-message {
    color: red;
    margin-top: 5px;
    margin-bottom: 5px;
    font-size: 18px;
}
</style>