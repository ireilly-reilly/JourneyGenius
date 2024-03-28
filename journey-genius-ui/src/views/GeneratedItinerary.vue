<template>
    <v-container>

        <!-- Title and Information Section -->
        <v-row justify="center">
            <v-col cols="12" class="text-center">
                <div style="margin-top: 50px;">
                    <h1 style="font-size: 3.5rem;" class="headline text-deep-purple-accent-2">
                        Welcome to {{ this.$store.state.city }}, {{ this.$store.state.stateData }}!
                    </h1>                    
                    <h2 style="font-size: 2rem;" class="headline text-deep-purple-accent-2">
                        Enter city slogan/motto generated from chat
                    </h2>                    
                    <h1 style="font-size: 1rem;" class="headline text-deep-purple-accent-2">
                        Planned for {{  this.$store.state.datesData }} with a {{ budget }} budget trip.
                    </h1>
                    <br>
                    <p>
                        Enter description generated from Chat
                    </p>
                    <br>
                    <hr>
                </div>
            </v-col>
        </v-row>

        <br>
        <h2 class="section-title text-center">Discover {{ this.$store.state.city }} - Overview</h2>


        <!-- Section with Image and Left Section -->
        <v-row justify="center" align="stretch" style="display: flex; flex-wrap: wrap; align-items: flex-start;">

            <!-- Right Section: Image -->
            <v-col cols="12" md="8" class="image-container align-self-start">
                <v-img src="@/assets/sfbridge2.jpeg" alt="San Francisco" class="fill-height align-self-start"
                    style="object-fit: cover; width: 100%; "></v-img>


            </v-col>
            <!-- Left Section: Activities, Landmarks, Places to Eat, Shopping Spots, Map, Estimated Costs -->
            <v-col cols="12" md="8" class="left-section" style="display: flex; flex-direction: column;">

                <!-- New Section: Activities, Landmarks, Places to Eat, Shopping Spots -->
                <div style="margin-bottom: 30; flex: 1;">

                    <!-- Activities Section -->
                    <div class="section-content">
                        <h3>Activities</h3>
                        <ul>
                            <li v-for="activity in activities" :key="activity">{{ activity }}</li>
                        </ul>
                    </div>

                    <!-- Landmarks Section -->
                    <div class="section-content">
                        <h3>Iconic Landmarks</h3>
                        <ul>
                            <li v-for="landmark in landmarks" :key="landmark">{{ landmark }}</li>
                        </ul>
                    </div>

                    <!-- Places to Eat Section -->
                    <div class="section-content">
                        <h3>Places to Eat</h3>
                        <ul>
                            <li v-for="food in foods" :key="food">{{ food }}</li>
                        </ul>
                    </div>

                    <!-- Shopping Spots Section -->
                    <div class="section-content">
                        <h3>Shopping Spots</h3>
                        <ul>
                            <li v-for="shop in shops" :key="shop">{{ shop }}</li>
                        </ul>
                    </div>
                </div>

            </v-col>

        </v-row>

        <br>
        <br>

        <!-- Underneath Section: Estimated Costs Section -->
        <!-- Combined Section: Map of San Francisco and Estimated Costs -->
        <div style="margin-bottom: 30px;">
            <hr>
            <br>

            <h2 class="section-title" style="text-align: center;">Explore {{ this.$store.state.city }} - Map and Estimated Costs</h2>
            <p style="text-align: center;">
                Explore this interactive map showcasing the locations of your selected points of interest, encompassing
                your
                chosen accommodation, transportation options, planned activities, and other areas of interest!
            </p>
            <br>
            <div style="position: relative; overflow: hidden; border-radius: 8px;">
                <!-- Replace YOUR_GOOGLE_MAPS_EMBED_CODE with the actual embed code from Google Maps -->
                <iframe width="100%" height="300" frameborder="0" style="border: 0; border-radius: 8px;"
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d100940.18159925131!2d-122.52000105328746!3d37.757671315006284!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80859a6d00690021%3A0x4a501367f076adff!2sSan%20Francisco%2C%20CA!5e0!3m2!1sen!2sus!4v1701922231766!5m2!1sen!2sus"
                    allowfullscreen></iframe>
            </div>
            <br>
            <v-row justify="center">
                <v-col cols="12" md="8" class="text-center">
                    <div style="margin-bottom: 30px; max-width: none;">
                        <h2 class="section-title">Estimated Costs (USD)</h2>
                        <div class="section-content">
                            <v-row>
                                <v-col cols="12" md="6">
                                    <v-icon color="deep-purple-accent-2">mdi-bed</v-icon> Accommodation: $100-$200 per
                                    night
                                </v-col>
                                <v-col cols="12" md="6">
                                    <v-icon color="deep-purple-accent-2">mdi-bus</v-icon> Transportation: $20-$50 per
                                    day
                                </v-col>
                                <v-col cols="12" md="6">
                                    <v-icon color="deep-purple-accent-2">mdi-food</v-icon> Food: $20-$40 per meal
                                </v-col>
                                <v-col cols="12" md="6">
                                    <v-icon color="deep-purple-accent-2">mdi-walk</v-icon> Activities: $20-$50 per
                                    activity
                                </v-col>
                            </v-row>
                        </div>
                    </div>
                </v-col>
            </v-row>
        </div>


        <!-- Two buttons on the bottom -->
        <v-row justify="center" class="mt-4">
            <v-col cols="12" md="8" class="text-center">
                <router-link to="/Itinerary">
                    <v-btn color="deep-purple-accent-2" class="white--text mt-6 mr-2" @click="previousStep"
                        style="min-width: 150px;">
                        Customize
                    </v-btn>
                </router-link>

                <router-link to="/GeneratedItinerary2">
                    <v-btn color="deep-purple-accent-2" class="white--text mt-6 ml-2" style="min-width: 150px;">
                        Generate
                    </v-btn>
                </router-link>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    name: 'SanFranciscoPage',


    mounted() {
        // Accessing the variables from the Vuex store
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


        console.log('Activities:', activities);
        console.log('Landmarks:', landmarks);
        console.log('Foods:', foods);
        console.log('Shops:', shops);
        console.log('Hotels:', hotels);
        console.log('Dates:', datesData);
        console.log('Budget:', budget);
        console.log('State:', stateData);
        console.log('City:', city);
        console.log('Latitude:', lat);
        console.log('Longitude:', long);
    },

    computed: {
        activities() {
            return this.$store.state.activities;
        },
        landmarks() {
            return this.$store.state.landmarks;
        },
        foods() {
            return this.$store.state.foods;
        },
        shops() {
            return this.$store.state.shops;
        },
        hotels() {
            return this.$store.state.hotels;
        },
        datesData() {
            return this.$store.state.datesData;
        },
        budget() {
            return this.$store.state.budget;
        },

        
    },



};
</script>

<style scoped>
/* Custom styles for the information and new sections */
.info-container {
    padding: 16px;
    background-color: #fff;
    /* You can customize the background color */
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    /* Optional: Add a subtle box shadow */
    margin-bottom: 16px;
}

.image-container {
    display: flex;
    align-items: flex-start;
    justify-content: center;
    /* Align the image at the top when screen is too small */
    text-align: center;
    /* Center the content horizontally */
}

.section-title {
    font-size: 1.8em;
    margin-bottom: 16px;
}

.section-content {
    margin-bottom: 24px;
}

.section-content h3 {
    font-size: 1.5em;
    margin-bottom: 8px;
}

.section-content ul {
    list-style-type: disc;
    /* Change 'disc' to 'circle' or 'square' if desired */
    padding-left: 20px;
    /* Adjust as needed */
}

.section-content ul li {
    margin-bottom: 4px;
}

/* Custom styles for the Estimated Costs section */
.estimated-costs {
    margin-top: 30px;
    /* Adjust as needed */
}

.estimated-costs h2 {
    font-size: 1.8em;
    margin-bottom: 16px;
}

.estimated-costs .section-content {
    margin-bottom: 16px;
}

.estimated-costs .section-content h3 {
    font-size: 1.5em;
    margin-bottom: 8px;
}
</style>
