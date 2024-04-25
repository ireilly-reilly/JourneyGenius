<template>
    <v-container>
      <!-- Header -->
      <v-row justify="center" class="mt-4">
        <v-col cols="12" md="8" class="text-center">
          <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">Trip Settings</h2>
          <p>Configure your trip preferences below. Adjust the settings to tailor the trip generation process to your needs, optimizing the experience for your convenience and satisfaction.</p>
          <br>
          <hr>
        </v-col>
      </v-row>
  
      <!-- Number of Selections -->
      <v-row justify="center">
        <v-col cols="12" md="8">
          <v-card class="pa-4 mb-4">
            <h3 class="headline text-deep-purple-accent-2">How many selections?</h3>
            <p>Choose how many options to generate. A lower number means quicker generation times. <br> 5 = Shortest, 10 = Medium, 15 = Slowest.</p>
            <v-range-slider
              v-model="sliderValue"
              :min="5"
              :max="15"
              :thumb-label="true"
              class="deep-purple-accent-2"
              color="deep-purple-accent-2"
            ></v-range-slider>
          </v-card>
        </v-col>
      </v-row>
  
      <!-- Description Generation Toggle -->
      <v-row justify="center">
        <v-col cols="12" md="8">
          <v-card class="pa-4 mb-4">
            <h3 class="headline text-deep-purple-accent-2">Description Generation Toggle</h3>
            <p>Enable this to use OpenAI to generate descriptions for the selected options.</p>
            <v-switch
              v-model="descriptionToggle"
              color="deep-purple-accent-2"
              :label="`Generate Descriptions: ${descriptionToggle ? 'On' : 'Off'}`"
            ></v-switch>
          </v-card>
        </v-col>
      </v-row>
  
      <!-- Estimated Loading Time -->
      <v-row justify="center">
        <v-col cols="12" md="8" class="text-center">
          <v-card class="pa-4">
            <h3 class="headline text-deep-purple-accent-2">Estimated Loading Time</h3>
            <v-btn
              color="deep-purple-accent-2"
              @click="estimateTime"
              large
            >
              <v-icon left>mdi-timer</v-icon>
              Generate Estimated Wait Time
            </v-btn>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        sliderValue: [5, 15],
        descriptionToggle: false,
      };
    },
    methods: {
      estimateTime() {
        // Placeholder function for estimating time based on user selections
        console.log('Estimating time...');
      },
    },
  };
  </script>
  
  <style scoped>
  .headline {
    font-size: 2.5rem;
  }
  
  .pa-4 {
    padding: 16px; /* Same as 4 * 4px in Vuetify's scale */
  }
  
  .mb-4 {
    margin-bottom: 16px;
  }
  </style>
  