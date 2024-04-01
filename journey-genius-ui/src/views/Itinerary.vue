<template>
    <v-app>
        <v-container>
            <LoadingScreenShort v-if="isLoading" />
            <!-- Header -->
            <v-row justify="center" class="mt-4">
                <v-col cols="12" md="8" class="text-center">
                    <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">
                        Plan Your Next Adventure in
                    </h2>
                    <h1 style="font-size: 3.5rem;" class="headline text-deep-purple-accent-2">
                        {{ cityData }}, {{ fullName }}
                    </h1>
                    <h1 style="font-size: 1rem;" class="headline text-deep-purple-accent-2">
                        Planned for {{ combinedDates }} with a {{ budgetString }} budget trip.
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

                <v-btn color="deep-purple-accent-2" class="white--text mt-6 mr-2" @click="showConfirmationDialog"
                    style="min-width: 150px;">
                    Go Back
                </v-btn>

                <v-dialog v-model="dialogVisible" max-width="650">
                    <v-card>
                        <v-card-title class="headline"
                            style="padding-left: 25px; padding-top: 15px;">Confirmation</v-card-title>
                        <v-card-text>
                            Are you sure you want to go back? This will restart your planning progress.
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="deep-purple-accent-2" text @click="dialogVisible = false">No</v-btn>
                            <v-btn color="red darken-1" text @click="goBack">Yes</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>

                <!-- <router-link to="/GeneratedItinerary"> -->
                <v-btn color="deep-purple-accent-2" class="white--text mt-6 ml-2" @click="updateTravelInfo"
                    style="min-width: 150px;">
                    Generate
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

    // mounted() {
    //     const state = this.$store.state.stateData;
    //     const city = this.$store.state.city;
    // },

    methods: {
        formatDate(date) {
            const options = { month: 'long', day: 'numeric', year: 'numeric' };
            return new Date(date).toLocaleDateString('en-US', options);
        },
        showConfirmationDialog() {
            this.dialogVisible = true;
        },
        goBack() {
            this.$router.push("/StartPlanning");
        },

        // Function to update the Vuex store with selected activities
        updateSelectedActivities() {
            // console.log('Selected activities:', this.selectedActivities);
            this.$store.commit('updateActivities', this.selectedActivities);
            console.log("Activities stored in Vuex: " + this.$store.state.activities); // Log the activities stored in Vuex
        },
        // Function to update the Vuex store with selected landmarks
        updateSelectedLandmarks() {
            this.$store.commit('updateLandmarks', this.selectedLandmarks);
            console.log("Landmarks stored in Vuex: " + this.$store.state.landmarks); // Log the landmarks stored in Vuex
        },
        // Function to update the Vuex store with selected foods
        updateSelectedFoods() {
            this.$store.commit('updateFoods', this.selectedFoods);
            console.log("Restaurants stored in Vuex: " + this.$store.state.foods); // Log the landmarks stored in Vuex

        },
        // Function to update the Vuex store with selected shops
        updateSelectedShops() {
            this.$store.commit('updateShops', this.selectedShops);
            console.log("Shopping Spots stored in Vuex: " + this.$store.state.shops); // Log the landmarks stored in Vuex
        },
        updateSelectedHotels() {
            this.$store.commit('updateHotels', this.selectedHotels);
            console.log("Hotels stored in Vuex: " + this.$store.state.hotels); // Log the landmarks stored in Vuex
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
            this.isLoading = true;

            // Generate City Summary + Slogan Section
            const requestData = {
                state: this.$store.state.stateData,
                city: this.$store.state.city,
            }
            // console.log(requestData)

            console.log("Generating Description...")
            axios.post('http://localhost:8000/api/generateDescription', requestData)
                .then(response => {
                    // console.log("City Description: ", response.data);
                    this.$store.commit('updateCityDescription', response.data);
                    console.log("City Description: " + response.data)
                    return axios.post('http://localhost:8000/api/generateSlogan', requestData)
                })
                .then(response => {
                    this.$store.commit('updateCitySlogan', response.data);
                    console.log("City Slogan " + response.data)
                })
                .then(response => {
                    this.isLoading = false;
                    this.$router.push({ name: 'GeneratedItinerary' });
                })
        }

    },
    mounted() {
        // Pulls information from the previous page.
        const activityData = JSON.parse(this.$route.query.activityData);
        // console.log(activityData)
        if (activityData && activityData.recommended_places) {
            this.activities = activityData.recommended_places;
        }

        const landmarkData = JSON.parse(this.$route.query.landmarkData);
        // console.log(landmarkData)
        if (landmarkData && landmarkData.recommended_places) {
            this.landmarks = landmarkData.recommended_places;
        }

        const restaurantData = JSON.parse(this.$route.query.restaurantData);
        // console.log(restaurantData)
        if (restaurantData && restaurantData.recommended_places) {
            this.foods = restaurantData.recommended_places;
        }

        const shoppingData = JSON.parse(this.$route.query.shoppingData);
        // console.log(shoppingData)
        if (shoppingData && shoppingData.recommended_places) {
            this.shops = shoppingData.recommended_places;
        }

        const hotelData = JSON.parse(this.$route.query.hotelData);
        // console.log(hotelData)
        if (hotelData && hotelData.recommended_places) {
            this.hotels = hotelData.recommended_places;
        }

        const cityData = JSON.parse(this.$route.query.cityData);
        // console.log(cityData);
        this.cityData = cityData; // Assign cityData to the component's property

        const state = JSON.parse(this.$route.query.stateData);
        // console.log(state);
        this.state = state;

        const budgetData = JSON.parse(this.$route.query.budgetData);
        // console.log(budgetData)
        this.budgetData = budgetData;

        const startDateData = JSON.parse(this.$route.query.startDateData);
        // console.log(startDateData)
        this.startDateData = startDateData;

        const endDateData = JSON.parse(this.$route.query.endDateData);
        // console.log(endDateData)
        this.endDateData = endDateData;


        // this.$store.commit('updateBudget', this.budgetString);
        //     console.log("Budget stored in Vuex: " + this.$store.state.budget); // Log the activities stored in Vuex
    },

    // mutations: {
    //     updateActivities(state, activities) {
    //         console.log('Updating activities in Vuex:', activities);
    //         state.activities = activities;
    //     },
    //     // Other mutations...
    // },

    computed: {
        // selectedActivities() {
        //     return this.$store.state.activities;
        // },
        // selectedBudget() {
        //     const store = useStore();
        //     return store.getters.selectedBudget;
        // },

        // ...mapState({
        //     selectedActivities: state => state.selectedActivities
        // }),

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