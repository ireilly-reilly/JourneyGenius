<template>
  <v-container>
    <!-- Your Header -->
    <v-row justify="center" class="mt-4">
      <v-col cols="12" md="8" class="text-center">
        <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">Your Interests</h2>
        <p>User profiling is integral to our application for several reasons.
          By understanding the unique preferences, interests, budget constraints,
          and travel goals of each user, we can tailor the recommendations to
          match their individual needs. This personalized approach ensures that
          users receive suggestions aligned with their tastes, making their
          vacation experience more enjoyable and satisfying.
        </p>
        <br>
        <hr>
      </v-col>
    </v-row>

    <!-- Personal Information Section -->
    <v-row justify="center" class="mt-4">
      <v-col cols="12" md="8">
        <v-card class="pa-4">
          <h3 class="headline text-deep-purple-accent-2">Personal Information</h3>
          <v-form>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field v-model="firstName" label="First Name"></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field v-model="lastName" label="Last Name"></v-text-field>
              </v-col>
              <!-- <v-col cols="12" md="6">
                <v-select v-model="gender" label="Gender" :items="genderOptions"></v-select>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field v-model="age" label="Age" type="number"></v-text-field>
              </v-col> -->
              <v-col cols="12">
                <v-text-field v-model="email" label="Email"></v-text-field>
              </v-col>
            </v-row>
          </v-form>
        </v-card>
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
              <v-btn class="companion-btn" :color="activity.selected ? 'deep-purple' : 'deep-purple-accent-2'" stacked
                @click="selectActivity(activity)">
                <v-icon v-if="activity.value === 'amusement_park'">mdi-popcorn</v-icon>
                <v-icon v-if="activity.value === 'aquarium'">mdi-fish</v-icon>
                <v-icon v-if="activity.value === 'art_gallery'">mdi-palette</v-icon>
                <v-icon v-if="activity.value === 'museum'">mdi-bank</v-icon>
                <v-icon v-if="activity.value === 'stadium'">mdi-football</v-icon>
                <v-icon v-if="activity.value === 'zoo'">mdi-dog</v-icon>
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
              <v-btn class="companion-btn" :color="food.selected ? 'deep-purple' : 'deep-purple-accent-2'" stacked
                @click="selectEthnicFood(food)">
                <v-icon v-if="food.value === 'asian'">mdi-noodles</v-icon>
                <v-icon v-if="food.value === 'american'">mdi-hamburger</v-icon>
                <v-icon v-if="food.value === 'italian'">mdi-pizza</v-icon>
                <v-icon v-if="food.value === 'mexican'">mdi-taco</v-icon>
                <v-icon v-if="food.value === 'mediterranean'">mdi-fish</v-icon>
                <v-icon v-if="food.value === 'vegan'">mdi-leaf</v-icon>
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
              <v-btn class="companion-btn" :color="shopping.selected ? 'deep-purple' : 'deep-purple-accent-2'" stacked
                @click="selectShopping(shopping)">
                <v-icon v-if="shopping.value === 'shopping_mall'">mdi-shopping</v-icon>
                <v-icon v-if="shopping.value === 'clothing_store'">mdi-tshirt-crew</v-icon>
                <v-icon v-if="shopping.value === 'electronics_store'">mdi-cellphone</v-icon>
                <v-icon v-if="shopping.value === 'book_store'">mdi-book</v-icon>
                <div>{{ shopping.label }}</div>
              </v-btn>
              <br>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>

    <!-- Accommodation Preferences Section -->
    <v-row justify="center" class="mt-4">
      <v-col cols="12" md="8">
        <v-card class="pa-4">
          <h3 class="headline text-deep-purple-accent-2">Accommodation Preferences</h3>
          <v-form>
            <v-radio-group v-model="accommodationPreference">
              <v-radio label="Hotels" value="hotels"></v-radio>
              <v-radio label="Resorts" value="resorts"></v-radio>
              <v-radio label="Vacation Rentals" value="vacationRentals"></v-radio>
            </v-radio-group>
          </v-form>
        </v-card>
      </v-col>
    </v-row>

    <!-- Transportation Preferences Section -->
    <!-- <v-row justify="center" class="mt-4">
      <v-col cols="12" md="8">
        <v-card class="pa-4">
          <h3 class="headline text-deep-purple-accent-2">Transportation Preferences</h3>
          <v-form>
            <v-radio-group v-model="transportationPreference">
              <v-radio label="Train" value="train"></v-radio>
              <v-radio label="Rental Car" value="rentalCar"></v-radio>
              <v-radio label="Ride Services" value="rideServices"></v-radio>
            </v-radio-group>
          </v-form>
        </v-card>
      </v-col>
    </v-row> -->
  </v-container>

  <!-- Save button -->
  <v-row justify="center" class="mt-4">
    <v-col cols="12" md="1" class="text-center">
      <v-btn size="large" class="save-btn" color="deep-purple-accent-2" @click="saveData">
        Save
      </v-btn>
    </v-col>
  </v-row>
</template>

<script>
import { defineComponent } from 'vue';
import axios from 'axios';
import Cookies from 'js-cookie'

export default defineComponent({
  data() {
    return {
      
      selectedActivities: [],
      firstName: '',
      lastName: '',
      gender: null,
      age: null,
      email: '',
      genderOptions: ['Male', 'Female', 'Other'],
      accommodationPreference: null,
      transportationPreference: null,
      existingUserData: {},
      savedActivities: [],

      activities: [
        { value: 'amusement_park', label: 'Amusement Park', selected: false },
        { value: 'aquarium', label: 'Aquarium', selected: false },
        { value: 'art_gallery', label: 'Art Gallery', selected: false },
        { value: 'museum', label: 'Museum', selected: false },
        { value: 'stadium', label: 'Stadium', selected: false },
        { value: 'zoo', label: 'Zoo', selected: false },
        // Add more activities as needed
      ],

      ethnicFoods: [
        { value: 'asian', label: 'Asian', selected: false },
        { value: 'american', label: 'American', selected: false },
        { value: 'italian', label: 'Italian', selected: false },
        { value: 'mexican', label: 'Mexican', selected: false },
        { value: 'mediterranean', label: 'Mediterranean', selected: false },
        { value: 'vegan', label: 'Vegan', selected: false },
      ],

      shoppingOptions: [
        { value: 'shopping_mall', label: 'Shopping Mall', selected: false },
        { value: 'clothing_store', label: 'Clothing Store', selected: false },
        { value: 'electronics_store', label: 'Electronics Store', selected: false },
        { value: 'book_store', label: 'Book Store', selected: false },
        // Add more shopping options as needed
      ],
    };
  },
  mounted() {

    const token = Cookies.get('login_token');
      console.log('token from navbar: ', token)

    if (token) {
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    }

    axios.get('/api/get_user_profile')
        .then(response => {
            this.firstName = response.data.firstName;
            this.lastName = response.data.lastName;
            this.gender = response.data.gender;
            this.age = response.data.age;
            this.email = response.data.email;
            this.accommodationPreference = response.data.accommodationPreference;
            this.transportationPreference = response.data.transportationPreference;
            this.selectedActivities = response.data.selectedActivities;
        })
        .catch(error => {
            console.error('Error fetching user profile data:', error);
        });
  },
  methods: {
    toggleInterest(activity) {
      const index = this.selectedActivities.indexOf(activity);
      if (index === -1) {
        this.selectedActivities.push(activity);
      } else {
        this.selectedActivities.splice(index, 1);
      }
    },

    saveData() {
    axios.post('/api/save_user_data', {
        firstName: this.firstName,
        lastName: this.lastName,
        gender: this.gender,
        age: this.age,
        email: this.email,
        accommodationPreference: this.accommodationPreference,
        transportationPreference: this.transportationPreference,
        selectedActivities: this.selectedActivities
    })
    .then(response => {
        console.log('Data saved successfully:', response.data);
        // Optionally, show a success message or navigate to another page
    })
    .catch(error => {
        console.error('Error saving user profile data:', error);
        // Optionally, show an error message to the user
    });


      // Log the form data
      console.log('Data saved:', {
        firstName: this.firstName,
        lastName: this.lastName,
        gender: this.gender,
        age: this.age,
        email: this.email,
        selectedActivities: this.selectedActivities,
        accommodationPreference: this.accommodationPreference,
        transportationPreference: this.transportationPreference,
      });
      // Add your logic to save the data (e.g., send it to a server)
      // You can also navigate to another page or show a success message
    },

    // Add your logic to save the data (e.g., send it to a server)
    // You can also navigate to another page or show a success message
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


  fetchExistingUserData() {
        const token = Cookies.get('login_token');
        console.log("Token from fetch: ", token)

        // Make an HTTP GET request to fetch the existing user data
        axios.get('http://localhost:8000/api/get_user_profile', { headers: { Authorization: `Bearer ${token}` }})
             .then(response => {
                 this.existingUserData = response.data;
                 // Autofill the text fields with the existing user data
                 this.firstName = this.existingUserData.firstName;
                 this.lastName = this.existingUserData.lastName;
                 this.email = this.existingUserData.email;
                 // ... autofill other fields as needed ...
             })
             .catch(error => {
                 console.error('Error fetching existing user data from fetchExistingUserData:', error);
             });
    },



  // fetchExistingUserData() {
  //   const token = this.checkLoginStatus();
  //   console.log("Token from fetch: ", token)

  //   // Make an HTTP GET request to fetch the existing user data
  //   axios.get('http://localhost:8000/api/GetUserProfile', { headers: { Authorization: `Bearer ${token}` }})




  //      .then(response => {
  //        this.existingUserData = response.data;
  //        // Autofill the text fields with the existing user data
  //        this.firstName = this.existingUserData.firstName;
  //        this.lastName = this.existingUserData.lastName;
  //        this.email = this.existingUserData.email;
  //        // ... autofill other fields as needed ...
  //      })
  //      .catch(error => {
  //        console.error('Error fetching existing user data from fetchExistingUserData:', error);
  //      });
  //  },
  getGender(gender) {
    switch (gender) {
      case 'Male':
        return 'M';
      case 'Female':
        return 'F';
      case 'Other':
        return 'O';
    }
  },
  // Method to send data to the Flask backend
  sendDataToBackend() {
    const selectedGender = this.getGender(this.gender);

    // Now you can send the selectedGender to your Flask backend
    // using an HTTP request (e.g., axios.post or axios.put)
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
</style>
