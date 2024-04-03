<template>
  <v-container>
    <!-- Saved Trips Introduction -->
    <v-row justify="center" class="mt-4">
      <v-col cols="12" md="8" class="text-center">
        <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">Saved Trips</h2>
        <p>
          Explore and manage your saved adventures effortlessly on our "Saved Trips" page. Easily access
          and review your curated itineraries, and if inspiration strikes or plans change, customize them
          to suit your preferences. This hub is your go-to destination for comprehensive details about
          your planned journeys, allowing you to delve into more information and make adjustments seamlessly.
          Your personalized travel experiences are just a click away on the Saved Trips page.
        </p>
        <br>
        <hr>
      </v-col>
    </v-row>

    <!-- Saved Trip Cards -->
    <v-row justify="center" v-if="savedTrips && savedTrips.length > 0">
      <v-col cols="12" md="8" v-for="(trip, index) in savedTrips" :key="index">
        <v-card class="pa-4 mb-4">
          <!-- Title and Delete Button Section -->
          <v-row align="center" class="mb-1">
            <v-col cols="12">
              <v-row justify="space-between" align="center">
                <v-col cols="8">
                  <h2 class="headline mb-1 text-deep-purple-accent-2">{{ trip.city }}, {{ trip.state }} </h2>
                  <h4 class="headline mb-0.5 black">{{ trip.dates }}</h4>
                </v-col>
                <v-col cols="4" class="text-right">
                  <v-btn icon @click="confirmDelete(index)">
                    <v-icon>mdi-delete</v-icon>
                  </v-btn>
                </v-col>
              </v-row>
            </v-col>
          </v-row>

          <!-- Main Content Section -->
          <v-row>
            <!-- Trip Dates -->
          <v-row align="center" class="mb-1">
            <v-col cols="12">
              <!-- <p class="subtitle-2 text-deep-purple-accent-2 mb-2">Trip Dates: {{ trip.dates }}</p> -->
            </v-col>
          </v-row>
            <!-- Description and Activities Section -->
            <v-col cols="12" md="6" class="pr-4">
              <p class="mb-2">{{ trip.city_description }}</p>
              <h3 class="subtitle-1 mb-2">Activities:</h3>
              <ul class="pl-2">
                <li v-for="activity in trip.activities" :key="activity">{{ activity }}</li>
              </ul>
            </v-col>

            <!-- Image and Open Itinerary Button Section (NEED TO CHANGE IMAGE SOURCE TO BE DYNAMIC) -->
            <v-col cols="12" md="6">
            <v-row align="center" justify="center">
              <v-img
                :src="imageSrc" 
                :alt="trip.location"
                class="mb-3"
                style="width: 100%; border-radius: 8px;"
              ></v-img>
              <router-link :to="{ name: 'GeneratedItinerary', params: { originPage: 'SavedTrips' } }">
                <v-btn color="deep-purple-accent-2" class="mt-3" @click="openItinerary">
                  Open Itinerary
                </v-btn>
            </router-link>
          </v-row>
        </v-col>
      </v-row>
    </v-card>
  </v-col>
</v-row>


    <!-- Message for no saved trips -->
    <v-row justify="center" v-else>
      <v-col cols="12" md="8" class="text-center">
        <p class="headline text-deep-purple-accent-2" style="font-size: 1.5rem;">You have no trips saved, let's plan one!</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';
export default {
  data() {
    return {
      savedTrips: [],
      imageSrc: require('@/assets/sf.jpeg'), //This will need to be changed to actual image 
    };
    defineProps({
        originPage: String
    })
  },
  mounted() {
    this.fetchSavedTrips();
  },
  methods: {
    fetchSavedTrips() {
      const jwtToken = Cookies.get('login_token');
      const url = 'http://localhost:8000/api/fetch_saved_trips'
      axios.get(url, {
        headers: {
            Authorization: `Bearer ${jwtToken}` // Include the JWT token in the Authorization header
        }
        })
        .then(response => {
          this.savedTrips = response.data.savedTrips;
        })
        .catch(error => {
          console.error('Error fetching saved trips:', error);
        });
    },
    confirmDelete(index) {
      const isConfirmed = window.confirm('Are you sure you want to delete this trip?');

      if (isConfirmed) {
        const jwtToken = Cookies.get('login_token');
        const trip_id = this.savedTrips[index].id; // Assuming each trip object has an 'id' property
        axios.delete(`http://localhost:8000/api/delete_trip/${trip_id}`, {
        headers: {
            Authorization: `Bearer ${jwtToken}` // Include the JWT token in the Authorization header
        }
        })
          .then(response => {
            if (response.status === 200) {
              // Remove the deleted trip from the savedTrips array
              const deletedIndex = this.savedTrips.findIndex(trip => trip.id === trip_id);
              if (deletedIndex !== -1) {
                this.savedTrips.splice(deletedIndex, 1);
              }
            } else {
              throw new Error('Failed to delete trip');
            }
          })
          .catch(error => {
            console.error('Error deleting trip:', error);
            alert('Failed to delete trip. Please try again.');
          });
      }
    },
  },
};
</script>

<style scoped>
/* Add custom styles if needed */
</style>
