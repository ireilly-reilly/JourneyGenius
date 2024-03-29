<template>
    <v-app>
        <v-container>
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
                                class="mb-1"></v-checkbox>
                        </v-col>

                    </v-row>
                    <v-col class="d-flex justify-center">
                        <!-- <v-btn @click="redirectToMoreActivitiesPage" color="deep-purple-accent-2">See More Activities</v-btn> -->
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
                                class="mb-1"></v-checkbox>
                        </v-col>
                    </v-row>
                    <v-col class="d-flex justify-center">
                        <!-- <v-btn @click="redirectToMoreLandmarksPage" color="deep-purple-accent-2">See More Landmarks</v-btn> -->
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
                                :label="Array.isArray(food) ? food.join(', ') : food" class="mb-1"></v-checkbox>
                        </v-col>
                    </v-row>
                    <v-col class="d-flex justify-center">
                        <!-- <v-btn @click="redirectToMoreDiningPage" color="deep-purple-accent-2">See More Dining Options</v-btn> -->
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
                                :label="Array.isArray(shop) ? shop.join(', ') : shop" class="mb-1"></v-checkbox>
                        </v-col>
                    </v-row>
                    <v-col class="d-flex justify-center">
                        <!-- <v-btn @click="redirectToMoreShoppingPage" color="deep-purple-accent-2">See More Retail Stores</v-btn> -->
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
                                :label="Array.isArray(hotel) ? hotel.join(', ') : hotel" class="mb-1"></v-checkbox>
                        </v-col>
                    </v-row>
                    <v-col class="d-flex justify-center">
                        <!-- <v-btn @click="redirectToMoreShoppingPage" color="deep-purple-accent-2">See More Retail Stores</v-btn> -->
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

                <router-link to="/GeneratedItinerary">
                    <v-btn color="deep-purple-accent-2" class="white--text mt-6 ml-2" style="min-width: 150px;">
                        Generate
                    </v-btn>
                </router-link>
            </v-col>
        </v-row>
    </v-app>
</template>

<script>
import { defineComponent } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import { mapState, mapMutations } from 'vuex';




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






        // Testing
        console.log("Before - City stored in Vuex: " + this.$store.state.city); // Log the city stored in Vuex
        console.log("Before - State stored in Vuex: " + this.$store.state.state); // Log the state stored in Vuex
        console.log("Before - Dates stored in Vuex: " + this.$store.state.dates); // Log the dates stored in Vuex
        console.log("Before - Budget stored in Vuex: " + this.$store.state.budget); // Log the budget stored in Vuex
        console.log("Before - Activities stored in Vuex: " + this.$store.state.activities); // Log the activities stored in Vuex
        console.log("Before - Landmarks stored in Vuex: " + this.$store.state.landmarks); // Log the landmarks stored in Vuex
        console.log("Before - Shopping stored in Vuex: " + this.$store.state.shops); // Log the shopping spots stored in Vuex
        console.log("Before - Dining stored in Vuex: " + this.$store.state.foods); // Log the dining options stored in Vuex
        console.log("Before - Hotels stored in Vuex: " + this.$store.state.hotels); // Log the dining options stored in Vuex
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
                return "cheap";
            } else if (this.budgetData === 2) {
                return "medium";
            } else if (this.budgetData === 3) {
                return "expensive";
            } else {
                return "Unknown";
            }
        },
        combinedDates() {
            if (this.startDateData && this.endDateData) {
                const startDateFormat = this.formatDate(this.startDateData);
                const endDateFormat = this.formatDate(this.endDateData);
                return `${startDateFormat} - ${endDateFormat}`;
            }
            return '';
        },
        fullName() {
            return this.stateMap[this.state] || this.state;
        },

    },

});
</script>

<style></style>