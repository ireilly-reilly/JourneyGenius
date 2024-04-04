<template>
    <v-container>


        <!-- Title and Information Section -->
        <v-row justify="center">
            <v-col cols="12" class="text-center">
                <div style="margin-top: 50px;">
                    <h1 style="font-size: 3.5rem;" class="headline text-deep-purple-accent-2">
                        Welcome to {{ this.$store.state.city }}, {{ this.$store.state.stateData }}!
                    </h1>
                    <h2 style="font-size: 2.25rem;" class="headline text-deep-purple-accent-2">
                        {{ this.$store.state.citySlogan }}
                    </h2>
                    <h1 style="font-size: 1rem;" class="headline text-deep-purple-accent-2">
                        Planned for {{ this.$store.state.datesData }} with a {{ budget }} budget trip.
                    </h1>
                    <br>
                    <p style="font-size: 1.125rem">
                        {{ this.$store.state.cityDescription }}
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

            <h2 class="section-title" style="text-align: center;">Explore {{ this.$store.state.city }} - Map</h2>
            <p style="text-align: center;">
                Explore this interactive map showcasing the locations of your selected points of interest, encompassing
                your
                chosen accommodation, transportation options, planned activities, and other areas of interest!
            </p>
            <br>
            <div style="position: relative; overflow: hidden; border-radius: 8px;">
                <iframe width="100%" height="300" frameborder="0" style="border: 0; border-radius: 8px;" :src="'https://www.google.com/maps/embed/v1/view?key=AIzaSyDGC5QtIMrpN1HXPJpamkDhgfVUkq9Jw8Y&center=' +
                            this.$store.state.lat + ',' + this.$store.state.long + '&zoom=15&maptype=roadmap'"
                    allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe>
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

                <!-- Render different buttons based on the origin page -->
                <router-link v-if="originPage === 'SavedTrips'" to="/SavedTrips">
                    <v-btn color="deep-purple-accent-2" class="white--text mt-6 mr-2" style="min-width: 150px;">
                        Close
                    </v-btn>
                </router-link>
                <router-link v-else to="/GeneratedItinerary2">
                    <v-btn color="deep-purple-accent-2" class="white--text mt-6 ml-2" style="min-width: 150px;">
                        Generate
                    </v-btn>
                </router-link>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from 'axios';
export default {
    mounted() {
        const tripObject = this.$store.state.tripObject;
        console.log("This is the saved object: " + tripObject)
        console.log(tripObject.id)
        console.log(tripObject.city)
        console.log(tripObject.city_Description)



        // axios.get(`http://localhost:8000/api/fetch_saved_itinerary/${tripId}`, {
        //     // headers: {
        //     //   Authorization: `Bearer ${jwtToken}` // Include the JWT token in the Authorization header
        //     // }
        // })
        //     .then(response => {
        //         if (response.status === 200) {
        //             this.savedTripDetails = response.data.savedTrip;
        //             console.log('Saved trip details:', this.savedTripDetails);
        //         } else {
        //             throw new Error('Failed to fetch saved trip details');
        //         }
        //     })
        //     .catch(error => {
        //         console.error('Error fetching saved trip details:', error);
        //         // alert('Failed to fetch saved trip details. Please try again.');
        //     });
    },

    data() {
        return {
            tripId: null,
            savedTripDetails: null,

        };
    },


    computed: {

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
