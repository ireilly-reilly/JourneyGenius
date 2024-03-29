<template>
  <v-container>
    <!-- Loading screen overlay -->
    <LoadingScreen v-if="isLoading" />

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
          <vue-google-autocomplete id="map2" ref="toAddress" classname="form-control" placeholder="Enter a City"
            v-on:placechanged="getAddressData" types="(cities)" country="us"
            style="width: 100%; max-width: 5000px; height: 50px; background-color: #f5f5f5; padding-left: 15px;">
          </vue-google-autocomplete> <!-- Drop down for cities -->
          <div v-if="showCityError" class="error-message3">{{ cityErrorMessage }}</div>
          <!-- <br>
          <br> -->
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
            <v-col cols="12" sm="6">
              <v-text-field v-model="formattedStartDate" label="Start Date" @click="isStartDatePickerVisible = true"
                readonly hide-details ref="startDate"></v-text-field>
              <v-date-picker v-model="startDate" @input="isStartDatePickerVisible = false" :max="endDate"
                v-if="isStartDatePickerVisible" no-title hide-details color="deep-purple-accent-2" scrollable
                hide-header="" style="width: 1000px; max-width: 100%;"></v-date-picker>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field v-model="formattedEndDate" label="End Date" @click="isEndDatePickerVisible = true" readonly
                hide-details ref="endDate"></v-text-field>
              <v-date-picker v-model="endDate" @input="isEndDatePickerVisible = false" :min="startDate"
                v-if="isEndDatePickerVisible" color="deep-purple-accent-2" scrollable hide-header=""
                style="width: 1000px; max-width: 100%;"></v-date-picker>
            </v-col>
            <div v-if="showDateError" class="error-message">{{ datesErrorMessage }}</div>
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
          <div v-if="showBudgetError" class="error-message2">{{ budgetErrorMessage }}</div>

        </v-card>
      </v-col>
    </v-row>

    <!-- Generate button -->
    <v-row justify="center">
      <v-col cols="12" md="8" class="text-center">
        <br>
        <!-- <router-link to="/Itinerary"> -->
        <v-btn class="generate-btn" color="deep-purple-accent-2" @click="generateItinerary">
          Generate
        </v-btn>
        <!-- </router-link> -->
      </v-col>
    </v-row>

  </v-container>
</template>

<script>

import { defineComponent } from 'vue';
import axios from 'axios';
import VueGoogleAutocomplete from "vue-google-autocomplete";
import LoadingScreen from '@/components/LoadingScreen.vue';



export default defineComponent({
  data() {
    return {
      // Data for handling city input and autocomplete
      city: '',
      autocompleteCities: [],
      state: '',

      startDate: null,
      endDate: null,
      isStartDatePickerVisible: false,
      isEndDatePickerVisible: false,

      selectedPlace: null,
      selectedLat: null,
      selectedLon: null,
      selectededBudget: null,

      // Variables used after the generation process
      isLoading: false,
      restaurantData: [],
      activityData: [],
      landmarkData: [],
      shoppingData: [],
      hotelData: [],
      cityData: [],
      budgetData: [],
      startDateData: [],
      endDateData: [],

      isPlaceValid: false,
      isStartDateValid: false,
      isEndDateValid: false,
      isBudgetValid: false,

      // loginErrorMessage: ,
      datesErrorMessage: "",
      showDateError: false,
      budgetErrorMessage: "",
      showBudgetError: false,
      cityErrorMessage: "",
      showCityError: false,

      // Data for budget selection
      budgets: [
        { label: 'Cheap', value: 'cheap', range: '0 - 1000 USD', selected: false, priceRange: ['1'] },
        { label: 'Medium', value: 'medium', range: '1000 - 2500 USD', selected: false, priceRange: ['2'] },
        { label: 'Expensive', value: 'expensive', range: '2500+ USD', selected: false, priceRange: ['3'] },
      ],

      // Other data properties
      isDatePickerVisible: false,
      // travelDestination: null,
      selectedBudget: null,

      // Validation rule for end date
      endDateRule: [
        (v) => !!v || 'End date is required',
        (v) => this.isEndDateValid(v) || 'End date must be equal or after the start date',
      ],

    };
  },
  watch: {
    startDate() {
      if (this.endDate && this.startDate > this.endDate) {
        this.endDate = null;
      }
    },
    endDate() {
      if (this.startDate && this.startDate > this.endDate) {
        this.startDate = null;
      }
    },
  },

  components: {
    VueGoogleAutocomplete,
    LoadingScreen,
  },

  computed: {
    formattedStartDate() {
      return this.startDate ? this.formatDate(this.startDate) : '';
    },
    formattedEndDate() {
      return this.endDate ? this.formatDate(this.endDate) : '';
    },
  },

  methods: {
    // Google Places API Dropdown
    getAddressData: function (addressData) {
      this.city = addressData.locality || addressData.latitude || addressData.longitude || '';
      this.state = addressData.administrative_area_level_1 || ''; // Store state information
      this.selectedPlace = {
        name: this.city,
        state: this.state,
        latitude: addressData.latitude,
        longitude: addressData.longitude,
      };
      console.log('Selected Place:', this.selectedPlace);
      this.selectedLat = addressData.latitude; // Store latitude
      this.selectedLon = addressData.longitude; // Store longitude
    },

    // Method for displaying the date picker
    showDatePicker() {
      this.isDatePickerVisible = true;
    },
    // Method for hiding the date picker
    hideDatePicker() {
      this.isDatePickerVisible = false;
    },

    // Method to check if the end date is valid
    isEndDateValid(selectedEndDate) {
      return !this.startDate || selectedEndDate >= this.startDate;
    },

    formatDate(date) {
      // Custom date formatting logic
      // return `${date.getMonth() + 1}-${date.getDate()}-${date.getFullYear()}`;

      const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
      return date.toLocaleDateString(undefined, options);
    },

    // Method for selecting a budget
    selectBudget(selectedBudget) {
      // Set the selected budget to the corresponding value
      if (selectedBudget.value === 'cheap') {
        this.selectedBudget = 1;
      } else if (selectedBudget.value === 'medium') {
        this.selectedBudget = 2;
      } else if (selectedBudget.value === 'expensive') {
        this.selectedBudget = 3;
      }

      // Update the selected state for each budget
      this.budgets.forEach((budget) => {
        budget.selected = budget === selectedBudget;
      });
    },


    // Method for generating an itinerary or navigating to another view page
    generateItinerary() {
      let isValid = true; // Assume input is valid unless proven otherwise

      if (!this.startDate || !this.endDate) {
        this.datesErrorMessage = "Both the start date and end date are required.";
        this.showDateError = true;
        isValid = false;
      } else {
        this.showDateError = false;
      }

      if (this.selectedBudget !== 1 && this.selectedBudget !== 2 && this.selectedBudget !== 3) {
        this.budgetErrorMessage = "The budget for your trip is required.";
        this.showBudgetError = true;
        isValid = false;
      } else {
        this.showBudgetError = false;
      }

      if (!this.selectedPlace || (!this.selectedPlace && (!this.selectedLat || !this.selectedLon))) {
        this.cityErrorMessage = 'Please select a valid city.';
        this.showCityError = true;
        isValid = false;
      } else {
        this.showCityError = false; 
      }

      if (!isValid) {
        return; // Exit the method if input is not valid
      }

      // Show loading screen overlay
      this.isLoading = true;

      const requestData = {
        target_lat_str: this.selectedLat,
        target_lon_str: this.selectedLon,
        desired_price_range_str: this.selectedBudget
      };

      axios.post('http://localhost:8000/api/scrape_restaurants', requestData)
        .then(response => {
          console.log('scrape_restaurants response:', response.data);
          return axios.post('http://localhost:8000/api/scrape_activities', requestData);
        })
        .then(response => {
          console.log('scrape_activities response', response.data);
          return axios.post('http://localhost:8000/api/scrape_landmarks', requestData);
        })
        .then(response => {
          console.log('scape_landmarks response', response.data);
          return axios.post('http://localhost:8000/api/scrape_shopping', requestData);
        })
        .then(response => {
          console.log('scrape_shopping response', response.data);
          return axios.post('http://localhost:8000/api/scrape_hotels', requestData);
        })
        .then(response => {
          console.log('scrape_hotels response', response.data);
          return axios.post('http://localhost:8000/api/run_ML_model_restaurant_recommendations', requestData);
        })
        .then(response => {
          this.restaurantData = response.data;
          console.log('run_ML_model_recommendations restaurant response:', response.data);
          return axios.post('http://localhost:8000/api/run_ML_model_activity_recommendations', requestData);
        })
        .then(response => {
          this.activityData = response.data;
          console.log('run_ML_model_recommendations activities response:', response.data);
          return axios.post('http://localhost:8000/api/run_ML_model_landmark_recommendations', requestData);
        })
        .then(response => {
          this.landmarkData = response.data;
          console.log('run_ML_model_recommendations landmarks response:', response.data);
          return axios.post('http://localhost:8000/api/run_ML_model_shopping_recommendations', requestData);
        })
        .then(response => {
          this.shoppingData = response.data;
          console.log('run_ML_model_recommendations shopping response:', response.data);
          return axios.post('http://localhost:8000/api/run_ML_model_hotel_recommendations', requestData)
        })
        .then(response => {
          this.hotelData = response.data;
          console.log('run_ML_model_recommendations hotels response:', response.data);
        })

        .then(() => {
          this.isLoading = false;
          this.$router.push({
            name: 'Itinerary',
            query: {
              restaurantData: JSON.stringify(this.restaurantData),
              activityData: JSON.stringify(this.activityData),
              landmarkData: JSON.stringify(this.landmarkData),
              shoppingData: JSON.stringify(this.shoppingData),
              hotelData: JSON.stringify(this.hotelData),
              cityData: JSON.stringify(this.selectedPlace.name),
              budgetData: JSON.stringify(this.selectedBudget),
              startDateData: JSON.stringify(this.formattedStartDate),
              endDateData: JSON.stringify(this.formattedEndDate),
              stateData: JSON.stringify(this.state),
            }
          });
        })
        .catch(error => {
          // Hide loading screen overlay on error
          this.isLoading = false;
          console.error(error);
        });
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

.v-date-picker-header {
  display: none
}

.error-message {
  color: red;
  margin-top: 5px;
  padding-left: 12px;
  margin-bottom: 10px;
}

.error-message2 {
  color: red;
  margin-top: 10px;
  margin-left: 1px;

}

.error-message3 {
  color: red;
  margin-top: 15px;
  margin-left: 1px;
}

.error-outline {
  border-color: red;
}
</style>