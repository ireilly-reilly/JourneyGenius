<template>
  <v-container>
    <!-- Header -->
    <v-row justify="center" class="mt-4">
      <v-col cols="12" md="8" class="text-center">
        <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">Plan Your Next Adventure</h2>
        <p>Our app transforms vacation planning by creating personalized itineraries based on user preferences. Users
          input their budget, location, stay duration, and interests. Using advanced algorithms, the app scans diverse
          travel data to find budget-friendly accommodations, local attractions, and outdoor activities, optimizing the
          itinerary for a cost-effective trip.</p>
        <br>
        <hr>
      </v-col>
    </v-row>

    <!-- Section for storing where they want to travel -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4 mb-4">
          <h3 class="headline text-deep-purple-accent-2">Where do you want to travel?</h3>
          <br>

          <!-- This was working -->
          <v-autocomplete v-model="city" :items="autocompleteCities" label="Type a City" @input="onInputChange">
          </v-autocomplete>

        </v-card>
      </v-col>
    </v-row>

    <!-- Date input components -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4 mb-4">
          <h3 class="headline text-deep-purple-accent-2">How Long Is Your Trip?</h3>
          <br>
          <v-row>
            <!-- Start Date -->
            <v-col cols="6">
              <v-text-field v-model="startDate" label="Start Date" type="date" @input="updateStartDate"></v-text-field>
            </v-col>

            <!-- End Date -->
            <v-col cols="6">
              <v-text-field v-model="endDate" label="End Date" type="date" @input="updateEndDate"></v-text-field>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>


    <!-- Budget selection -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4">
          <h3 class="headline text-deep-purple-accent-2">How Much Have You Allocated for Your Expenses?</h3>
          <p>The budget is specifically designated for activities and dining experiences.</p>
          <br>
          <v-row justify="center">
            <v-col v-for="budget in budgets" :key="budget.value" class="mb-2">
              <v-btn class="budget-btn" stacked="" :color="budget.selected ? 'deep-purple' : 'deep-purple-accent-2'"
                @click="selectBudget(budget)">
                <v-icon v-if="budget.value === 'cheap'">mdi-cash-remove</v-icon>
                <v-icon v-if="budget.value === 'medium'">mdi-cash</v-icon>
                <v-icon v-if="budget.value === 'expensive'">mdi-cash-multiple</v-icon>
                <div>{{ budget.label }}</div>
                <div class="caption text--secondary">{{ budget.range }}</div>
              </v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>


    <!-- Travel Companions selection -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4">
          <h3 class="headline text-deep-purple-accent-2">Who Are Your Travel Companions?</h3>
          <v-row justify="center">
            <v-col v-for="companion in travelCompanions" :key="companion.value" cols="4">
              <v-btn class="companion-btn" :color="companion.selected ? 'deep-purple' : 'deep-purple-accent-2'" stacked
                @click="selectTravelCompanion(companion)">
                <v-icon v-if="companion.value === 'solo'">mdi-account</v-icon>
                <v-icon v-if="companion.value === 'group'">mdi-account-group-outline</v-icon>
                <v-icon v-if="companion.value === 'couple'">mdi-heart</v-icon>
                <div>{{ companion.label }}</div>
              </v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>


    <!-- Generate button -->
    <v-row justify="center">
      <v-col cols="12" md="8" class="text-center">
        <br>
        <v-btn class="generate-btn" color="deep-purple-accent-2" @click="generateItinerary">
          Generate
        </v-btn>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>

import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
  data() {
    return {
      // Data for handling city input and autocomplete
      city: '',
      allCities: ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Seattle'],
      menu: false,
      startDate: '', // Initialize with an empty string or a default date
      endDate: '',

      // Data for budget selection
      budgets: [
        { label: 'Cheap', value: 'cheap', range: '0 - 1000 USD', selected: false, priceRange: ['1'] },
        { label: 'Medium', value: 'medium', range: '1000 - 2500 USD', selected: false, priceRange: ['2'] },
        { label: 'Expensive', value: 'expensive', range: '2500+ USD', selected: false, priceRange: ['3'] },
      ],


      // Data for travel companion selection
      travelCompanions: [
        { label: 'Solo', value: 'solo', selected: false },
        { label: 'Group', value: 'group', selected: false },
        { label: 'Couple', value: 'couple', selected: false },
      ],

      // Other data properties
      selectedDate: null,
      isDatePickerVisible: false,
      travelDestination: null,
      selectedBudget: null,

      // Validation rule for end date
      endDateRule: [
        (v) => !!v || 'End date is required',
        (v) => this.isEndDateValid(v) || 'End date must be equal or after the start date',
      ],
    };
  },
  computed: {
    // Computed property for autocomplete suggestions based on user input
    autocompleteCities() {
      if (this.city == null) {
        return this.allCities;
      }

      const lowerCaseInput = this.city.toLowerCase();
      return this.allCities.filter(city => city.toLowerCase().includes(lowerCaseInput));
    },
  },
  methods: {
    // Method for handling input change in the city text field
    onInputChange() {
      this.menu = !!this.city; // Show menu only when there is input
    },
    // Method for selecting a city from the autocomplete suggestions
    selectCity(selectedCity) {
      this.city = selectedCity;
      this.menu = false;
    },

    // Method for displaying the date picker
    showDatePicker() {
      this.isDatePickerVisible = true;
    },
    // Method for hiding the date picker
    hideDatePicker() {
      this.isDatePickerVisible = false;
    },
    // Method for selecting a budget
    selectBudget(selectedBudget) {
      this.$store.commit('setSelectedBudget', selectedBudget);
      this.budgets.forEach((budget) => {
        budget.selected = budget === selectedBudget;
      });
    },
    // Method for selecting a travel companion
    selectTravelCompanion(selectedCompanion) {
      this.travelCompanions.forEach((companion) => {
        companion.selected = companion === selectedCompanion;
      });
    },
    // Method for generating an itinerary or navigating to another view page
    generateItinerary() {
      // Prepare data to send to the backend
      const requestData = {
        target_place: 'Reno',
        // latitude: this.latitude, // Assume you have a way to get the latitude from the user input
        // longitude: this.longitude, // Assume you have a way to get the longitude from the user input
        target_lat_str: '39.5296',
        target_lon_str: '-119.8138',
        desired_price_range_str: '2'
        // desired_price_range: this.selectedBudget.priceRange, // Assuming selectedBudget has a priceRange property
      };

      // Send a POST request to the Flask backend
      axios.post('http://localhost:8000/api/run_ML_model_recommendations', requestData)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });

    },
    // Method to check if the end date is valid
    isEndDateValid(selectedEndDate) {
      return !this.startDate || selectedEndDate >= this.startDate;
    },
  },
});

</script>


<style>
.companion-btn {
  width: 100%;
  margin-top: 8px;
}

.budget-btn {
  width: 100%;
  margin-top: 8px;
}
</style>