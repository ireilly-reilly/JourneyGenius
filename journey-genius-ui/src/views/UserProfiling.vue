<template>
  <v-container>
    <template>
      <div class="text-center">
        <!-- Other template markup -->
        <v-snackbar v-model="showSnackbar" color="deep-purple-accent-2" top>
          <span class="centered-text">Preferences Saved Successfully!</span>
        </v-snackbar>
      </div>
    </template>
    <!-- Your Header -->
    <v-row justify="center" class="mt-4">
      <v-col cols="12" md="8" class="text-center">
        <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">Your Interests</h2>
        <p>Select your interests so we can curate your trip. 
        </p>
        <br>
        <hr>
      </v-col>
    </v-row>

    <!-- Activities selection -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4">
          <h3 class="headline text-deep-purple-accent-2">Select Favorite Activities</h3>
          <p>Choose your favorite activities to customize your experience!</p>

          <v-row justify="center">
            <v-col v-for="activity in activities" :key="activity.value" cols="4">
              <v-btn class="activities-btn" stacked=""
                :color="activity.selected ? 'deep-purple' : 'deep-purple-accent-2'" @click="toggleActivity(activity)">
                <v-icon v-if="activity.value === 'amusement_park'">mdi-popcorn</v-icon>
                <v-icon v-if="activity.value === 'museum'">mdi-bank</v-icon>
                <v-icon v-if="activity.value === 'art_gallery'">mdi-palette</v-icon>
                <v-icon v-if="activity.value === 'zoo'">mdi-dog</v-icon>
                <v-icon v-if="activity.value === 'aquarium'">mdi-fish</v-icon>
                <v-icon v-if="activity.value === 'stadium'">mdi-football</v-icon>
                <v-icon v-if="activity.value === 'casino'">mdi-cards-playing-outline</v-icon>
                <v-icon v-if="activity.value === 'night_club'">mdi-dance-pole</v-icon>


                <div>{{ activity.label }}</div>
              </v-btn>
              <br>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>


    <!-- Ethnic Foods selection -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4">
          <h3 class="headline text-deep-purple-accent-2">Select Ethnic Foods</h3>
          <p>Select your favorite types of cuisine and we'll cater to your tastes!</p>

          <v-row justify="center">
            <v-col v-for="food in ethnicFoods" :key="food.value" cols="4">
              <v-btn class="food-btn" stacked="" :color="food.selected ? 'deep-purple' : 'deep-purple-accent-2'"
                @click="toggleFood(food)">
                <v-icon v-if="food.value === 'american'">mdi-hamburger</v-icon>
                <v-icon v-if="food.value === 'mexican'">mdi-taco</v-icon>
                <v-icon v-if="food.value === 'european_mediterranean'">mdi-pasta</v-icon> 
                <v-icon v-if="food.value === 'east_asian'">mdi-noodles</v-icon> 
                <v-icon v-if="food.value === 'south_asian'">mdi-tea</v-icon>
                <v-icon v-if="food.value === 'east_asian_2'">mdi-rice</v-icon>
                <v-icon v-if="food.value === 'bar'">mdi-glass-cocktail</v-icon>
                <v-icon v-if="food.value === 'specialty'">mdi-chef-hat</v-icon> 
                <v-icon v-if="food.value === 'dietary_focused'">mdi-carrot</v-icon> 
                <div>{{ food.label }}</div>
              </v-btn>
              <br>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>

    <!-- Shopping selection -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-4">
          <h3 class="headline text-deep-purple-accent-2">Select Favorite Shopping Options</h3>
          <p>Choose your favorite shopping options and spend some money!</p>

          <v-row justify="center">
            <v-col v-for="shopping in shoppingOptions" :key="shopping.value" cols="4">
              <v-btn class="shopping-btn" :color="shopping.selected ? 'deep-purple' : 'deep-purple-accent-2'" stacked
                @click="toggleShopping(shopping)">
                <v-icon v-if="shopping.value === 'shopping_mall'">mdi-shopping</v-icon>
                <v-icon v-if="shopping.value === 'clothing_store'">mdi-tshirt-crew</v-icon>
                <!-- <v-icon v-if="shopping.value === 'electronics_store'">mdi-cellphone</v-icon> -->
                <v-icon v-if="shopping.value === 'book_store'">mdi-book</v-icon>
                <div>{{ shopping.label }}</div>
              </v-btn>
              <br>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>

  <!-- Save button -->
  <v-row justify="center" class="mt-4">
    <v-col cols="12" md="1" class="text-center">
      <v-btn size="large" class="save-btn" color="deep-purple-accent-2" @click="savePreferencesToUser">
        Save
      </v-btn>
    </v-col>
  </v-row>
</template>

<script>
import { defineComponent } from 'vue';
import axios from 'axios';
import Cookies from 'js-cookie';

export default defineComponent({
  data() {
    return {

      selectedActivities: [],
      selectedFoods: [],
      selectedShopping: [],
      selectedAccommodation: [],
      existingUserData: {},
      savedActivities: [],
      showSnackbar: false,
      existingUserData: {},

      activities: [
        { value: 'amusement_park', label: 'Amusement Park', selected: false },
        { value: 'museum', label: 'Museum', selected: false },
        { value: 'art_gallery', label: 'Art Gallery', selected: false },
        { value: 'zoo', label: 'Zoo', selected: false },
        { value: 'aquarium', label: 'Aquarium', selected: false },
        { value: 'stadium', label: 'Stadium', selected: false },
        { value: 'casino', label: 'Casino', selected: false },
        { value: 'night_club', label: 'Night Club', selected: false },

        // Add more activities as needed
      ],


      ethnicFoods: [
        { value: 'american', label: 'American', selected: false },
        { value: 'mexican', label: 'Mexican', selected: false },
        { value: 'european_mediterranean', label: 'European & Mediterranean', selected: false },
        { value: 'east_asian', label: 'East Asian', selected: false },
        { value: 'south_asian', label: 'South Asian', selected: false },
        { value: 'east_asian_2', label: 'East Asian 2', selected: false }, // Consider renaming for clarity
        { value: 'bar', label: 'Bar', selected: false },
        { value: 'specialty', label: 'Specialty Food Types', selected: false },
        { value: 'dietary_focused', label: 'Dietary-Focused', selected: false },
      ],


      shoppingOptions: [
        { value: 'shopping_mall', label: 'Shopping Mall', selected: false },
        { value: 'clothing_store', label: 'Clothing Store', selected: false },
        // { value: 'electronics_store', label: 'Electronics Store', selected: false },
        { value: 'book_store', label: 'Book Store', selected: false },
        // Add more shopping options as needed
      ],
    };
  },
  mounted() {
    this.fetchUserPreferences();
    const token = Cookies.get('login_token');
    console.log('token from navbar: ', token)


  },
  methods: {
    toggleActivity(activity) {
      activity.selected = !activity.selected;
      if (activity.selected) {
        // If activity is selected, add it to the array
        this.selectedActivities.push(activity.label);
      } else {
        // If activity is unselected, remove its label from the array
        const index = this.selectedActivities.indexOf(activity.label);
        if (index !== -1) {
          this.selectedActivities.splice(index, 1);
        }
      }
      console.log('Activities array: ', this.selectedActivities);
    },
    toggleFood(food) {
      food.selected = !food.selected;
      if (food.selected) {
        // If activity is selected, add it to the array
        this.selectedFoods.push(food.label);
      } else {
        // If activity is unselected, remove its label from the array
        const index = this.selectedFoods.indexOf(food.label);
        if (index !== -1) {
          this.selectedFoods.splice(index, 1);
        }
      }
      console.log('Foods array: ', this.selectedFoods);
    },
    toggleShopping(shopping) {
      shopping.selected = !shopping.selected;
      if (shopping.selected) {
        // If activity is selected, add it to the array
        this.selectedShopping.push(shopping.label);
      } else {
        // If activity is unselected, remove its label from the array
        const index = this.selectedShopping.indexOf(shopping.label);
        if (index !== -1) {
          this.selectedShopping.splice(index, 1);
        }
      }
      console.log('Shopping array: ', this.selectedShopping);
      console.log('Accommodation Preference: ', this.selectedAccommodation)
    },
    savePreferencesToUser() {
      const token = Cookies.get('login_token');
      const preferences = {
        selectedActivities: this.selectedActivities,
        selectedFoods: this.selectedFoods,
        selectedShopping: this.selectedShopping,
        selectedAccommodation: this.selectedAccommodation,
      };

      axios.post('http://localhost:8000/api/user_profiling/save_preferences_to_user', preferences, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then(response => {
          // Handle response
          console.log('Preferences saved successfully:', response.data);
          this.showSnackbar = true;
        })
        .catch(error => {
          // Handle error
          console.error('Error saving preferences:', error);
        });
    },
    //Function to gather user preferences from database
    async fetchUserPreferences() {
      const token = Cookies.get('login_token');
      try {
        const response = await axios.get('http://localhost:8000/api/user_profiling/fetch_user_preferences', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        //Get user preferences from respone
        this.existingUserData = response.data;

        //Printing response data to console
        console.log('-----------FROM FETCHED DATA------------')
        console.log(this.existingUserData);
        console.log('Activities: ', this.existingUserData.activities);
        console.log('Foods: ', this.existingUserData.foods);
        console.log('Shopping: ', this.existingUserData.shopping);
        console.log('Accommodation: ', this.existingUserData.accommodation);
        console.log('-----------END FETCHED DATA------------')

        //Turning response data into arrays that can be used to update buttons to reflect previously selected preferences
        const activitiesArray = Array.from(this.existingUserData.activities);
        const foodsArray = Array.from(this.existingUserData.foods);
        const shoppingArray = Array.from(this.existingUserData.shopping);
        //Accommodation just directly set because only one can be chosen
        this.selectedAccommodation = this.existingUserData.accommodation;

        //Actually updates buttons and selected options on vue end
        this.toggleButtons(activitiesArray, this.activities);
        this.toggleButtons(foodsArray, this.ethnicFoods);
        this.toggleButtons(shoppingArray, this.shoppingOptions);
        //this.toggleButtons(accommodationArray, this.selectedAccommodation);

        //Prints preferences saved on vue end
        console.log('********FROM SELECTED OPTIONS VUE**********');
        console.log('Selected Activities: ', this.selectedActivities);
        console.log('Selected Foods: ', this.selectedFoods);
        console.log('Selected Shopping: ', this.selectedShopping);
        console.log('Selected Accommodation: ', this.selectedAccommodation);
        console.log('********END SELECTED OPTIONS VUE**********');
      } catch (error) {
        console.error('Error fetching user preferences:', error);
      }
    },
    toggleButtons(preferences, options) {
      //Loop through the preferences retrieved from the backend
      for (const preference of preferences) {
        //Find the corresponding option in the Vue array and set its selected property to true
        const option = options.find(option => option.label === preference);
        if (option) {
          if (options === this.activities) {
            this.selectedActivities.push(option.label);
            option.selected = true;
          } else if (options === this.ethnicFoods) {
            this.selectedFoods.push(option.label);
            option.selected = true;
          } else if (options === this.shoppingOptions) {
            this.selectedShopping.push(option.label);
            option.selected = true;

          }

        }
      }
    },
  },
  async checkLoginStatus() {
    const url = 'http://localhost:8000/api/check_login_status';

    const token = Cookies.get('login_token');
    console.log('token from navbar: ', token)
    this.isLoggedIn = true;
    if (token) {
      return token;
    }
    if (!token) {
      console.log('Token not available.');
      this.isLoggedIn = false;
      return;
    }

  },
},
);
</script>

<style scoped>
.interest-btn {
  width: 100%;
  margin-top: 8px;
}

.save-btn {
  width: 100%;
  margin-top: 16px;
}

.activities-btn {
  width: 100%;
  margin-top: 8px;
}

.food-btn {
  width: 100%;
  margin-top: 8px;
}

.shopping-btn {
  width: 100%;
  margin-top: 8px;
}
</style>