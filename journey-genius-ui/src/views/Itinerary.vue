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
                    The activities you select will form your final itinerary. You are required to check at least one box in
                    every category. Once you are content with the activities that have piqued your interest, proceed to the
                    next step. If you desire more options, simply press the more button, and additional choices will become
                    available.
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
                <v-row>
                    <v-col v-for="(activity, index) in activities" :key="index" cols="12">
                        <v-checkbox v-model="selectedActivities[index]" :label="activity" class="mb-1"></v-checkbox>
                    </v-col>
                </v-row>
                <v-col class="d-flex justify-center">
                    <v-btn @click="redirectToMoreActivitiesPage" color="deep-purple-accent-2">See More Activities</v-btn>
                </v-col>
            </v-col>
        </v-row>

        <!-- Category: Iconic Landmarks and Photo Opportunities -->
        <v-row justify="center" class="mt-4">
            <v-col cols="12" md="8">
                <h3 class="headline text-deep-purple-accent-2">Iconic Landmarks and Photo Opportunities</h3>
                <br>
                <v-row>
                    <v-col v-for="(landmark, index) in landmarks" :key="index" cols="12">
                        <v-checkbox v-model="selectedLandmarks[index]" :label="landmark" class="mb-1"></v-checkbox>
                    </v-col>
                </v-row>
                <v-col class="d-flex justify-center">
                    <v-btn @click="redirectToMoreLandmarksPage" color="deep-purple-accent-2">See More Landmarks</v-btn>
                </v-col>
            </v-col>
        </v-row>

        <!-- Category: What do You want to Eat? -->
        <v-row justify="center" class="mt-4">
            <v-col cols="12" md="8">
                <h3 class="headline text-deep-purple-accent-2">What do You want to Eat?</h3>
                <br>
                <v-row>
                    <v-col v-for="(food, index) in foods" :key="index" cols="12">
                        <v-checkbox v-model="selectedFoods[index]" :label="food" class="mb-1"></v-checkbox>
                    </v-col>
                </v-row>
                <v-col class="d-flex justify-center">
                    <v-btn @click="redirectToMoreDiningPage" color="deep-purple-accent-2">See More Dining Options</v-btn>
                </v-col>
            </v-col>
        </v-row>

        <!-- Category: Shopping Spots -->
        <v-row justify="center" class="mt-4">
            <v-col cols="12" md="8">
                <h3 class="headline text-deep-purple-accent-2">Shopping Spots</h3>
                <br>
                <v-row>
                    <v-col v-for="(shop, index) in shops" :key="index" cols="12">
                        <v-checkbox v-model="selectedShops[index]" :label="shop" class="mb-1"></v-checkbox>
                    </v-col>
                </v-row>
                <v-col class="d-flex justify-center">
                    <v-btn @click="redirectToMoreShoppingPage" color="deep-purple-accent-2">See More Retail Stores</v-btn>
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
//import Papa from 'papaparse'; // Import PapaParse for parsing CSV

export default defineComponent({
    data() {
        return {
            activities: ['Biking Across the Golden Gate Bridge: Rent a bike and pedal across the iconic Golden Gate Bridge. Once on the other side, explore the trails in the Marin Headlands for stunning views of the bridge and the city.', 'Land\'s End Trail: Hike the Land\'s End Trail for breathtaking views of the Pacific Ocean, the Golden Gate Bridge, and the Marin Headlands. Don\'t miss the historic Sutro Baths and the labyrinth along the way.', 'Kayaking on the Bay: Rent a kayak and paddle around the San Francisco Bay. You can get unique views of the city skyline and might even spot some sea lions near Pier 39.', 'Sailing on the Bay: Charter a sailboat or join a sailing tour to experience the beauty of San Francisco from the water.'], // Add your activities here
            landmarks: ['Golden Gate Park: This expansive park offers a variety of attractions, including the California Academy of Sciences, the de Young Museum, the Japanese Tea Garden, and the San Francisco Botanical Garden.', 'Fisherman\'s Wharf: Enjoy the lively atmosphere at Fisherman\'s Wharf, where you can indulge in seafood, visit Pier 39 with its sea lions, and explore the Muse Mecanique, a vintage arcade.', 'Alcatraz Island: Take a ferry to Alcatraz and explore the infamous former prison. The audio tour provides a fascinating glimpse into the history of this iconic site.', 'Chinatown: Explore the vibrant and historic Chinatown, known for its unique shops, markets, and delicious restaurants.'], // Add your landmarks here
            foods: [], // Initialize as empty array
            shops: ['Union Square: Known as the city\'s premier shopping destination, Union Square is home to flagship stores of major brands such as Macy\'s,Saks Fifth Avenue,Neiman Marcus,and Apple. You\'ll also find a variety of luxury boutiques and department stores in the surrounding area.', 'Westfield San Francisco Centre (865 Market St): This large shopping mall in the heart of downtown features a mix of high-end and mainstream retailers, including Bloomingdale\'s, Nordstrom, and a variety of other shops.', 'Ghirardelli Square (900 North Point St): While primarily known for its chocolate shops, Ghirardelli Square also houses boutique stores, galleries, and restaurants. It\'s a great place to shop while enjoying views of the bay.', 'Valencia Street (Mission District): Valencia Street in the Mission District is known for its hip and eclectic shops, including vintage stores, bookshops, and unique boutiques.'], // Add your shops here
            selectedActivities: [],
            selectedLandmarks: [],
            selectedFoods: [],
            selectedShops: [],
        };
    },
    methods: {
        redirectToMoreActivitiesPage() {
            this.$store.commit('updateSelectedActivities', this.selectedActivities);
            this.$router.push('/MoreActivitiesPage');
        },
        redirectToMoreLandmarksPage() {
            this.$store.commit('updateSelectedLandmarks', this.selectedLandmarks);
            this.$router.push('/MoreLandmarksPage');
        },
        redirectToMoreDiningPage() {
            this.$store.commit('updateSelectedFoods', this.selectedFoods);
            this.$router.push('/MoreDiningPage');
        },
        redirectToMoreShoppingPage() {
            this.$store.commit('updateSelectedShops', this.selectedShops);
            this.$router.push('/MoreShoppingPage');
        },
        loadFoodsFromCSV(priceRange) {
            this.foods = recommendedRestaurants;
        },
    },
    computed: {
        selectedBudget() {
            const store = useStore();
            return store.getters.selectedBudget;
        },
    },
    watch: {
        selectedBudget(newValue) {
            this.loadFoodsFromCSV(newValue);
        },
    },
});
</script>

<style></style>