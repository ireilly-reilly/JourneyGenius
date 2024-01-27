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
              <v-col cols="12" md="6">
                <v-select v-model="gender" label="Gender" :items="genderOptions"></v-select>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field v-model="age" label="Age" type="number"></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field v-model="email" label="Email"></v-text-field>
              </v-col>
            </v-row>
          </v-form>
        </v-card>
      </v-col>
    </v-row>

    <!-- Interest Activities Section -->
    <v-row justify="center" class="mt-4">
      <v-col cols="12" md="8">
        <v-card class="pa-4">
          <h3 class="headline text-deep-purple-accent-2">Interest Activities</h3>
          <v-row justify="center">
            <v-col v-for="activity in interestActivities" :key="activity" cols="4">
              <v-btn class="interest-btn" stacked="" :color="selectedActivities.includes(activity) ? 'deep-purple' : 'deep-purple-accent-2'"
                @click="toggleInterest(activity)">
                <v-icon v-if="activity === 'Beaches'">mdi-beach</v-icon>
                <v-icon v-if="activity === 'City Sightseeing'">mdi-city</v-icon>
                <v-icon v-if="activity === 'Outdoor Adventures'">mdi-image-filter-hdr</v-icon>
                <v-icon v-if="activity === 'Festival/Events'">mdi-party-popper</v-icon>
                <v-icon v-if="activity === 'Food Exploration'">mdi-food</v-icon>
                <v-icon v-if="activity === 'Nightlife'">mdi-glass-cocktail</v-icon>
                <v-icon v-if="activity === 'Shopping'">mdi-shopping</v-icon>
                <v-icon v-if="activity === 'Spa Wellness'">mdi-spa</v-icon>
                {{ activity }}
              </v-btn>
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
    <v-row justify="center" class="mt-4">
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
    </v-row>
  </v-container>

  <!-- Save button -->
  <v-row justify="center" class="mt-4">
    <v-col cols="12" md="1" class="text-center">
      <v-btn class="save-btn" color="deep-purple-accent-2" @click="saveData">
        Save
      </v-btn>
    </v-col>
  </v-row>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      interestActivities: [
        'Beaches', 'City Sightseeing', 'Outdoor Adventures', 'Festival/Events',
        'Food Exploration', 'Nightlife', 'Shopping', 'Spa Wellness'
      ],
      selectedActivities: [],
      firstName: '',
      lastName: '',
      gender: null,
      age: null,
      email: '',
      genderOptions: ['Male', 'Female', 'Other'],
      accommodationPreference: null,
      transportationPreference: null
    };
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
  },
});
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
