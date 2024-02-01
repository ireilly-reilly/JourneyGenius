<template>
  <div class="home">
    <v-container fluid class="no-border">
      <!-- Top Section -->
      <v-row align="center" justify="center" class="my-3 ">
        <v-col cols="12" md="10" lg="8" class="text-center">
          <!-- <v-card class="pa-5"> -->
          <h2 class="display-1 font-weight-black">

          </h2>
          <h2 class="display-1 font-weight-black">
            Vacation Itineraries with
          </h2>
          <h2 class="display-1 font-weight-black mb-2">
            <span class="text-deep-purple-accent-2">Journey Genius</span>
          </h2>
          <!-- Additional smaller text -->
          <h3 class="subtitle-1 text-grey-darken-2">
            This application serves as your dedicated travel curator, crafting distinctive itineraries
          </h3>
          <h3 class="subtitle-1 text-grey-darken-2">
            tailored to your interests and budget.
          </h3>

          <!-- "Start Now" -->
          <router-link to='/StartPlanning'>
            <v-btn rounded="lg" size="large" color="deep-purple-accent-2" class="white--text mt-6">
              Start Planning
            </v-btn>
          </router-link>
          <!-- </v-card> -->
          <br>
          <br>
        </v-col>
      </v-row>


      <!-- What Makes Our Application Special -->
      <v-row justify="center" class="my-5">
        <v-col cols="12">
          <h2 class="headline font-weight-black text-center">
            What Makes Our Application Special
          </h2>
        </v-col>

        <v-row justify="center" class="my-5" style="display: flex; flex-wrap: wrap;">
          <v-col v-for="(feature, index) in specialFeatures" :key="index" cols="12" md="3">
            <v-card class="pa-2" elevation="10" style="flex: 1;">
              <!-- Center-align the icon and text -->
              <div class="d-flex flex-column align-center">
                <v-icon class="display-1 mb-2 ">{{ feature.icon }}</v-icon>
                <h3 class="subtitle-1 text-center">{{ feature.title }}</h3>
              </div>
              <p class="body-1 text-center description-height2">{{ feature.description }}</p>
            </v-card>
          </v-col>
        </v-row>
      </v-row>

      <!-- Featured Destinations -->
      <v-row justify="center" class="my-5">
        <v-col cols="12">
          <h2 class="headline font-weight-black text-center">
            Featured Destinations
          </h2>
        </v-col>

        <!-- Featured Destinations -->
        <v-row justify="center" class="my-5" style="display: flex; flex-wrap: wrap;">
          <v-col v-for="(destination, index) in featuredDestinations" :key="index" cols="12" md="4" lg="3" xl="3">
            <v-card class="pa-3" elevation="10" style="flex: 1;">
              <!-- Replace the placeholder content with your destination information -->
              <h3 class="subtitle-1 text-center mt-2">{{ destination.name }}</h3>
              <p class="body-1 text-center description-height">{{ destination.description }}</p>
              <v-responsive aspect-ratio="16/9">
                <v-img :src="destination.image" alt="Destination Image" style="border-radius: 5px;"></v-img>
              </v-responsive>
            </v-card>
          </v-col>
        </v-row>


      </v-row>

      <!-- The Most Optimal Way to Travel Section -->
      <v-row align="start" justify="start" class="mt-5 ">
        <!-- gradient-background -->
        <v-col cols="12">
          <h1 class="headline font-weight-black text-center">
            The Most Optimal Way to Travel
          </h1>
          <v-row justify="center" class="mt-5">

            <!-- Optimal Route Planning -->
            <v-col cols="12" md="3">
              <v-card class="pa-3" elevation="10" style="flex: 1;">
                <div class="d-flex flex-column align-center">
                  <v-icon class="display-1 mb-2">mdi-directions</v-icon>
                  <h3 class="subtitle-1 text-center">Optimal Route Planning</h3>
                  <p class="body-1 text-center description-height3">
                    Our AI algorithms analyze your preferences to craft the most efficient route, saving you time and
                    effort.
                  </p>
                </div>
              </v-card>
            </v-col>

            <!-- Personalize Your Adventure -->
            <v-col cols="12" md="6" lg="3">
              <v-card class="pa-3" elevation="10" style="flex: 1;">
                <div class="d-flex flex-column align-center">
                  <v-icon class="display-1 mb-2">mdi-pencil</v-icon>
                  <h3 class="subtitle-1 text-center">Personalize Your Adventure</h3>
                  <p class="body-1 text-center description-height3">
                    Shape your journey by freely adding, editing, or deleting activities from your itinerary.
                  </p>
                </div>
              </v-card>
            </v-col>

            <!-- Local Cuisine Recommendations -->
            <v-col cols="12" md="6" lg="3">
              <v-card class="pa-3" elevation="10" style="flex: 1;">
                <div class="d-flex flex-column align-center">
                  <v-icon class="display-1 mb-2">mdi-food</v-icon>
                  <h3 class="subtitle-1 text-center">Local Cuisine</h3>
                  <p class="body-1 text-center description-height3">
                    Discover local cuisines and hidden gems recommended by our AI, tailored to your taste buds.
                  </p>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>

    </v-container>




  </div>
</template>

<script>
import { defineComponent } from 'vue';


export default defineComponent({
  data() {
    return {
      featuredDestinations: [
        {
          name: 'New York, New York',
          image: require('@/assets/nyc.jpeg'),
          description: 'Vibrant city, renowned for iconic landmarks, diverse neighborhoods, cultural attractions, and nightlife scene.'
        },
        {
          name: 'Seattle, Washington',
          image: require('@/assets/seattle.jpeg'),
          description: 'Seattle, the Emerald City, offers a blend of tech innovation, stunning natural beauty, coffee culture, and arts scene.'
        },
        {
          name: 'Honolulu, Hawaii',
          image: require('@/assets/hawaii.jpeg'),
          description: 'Honolulu, the capital of Hawaii, is a tropical paradise known for its beaches, cultural heritage, and Pacific cuisine.'
        },


        // Add more featured destinations as needed
      ],
      specialFeatures: [
        { icon: 'mdi-star', title: 'Tailored Itineraries', description: 'Crafting unique travel plans based on your interests and preferences.' },
        { icon: 'mdi-clock-time-three-outline', title: 'Time Efficiency', description: 'Save time with automated itinerary generation and smart suggestions.' },
        { icon: 'mdi-wallet-outline', title: 'Budget-Friendly', description: 'Travel planning that fits your budget without compromising on experiences.' },
        // Add more features as needed
      ],
    }
  }
});
</script>


<style scoped>
/* Adjust the font size to make it larger */
.display-1 {
  font-size: 4rem;
  /* You can adjust this value as needed */
}

/* Add styles for the additional smaller text */
.subtitle-2 {
  font-size: 1.5rem;
  /* Adjust the font size as needed */
  color: #757575;
  /* Use a lighter color of black, adjust as needed */
}

/* Additional styles for the new grid section */
.headline {
  font-size: 3rem;
  font-weight: bold;
  color: #333;
  /* Adjust the color as needed */
}

.body-1 {
  font-size: 1rem;
  color: #555;
  /* Adjust the color as needed */
}

.gradient-background {
  background: linear-gradient(to right, #673AB7, #2196F3);
  /* Your gradient colors */
  color: white;
  /* Set text color to contrast with the background */
}

.custom-card {
  max-width: 1500px;
  /* Adjust the value as needed */
  margin: 0 auto;
  /* Center the card within the container */
}

.description-height {
  height: 100px;
  /* Set a fixed height for the descriptions */
  overflow: hidden;
  /* Hide overflow content if the description is longer */
  display: -webkit-box;
  -webkit-line-clamp: 3;
  /* Limit the number of lines to show */
  -webkit-box-orient: vertical;
}

.description-height2 {
  height: 70px;
  /* Set a fixed height for the descriptions */
  overflow: hidden;
  /* Hide overflow content if the description is longer */
  display: -webkit-box;
  -webkit-line-clamp: 3;
  /* Limit the number of lines to show */
  -webkit-box-orient: vertical;
}

.description-height3 {
  height: 80px;
  /* Set a fixed height for the descriptions */
  overflow: hidden;
  /* Hide overflow content if the description is longer */
  display: -webkit-box;
  -webkit-line-clamp: 3;
  /* Limit the number of lines to show */
  -webkit-box-orient: vertical;
}</style>
