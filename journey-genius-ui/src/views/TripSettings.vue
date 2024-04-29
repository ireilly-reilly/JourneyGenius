<template>
    <v-dialog v-model="preferencesNotSet" max-width="650">
            <v-card>
                <v-card-title class="headline"
                    style="padding-left: 25px; padding-top: 15px;">Trip Preferences Not Set!</v-card-title>
                <v-card-text>
                    To plan a trip, we need to get to know you! Go to the Trip Preferences page to select some preferences for your trips.
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="deep-purple-accent-2" text @click="preferencesNotSet = false">Close</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    <v-container>
        <!-- Header -->
        <v-row justify="center" class="mt-4">
            <v-col cols="12" md="8" class="text-center">
                <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">Trip Settings</h2>
                <p>Configure number of options and details available for your trip. </p>
                <br>
                <hr>
            </v-col>
        </v-row>

        <!-- Number of Selections -->
        <v-row justify="center">
            <v-col cols="12" md="8">
                <v-card class="pa-4 mb-4">
                    <h2 class="headline text-deep-purple-accent-2">How many options?</h2>
                    <p>Choose how many options to generate. The number you select represents how many activities,
                        landmarks, restaurants, shopping options, and hotels will be available for you to choose. More options will result in a longer wait time. Adjust
                        the slider below: </p>
                    <br>
                    <v-slider v-model="sliderValue" :min="5" :max="15" :step="1" :thumb-label="true"
                        class="deep-purple-accent-2" color="deep-purple-accent-2"></v-slider>
                </v-card>
            </v-col>
        </v-row>

        <!-- Description Generation Toggle -->
        <v-row justify="center">
            <v-col cols="12" md="8">
                <v-card class="pa-4 mb-4">
                    <h2 class="headline text-deep-purple-accent-2">Description Generation Toggle</h2>
                    <p>Enable this to use OpenAI to generate descriptions for your selected options. Please note that
                        these descriptions are crafted to provide a broad overview rather than detailed specifics, so you have a better idea of what to expect. Enabling this will increase wait time.</p>
                    <v-row align="center" justify="center" class="my-3 align-center">
                        <v-col cols="12" class="d-flex justify-center"> <!-- Using d-flex on v-col directly -->
                                <v-switch v-model="descriptionToggle" color="deep-purple-accent-2" class="centered-text"
                                    :label="`Generate Descriptions: ${descriptionToggle ? 'On' : 'Off'}`"
                                    large></v-switch>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>



        <!-- Estimated Loading Time -->
        <v-row justify="center">
            <v-col cols="12" md="8">
                <v-card class="pa-4 mb-4 justify-center">
                    <!-- Header aligned to the left -->
                    <h2 class="headline text-deep-purple-accent-2" style="text-align: left;">Estimated Loading Time</h2>
                    <p>Calculate expected loading time based on current settings.</p>
                    <br>
                    <!-- Centralized button and output message layout -->
                    <v-row justify="center" align="center" no-gutters>
                        <v-col cols="12" class="text-center">
                            <v-btn size="large" color="deep-purple-accent-2" @click="estimateTime">
                                <v-icon left>mdi-timer</v-icon>
                                Generate Estimated Wait Time
                            </v-btn>
                            <!-- Display the estimated time message if it exists -->
                            <div v-if="estimatedTimeMessage" class="mt-3">
                                <h4 style="color: #7C4DFF">{{ estimatedTimeMessage }}</h4>
                            </div>
                        </v-col>
                    </v-row>
                    <br>
                </v-card>
            </v-col>
        </v-row>




        <!-- Generate button -->
        <v-row justify="center">
            <v-col cols="12" md="8" class="text-center">
                <br>
                <v-btn size="large" class="generate-btn" color="deep-purple-accent-2" @click="checkPreferencesFlag">
                    Start Planning
                </v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>

import Cookies from 'js-cookie'
import axios from 'axios'
export default {
    data() {
        return {
            sliderValue: 5, // Default slider value set to the mid-point
            descriptionToggle: false,
            estimatedTimeMessage: '', // Initially empty
            selections: '',

            preferences_flag: true,
            existingUserData: {},
            preferencesNotSet: false,

        };
    },
    mounted(){
        this.fetchUserProfiling();
    },
    methods: {
        estimateTime() {
            // Placeholder function for estimating time based on user selections
            this.estimatedTimeMessage = 'Estimated wait time is approximately 3 minutes.';
        },
        startPlanning() {
            this.$store.commit('updateSelectionAmount', this.sliderValue);
            this.$store.commit('updateDescriptionToggle', this.descriptionToggle);
            
            console.log(this.$store.state.sliderValue);             
            console.log(this.$store.state.descriptionToggle);

            this.$router.push({ name: 'StartPlanning' });

        },
        async fetchUserProfiling(){
            const jwtToken = Cookies.get('login_token');
            try {

                const response = await axios.get('http://localhost:8000/api/user_profiling/fetch_user_preferences', {
                headers: {
                    Authorization: `Bearer ${jwtToken}` // Include the JWT token in the Authorization header
                }
                });
                this.existingUserData = response.data;
                // const { activities, foods, shopping, accommodation } = response.data;
                const activities = response.data.activities;
                const foods = response.data.foods;
                const shopping = response.data.shopping;
                if (!activities || activities.length === 0 ||
                !foods || foods.length === 0 ||
                !shopping || shopping.length === 0) {
                    this.preferences_flag = false;
                }
                console.log("Preferences flag: ", this.preferences_flag);

             // if (response.data.activities = [])

            }
            catch (error) {
                console.error('Error fetching user preferences:', error);
            }
        },
        checkPreferencesFlag(){
            if (this.preferences_flag === false){
                this.preferencesNotSet = true;
            } else{
                this.startPlanning();
            }
        },
    },
};
</script>
