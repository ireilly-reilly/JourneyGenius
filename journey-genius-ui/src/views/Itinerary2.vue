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
                <br />
                <hr />
            </v-col>
        </v-row>

        <!-- Flight Lookup Section -->
        <v-row justify="center" class="mt-4">
            <v-col cols="12" md="8" class="text-center">
                <h3 class="headline text-deep-purple-accent-2">
                    <v-icon color="deep-purple-accent-2">mdi-airplane-takeoff</v-icon>
                    Flight Lookup
                </h3>
                <br>
                <v-form @submit.prevent="lookupFlights">
                    <v-row align="center">
                        <v-col cols="12" md="6">
                            <v-text-field v-model="departureCity" label="Departure City" outlined dense></v-text-field>
                        </v-col>
                        <v-col cols="12" md="6">
                            <!-- Set destinationCity to 'SFO' -->
                            <v-text-field v-model="destinationCity" label="Destination City" outlined dense
                                readonly></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row align="center">
                        <v-col>
                            <v-btn type="submit" color="deep-purple-accent-2">
                                <v-icon left>mdi-magnify</v-icon>
                                {{ isLoading ? 'Searching...' : 'Lookup Flights' }}
                            </v-btn>
                        </v-col>
                    </v-row>

                    <!-- Show error message if there's an issue -->
                    <v-row v-if="errorMessage" align="center">
                        <v-col>
                            <v-alert type="error" color="deep-purple-accent-2">{{ errorMessage }}</v-alert>
                        </v-col>
                    </v-row>

                    <v-row>
                        <v-col>
                            <v-checkbox v-model="handleFlightIndependently"
                                label="I will be handling my flight arrangements independently and won't be utilizing Journey Genius."></v-checkbox>
                        </v-col>
                    </v-row>

                </v-form>
            </v-col>
        </v-row>



        <!-- Housing Options Section -->
        <v-row justify="center" class="mt-4">
            <v-col cols="12" md="8">
                <h3 class="headline text-deep-purple-accent-2">Housing Options</h3>
                <br>
                <v-radio-group v-model="selectedHousingOption">
                    <v-row>
                        <v-col v-for="(option, index) in housingOptions" :key="index" cols="12">
                            <v-radio :label="option.name" :value="option.name" class="mb-1"></v-radio>
                            <v-img :src="option.photo" alt="Housing Option" width="100%" class="mb-2"></v-img>
                        </v-col>
                    </v-row>
                </v-radio-group>
            </v-col>
        </v-row>


        <!-- Transportation Options Section -->
        <v-row justify="center" class="mt-4">
            <v-col cols="12" md="8">
                <h3 class="headline text-deep-purple-accent-2">Transportation Options</h3>
                <br>
                <v-radio-group v-model="selectedTransportationOption">
                    <v-row>
                        <v-col v-for="(option, index) in transportationOptions" :key="index" cols="12">
                            <v-radio :label="option.name" :value="option.name" class="mb-1"></v-radio>
                            <v-img :src="option.photo" alt="Transportation Option" width="100%" class="mb-2"></v-img>
                        </v-col>
                    </v-row>
                </v-radio-group>
            </v-col>
        </v-row>


        <!-- Two buttons on the bottom -->
        <v-row justify="center" class="mt-4">
            <v-col cols="12" md="8" class="text-center">
                <hr />

                <router-link to="/Itinerary">
                    <v-btn color="deep-purple-accent-2" class="white--text mt-6 mr-2" @click="previousStep"
                        style="min-width: 150px;">
                        Previous Step
                    </v-btn>
                </router-link>

                <router-link to="/GeneratedItinerary">
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
    data() {
        return {
            departureCity: '',
            destinationCity: 'SFO',
            flightResults: [],
            apiKey: '3311fb347e8b9eb0da3b5d4b57d2baad',
            apiUrl: 'http://api.aviationstack.com/v1/flights',
            handleFlightIndependently: false,
            isLoading: false,
            errorMessage: '',

            housingOptions: [],

            selectedHousingOption: null,
            handleAccommodationIndependently: false,
            selectedHousingOptions: [],

            transportationOptions: [
                { name: 'Rental Car', photo: 'path/to/rental-car-photo.jpg' },
                { name: 'Taxi', photo: 'path/to/taxi-photo.jpg' },
                { name: 'Public Transit', photo: 'path/to/public-transit-photo.jpg' },
                // Add more transportation options as needed
            ],
            selectedTransportationOption: null,
        };
    },
    methods: {
        lookupFlights() {
            this.isLoading = true;
            this.errorMessage = ''; // Reset error message

            const { departureCity, destinationCity, handleFlightIndependently, apiKey, apiUrl } = this;

            // Make a request to the AviationStack API
            axios.get(apiUrl, {
                params: {
                    access_key: apiKey,
                    departure_iata: departureCity,
                    arrival_iata: destinationCity,
                },
            })
                .then(response => {
                    this.isLoading = false;

                    // Handle the flight data
                    this.flightResults = response.data.data;
                })
                .catch(error => {
                    this.isLoading = false;
                    console.error('Error fetching flight data:', error);

                    // Set an error message for the user
                    this.errorMessage = 'Error fetching flight data. Please try again.';
                });
        },
    },
};
</script>

<style scoped>/* Add your custom styles here */</style>