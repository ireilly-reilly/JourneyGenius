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
<v-row justify="center">
  <v-col cols="12" md="8" v-for="(trip, index) in savedTrips" :key="index">
    <v-card class="pa-4 mb-4">
      <!-- Title and Delete Button Section -->
      <v-row align="center" class="mb-1">
        <v-col cols="12">
          <v-row justify="space-between" align="center">
            <v-col cols="8">
              <h2 class="headline mb-2">{{ trip.location }}</h2>
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
        <!-- Description and Activities Section -->
        <v-col cols="12" md="6" class="pr-4">
          <p class="mb-2">{{ trip.description }}</p>
          <h3 class="subtitle-1 mb-2">Activities:</h3>
          <ul class="pl-2"> <!-- Added margin-left to the activities list -->
            <li v-for="activity in trip.activities" :key="activity">{{ activity }}</li>
          </ul>
        </v-col>

        <!-- Image and Open Itinerary Button Section -->
        <v-col cols="12" md="6">
          <v-row align="center" justify="center">
            <v-img
              :src="trip.imageSrc"
              :alt="trip.location"
              class="mb-3"
              style="width: 100%; border-radius: 8px;"
            ></v-img>
            <router-link to='/GeneratedItinerary'>
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
</v-container>


</template>

<script>
export default {
  data() {
    return {
      savedTrips: [
        {
          location: 'San Francisco, California',
          description: `San Francisco is a vibrant city known for its iconic landmarks, diverse culture, and stunning views. Explore the Golden Gate Bridge, visit Alcatraz Island, and stroll through Fisherman's Wharf for a taste of the city's rich history and delicious seafood.`,
          activities: ['Golden Gate Bridge Sightseeing', 'Alcatraz Island Tour', 'Fisherman\'s Wharf Exploration', 'Vibrant Asian Culture in Chinatown'],
          imageSrc: require('@/assets/sf.jpeg'),
        },
        // Add more saved trips as needed
      ],
    };
  },
  methods: {
    openItinerary() {
      // Implement logic to open the itinerary for this saved trip
      console.log('Opening Itinerary...');
    },
    confirmDelete(index) {
      const isConfirmed = window.confirm('Are you sure you want to delete this trip?');

      if (isConfirmed) {
        // Implement logic to delete the saved trip
        this.savedTrips.splice(index, 1); // Remove the trip at the specified index
      }
    },
  },
};
</script>

<style scoped>
/* Add custom styles if needed */
</style>




