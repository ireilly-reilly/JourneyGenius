<template>
    <v-container>
        <!-- Header -->
        <v-row justify="center" class="mt-4">
            <v-col cols="12" md="8" class="text-center">
                <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">
                    Plan Your Next Adventure
                </h2>
                <p style="font-size: 0.75rem;" class="headline text-deep-purple-accent-2">
                    Planned for February 13 - February 15. High budget, traveling with friends.
                </p>
                <p style="margin-top: 10px;">
                    The activities you select will form your final itinerary. You are required to check at least one box
                    in
                    every category. Once you are content with the activities that have piqued your interest, proceed to
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
                <h3 class="headline text-deep-purple-accent-2">Choose the Activities that Peak Your Interest</h3>
                <br>
                <v-row dense>
                    <v-col v-for="(activity, index) in activities" :key="index" cols="12">
                        <v-checkbox v-model="selectedActivities" :value="activity"
                            :label="Array.isArray(activity) ? activity.join(', ') : activity" class="mb-1"></v-checkbox>
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
                <h3 class="headline text-deep-purple-accent-2">Iconic Landmarks and Photo Opportunities</h3>
                <br>
                <v-row dense>
                    <v-col v-for="(landmark, index) in landmarks" :key="index" cols="12">
                        <v-checkbox v-model="selectedLandmarks" :value="landmark"
                            :label="Array.isArray(landmark) ? landmark.join(', ') : landmark" class="mb-1"></v-checkbox>
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
                <h3 class="headline text-deep-purple-accent-2">What do You want to Eat?</h3>
                <br>
                <v-row dense>
                    <v-col v-for="(food, index) in foods" :key="index" cols="12">
                        <v-checkbox v-model="selectedFoods" :value="food"
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
                <h3 class="headline text-deep-purple-accent-2">Shopping Spots</h3>
                <br>
                <v-row dense>
                    <v-col v-for="(shop, index) in shops" :key="index" cols="12">
                        <v-checkbox v-model="selectedShops" :value="shop"
                            :label="Array.isArray(shop) ? shop.join(', ') : shop" class="mb-1"></v-checkbox>
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

            <router-link to="/StartPlanning">
                <v-btn color="deep-purple-accent-2" class="white--text mt-6 mr-2" @click="previousStep"
                    style="min-width: 150px;">
                    Previous Step
                </v-btn>
            </router-link>

            <router-link to="/Itinerary2">
                <v-btn color="deep-purple-accent-2" class="white--text mt-6 ml-2" style="min-width: 150px;">
                    Next Step
                </v-btn>
            </router-link>
        </v-col>
    </v-row>
</template>

<script>
import { defineComponent } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';

export default defineComponent({
    data() {
        return {

            activities: [],
            landmarks: [],
            foods: [],
            shops: [],
            selectedActivities: [],
            selectedLandmarks: [],
            selectedFoods: [],
            selectedShops: [],
        };
    },
    methods: {

    },
    mounted() {
        // const restaurantData = JSON.parse(this.$route.query.restaurantData);
        // if (restaurantData && restaurantData.recommended_places) {
        //     this.foods = restaurantData.recommended_places;
        // }

        // Parse the JSON strings into objects
        // Check if the query parameters are defined before parsing
        //const restaurantData = this.$route.query.restaurantData ? JSON.parse(this.$route.query.restaurantData) : null;
        // const activityData = this.$route.query.activityData ? JSON.parse(this.$route.query.activityData) : null;
        // const landmarkData = this.$route.query.landmarkData ? JSON.parse(this.$route.query.landmarkData) : null;
        // const shoppingData = this.$route.query.shoppingData ? JSON.parse(this.$route.query.shoppingData) : null;

        // Now you can use these variables in your component
        //this.foods = restaurantData;
        // this.activities = activityData;
        // this.landmarks = landmarkData;
        // this.shops = shoppingData;
        // console.log(restaurantData);
        // console.log(landmarkData);
        // console.log(shoppingData);


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

    },

    computed: {
        selectedBudget() {
            const store = useStore();
            return store.getters.selectedBudget;
        },
    },

});
</script>

<style></style>