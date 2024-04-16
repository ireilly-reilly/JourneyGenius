<!-- <template>

  <v-container>

    <div class="text-center">
          <v-snackbar v-model="showSnackbar" color="deep-purple-accent-2" top>
            <span class="centered-text">Successfully Deleted.</span>
          </v-snackbar>
        </div>

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

    
      


    <v-row justify="center" v-if="savedTrips && savedTrips.length > 0">
      <v-col cols="12" md="8" v-for="(trip, index) in savedTrips" :key="index">
        <v-hover v-slot="{ isHovering, props }">
          <v-card class="pa-4 mb-4" v-bind="props">
            <v-img :src="imageSrc" :alt="trip.location" class="mb-3"
              style="width: 100%; border-top-left-radius: 8px; border-top-right-radius: 8px;"></v-img>

            <v-row align="center" class="mb-1">
              <v-col cols="12">
                <v-row justify="space-between" align="center">
                  <v-col cols="12">
                    <h2 class="headline mb-1 text-deep-purple-accent-2">{{ trip.city }}, {{ trip.state }}</h2>
                    <h4 class="headline mb-0.5 black">{{ trip.dates }}</h4>
                  </v-col>
                  <v-col cols="12" class="text-right">
                  </v-col>
                </v-row>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" class="pr-4">
                <p class="mb-2">{{ trip.city_description }}</p>
              </v-col>
            </v-row>


            <v-overlay :model-value="isHovering" class="align-center justify-center" scrim="deep-purple-accent-2"
              contained>
              <v-row justify="center">
                <v-btn size="large" color="white" class="mr-4" @click="getSavedTripDetails(index)">
                  Open Itinerary <v-icon class="ml-1" right>mdi-map-marker</v-icon>
                </v-btn>
                <v-btn size="large" color="white" @click="showConfirmationDialog">
                  Delete Trip <v-icon class="ml-1" right>mdi-delete</v-icon>
                </v-btn>
              </v-row>
            </v-overlay>


            <v-dialog v-model="dialogVisible" max-width="650">
              <v-card>
                <v-card-title class="headline"
                  style="padding-left: 25px; padding-top: 15px;">Confirmation</v-card-title>
                <v-card-text>
                  Are you sure you want to delete this trip? This action cannot be undone.
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="deep-purple-accent-2" text @click="dialogVisible = false">No</v-btn>
                  <v-btn color="red darken-1" text @click="confirmDelete(index)">Yes</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card>
        </v-hover>
      </v-col>
    </v-row>



    <v-row justify="center" v-else>
      <v-col cols="12" md="8" class="text-center">
        <p class="headline text-deep-purple-accent-2" style="font-size: 1.5rem;">You have no trips saved, let's plan
          one!</p>
      </v-col>
    </v-row>

  </v-container>
</template> -->


<!-- Grid system - Future implemenetation. Don't delete this commented out code. -->
<!-- <v-row justify="center" v-if="savedTrips && savedTrips.length > 0">
        <v-col cols="6" md="4" v-for="(trip, index) in savedTrips" :key="index">
          <v-hover v-slot="{ isHovering, props }">

          <v-card class="pa-4 mb-4" @mouseover="isHovering = index" @mouseleave="isHovering = null">

            <v-img :src="imageSrc" :alt="trip.location" class="mb-3" style="width: 100%; border-radius: 8px;"></v-img>

            <v-row align="center" class="mb-1">
              <v-col cols="12">
                <h2 class="headline mb-2 text-deep-purple-accent-2">{{ trip.city }}, {{ trip.state }}</h2>
                <h4 class="headline mb-0.5 black">{{ trip.dates }}</h4>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" class="pr-4">
                <p class="mb-2">{{ trip.city_description }}</p>
              </v-col>
            </v-row>

             <v-overlay :value="isHovering === index" class="align-center justify-center" scrim="deep-purple-accent-2" contain>
              contain>
              <v-row justify="center">
                <v-btn size="large" color="white" class="mr-4" @click="openItinerary(index)">
                  Open Itinerary <v-icon class="ml-1" right>mdi-map-marker</v-icon>
                </v-btn>
                <v-btn size="large" color="white" @click="confirmDelete(index)">
                  Delete Trip <v-icon class="ml-1" right>mdi-delete</v-icon>
                </v-btn>
              </v-row>
            </v-overlay>
          </v-card>
          </v-hover>
        </v-col>
      </v-row> -->

<template>
  <v-container>

    <div class="text-center">
      <v-snackbar v-model="showSnackbar" color="deep-purple-accent-2" top>
        <span class="centered-text">Successfully Deleted.</span>
      </v-snackbar>
    </div>



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

    <v-row justify="center" v-if="savedTrips && savedTrips.length > 0">
      <v-col cols="12" md="8">
        <v-select v-model="sortKey" :items="sortOptions" label="Sort by" @change="sortTrips" outlined dense return-object></v-select>

       
          <!-- <v-select label="Sort by"
          :items="['Recently Added', 'Date', 'State', 'City', 'Budget']" @change="sortTrips"></v-select> -->
      </v-col>
    </v-row>

    <!-- Grid style Saved Trips Cards -->
    <v-row justify="center" v-if="savedTrips && savedTrips.length > 0">
      <v-col cols="12" md="8">
        <v-row class="equal-height-cards">
          <v-col cols="12" md="6" v-for="(trip, index) in savedTrips" :key="index">
            <v-hover v-slot="{ isHovering, props }">
              <v-card class="pa-4 mb-4 d-flex flex-column" v-bind="props">
                <v-img :src="imageSrc" :alt="trip.location" class="mb-3"
                  style="width: 100%; border-top-left-radius: 8px; border-top-right-radius: 8px;"></v-img>

                <v-row align="center" class="mb-1">
                  <v-col cols="12">
                    <v-row justify="space-between" align="center">
                      <v-col cols="12">
                        <h2 class="headline mb-1 text-deep-purple-accent-2">{{ trip.city }}, {{ trip.state }}</h2>
                        <h4 class="headline mb-0.5 black">{{ trip.dates }}</h4>
                      </v-col>
                    </v-row>
                  </v-col>
                </v-row>

                <!-- make this section the same height -->
                <v-row class="flex-grow-1">
                  <v-col cols="12" class="pr-4">
                    <p class="mb-2" style="flex: 1; overflow: hidden;">{{ trip.city_description }}</p>
                  </v-col>
                </v-row>

                <v-overlay :model-value="isHovering" class="align-center justify-center" scrim="deep-purple-accent-2"
                  contained>
                  <v-row justify="center">
                    <v-btn size="large" color="white" class="mr-4" @click="getSavedTripDetails(index)">
                      Open Itinerary <v-icon class="ml-1" right>mdi-map-marker</v-icon>
                    </v-btn>
                    <v-btn size="large" color="white" @click="showConfirmationDialog">
                      Delete Trip <v-icon class="ml-1" right>mdi-delete</v-icon>
                    </v-btn>
                  </v-row>
                </v-overlay>

                <v-dialog v-model="dialogVisible" max-width="650">
                  <v-card>
                    <v-card-title class="headline"
                      style="padding-left: 25px; padding-top: 15px;">Confirmation</v-card-title>
                    <v-card-text>
                      Are you sure you want to delete this trip? This action cannot be undone.
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="deep-purple-accent-2" text @click="dialogVisible = false">No</v-btn>
                      <v-btn color="red darken-1" text @click="confirmDelete(index)">Yes</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>

              </v-card>
            </v-hover>
          </v-col>
        </v-row>
      </v-col>
    </v-row>



    <!-- Message for no saved trips -->
    <v-row justify="center" v-else>
      <v-col cols="12" md="8" class="text-center">
        <p class="headline text-deep-purple-accent-2" style="font-size: 1.5rem;">You have no trips saved, let's plan
          one!</p>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';
export default {
  data() {
    console.log(this.sortOptions); // Check if sortOptions are correctly populated

    return {
      savedTrips: [],
      imageSrc: require('@/assets/sf.jpeg'), //This will need to be changed to actual image 
      showSnackbar: false,
      dialogVisible: false,
      sortKey: '',

      sortOptions: [
        { name: 'Recently Added', value: '' },
        { name: 'Dates', value: "tripDate" },
        { name: 'State Name', value: "tripState" },
        { name: 'City Name', value: "tripCity" },
        { name: 'Budget', value: "tripBudget" }
      ],

    };
    defineProps({
      originPage: String
    })
  },
  mounted() {
    this.fetchSavedTrips();
    // console.log('Sort Options:', this.sortOptions); // Check if sortOptions are populated correctly

  },
  methods: {
    sortTrips() {
      console.log("the text field was selected"); 

      if (!this.sortKey) return; // Do nothing if sortKey is not selected

      console.log('Sorting by:', this.sortKey); // Debug: Check which key is used for sorting

      const isDescending = (key) => ['recent', 'budget'].includes(key); // Add keys that should sort descending

      this.savedTrips.sort((a, b) => {
        let valA, valB;
        switch (this.sortKey) {
          case 'recent':
            valA = new Date(a.addedDate);
            valB = new Date(b.addedDate);
            break;
          case 'dates':
            valA = new Date(a.dates.start);
            valB = new Date(b.dates.start);
            break;
          case 'state':
          case 'city':
            valA = a[this.sortKey].toLowerCase(); // assuming city and state are stored as strings
            valB = b[this.sortKey].toLowerCase();
            break;
          case 'budget':
            valA = parseFloat(a.budget); // assuming budget is stored as a string or number
            valB = parseFloat(b.budget);
            break;
          default:
            return 0;
        }

        console.log(`Comparing ${valA} to ${valB}`); // Debug: Check values being compared

        if (isDescending(this.sortKey)) {
          return valB - valA; // For descending order
        }
        return valA - valB; // For ascending order
      });

      // To trigger Vue's reactivity system after sorting
      this.savedTrips = [...this.savedTrips];
    },

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
      // const isConfirmed = window.confirm('Are you sure you want to delete this trip?');

      // if (isConfirmed) {

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
            this.showSnackbar = true;
            const deletedIndex = this.savedTrips.findIndex(trip => trip.id === trip_id);
            if (deletedIndex !== -1) {
              this.savedTrips.splice(deletedIndex, 1);
            }
            this.dialogVisible = false;

          } else {
            throw new Error('Failed to delete trip');
          }
        })
        .catch(error => {
          console.error('Error deleting trip:', error);
          alert('Failed to delete trip. Please try again.');
        });
      // }
    },
    showConfirmationDialog() {
      this.dialogVisible = true;
    },
    getSavedTripDetails(index) {
      const jwtToken = Cookies.get('login_token');
      const tripId = this.savedTrips[index].id; // Assuming each trip object has an 'id' property
      console.log("token: " + jwtToken)
      console.log("tripId: " + tripId)


      axios.get(`http://localhost:8000/api/fetch_saved_itinerary/${tripId}`, {
        headers: {
          Authorization: `Bearer ${jwtToken}` // Include the JWT token in the Authorization header
        }
      })
        .then(response => {
          if (response.status === 200) {
            const savedTripDetails = response.data.savedTrip;
            console.log('Saved trip details:', savedTripDetails);

            this.$store.commit('updateTripObject', savedTripDetails);
            this.$router.push("SavedItinerary");

            // Route to the SavedItinerary page and pass savedTripDetails as a route parameter
            // this.$router.push({
            //   name: 'SavedItinerary',
            //   params: { savedTrip: savedTripDetails }
            // });
          } else {
            throw new Error('Failed to fetch saved trip details');
          }
        })
        .catch(error => {
          console.error('Error fetching saved trip details:', error);
          alert('Failed to fetch saved trip details. Please try again.');
        }
        );

      // const tripId = this.savedTrips[index].id; // Assuming each trip object has an 'id' property
      // console.log("tripId: " + tripId);
      // this.$store.commit('updateTripId', tripId);
      // this.$router.push("SavedItinerary");
    }




  },
};
</script>

<style scoped>
.centered-text {
  display: block;
  text-align: center;
  font-size: medium;
}

.equal-height-cards {
  display: flex;
  flex-wrap: wrap;
}

.description-row {
  display: flex;
  flex-wrap: wrap;
}

.description-col {
  display: flex;
  flex-direction: column;
}

.description-content {
  flex: 1;
  /* Makes the content expand to fill the available space */
}
</style>
