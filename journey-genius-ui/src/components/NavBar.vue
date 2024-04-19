<template>
  <nav>
    <v-toolbar flat app>
      <!-- Title -->
      <v-toolbar-title class="text-uppercase grey--text mr-5">
        <span class="font-weight-light">Journey</span>
        <span>Genius</span>
      </v-toolbar-title>

      <!-- Buttons that link to other parts of the site -->
      <div class="d-flex align-center ml-16">
        <v-btn v-for="button in buttons" :key="button.to" flat color="grey" :to="button.to">
          {{ button.text }}
        </v-btn>
      </div>

      <v-spacer></v-spacer>

      <!-- Render login/logout button dynamically based on isLoggedIn -->
      <router-link v-if="!isLoggedIn" to="/LoginPage">
        <v-btn color="grey darken-2" flat>
          <span style="margin-right: 5px;">Login</span>
          <v-icon right>mdi-exit-to-app</v-icon>
        </v-btn>
      </router-link>

      <v-btn v-else color="grey darken-2" flat @click="logout">
        <span style="margin-right: 5px;">Logout</span>
        <v-icon right>mdi-exit-to-app</v-icon>
      </v-btn>
    </v-toolbar>
  </nav>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  data() {
    return {
      isLoggedIn: false,
      buttons: [
        { text: 'Home', to: '/' },
      ],
      token: Cookies.get('login_token'),
      isPageRefreshed: false, // Flag to track if the page has been refreshed
    };
  },
  mounted() {
    this.checkLoginStatus();
  },
  methods: {
    logout() {
      const url = 'http://localhost:8000/api/LogoutUser';
      Cookies.remove('login_token');
      Cookies.remove('database_id');
      Cookies.remove('refresh_token');

      axios.post(url)
        .then(response => {
          console.log('Logout successful!', response);
          this.message = 'Logout successful.';
          this.isLoggedIn = false;
          this.$router.push({ name: 'LoggingOut' });
        })
        .catch(error => {
          console.error('Error logging out', error);
          this.message = 'Error logging out.';
        });

      this.buttons = [
        { text: 'Home', to: '/' },
      ];
    },
    checkLoginStatus() {
      const token = Cookies.get('login_token');
      console.log('jwt token from navbar: ', token)
      // If the token is available, it means the user is logged in
      if (token) {
        console.log('User logged in');
        this.isLoggedIn = true;
        console.log(this.isLoggedIn);

        // Update the navigation buttons for logged-in users
        this.buttons = [
          { text: 'Home', to: '/' },
          { text: 'User Profiling', to: '/UserProfiling' },
          { text: 'Plan Trip', to: '/StartPlanning' },
          { text: 'Saved Trips', to: '/SavedTrips' }
        ];
        // Set a flag indicating successful login
        this.$emit('loginSuccess');

      } else {
        // If the token is not available, the user is not logged in
        console.log('Token not available.');
        this.isLoggedIn = false;
      }
    },
  },
};
</script>
