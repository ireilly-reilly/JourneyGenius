<template>
    <nav>
      <v-toolbar flat app>
  
        <!-- If we want to utilize the sidebar component -->
        <!-- <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon> -->
  
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
  
        <router-link v-if="!isLoggedIn" to="/LoginPage">
          <v-btn color="grey darken-2" flat>
            <span style="margin-right: 5px;">Login</span>
            <v-icon right>mdi-exit-to-app</v-icon>
          </v-btn>
        </router-link>

        <v-btn v-if="isLoggedIn" color="grey darken-2" flat @click="logout">
          <span style="margin-right: 5px;">Logout</span>
          <v-icon right>mdi-exit-to-app</v-icon>
        </v-btn>
      </v-toolbar>
    </nav>
  </template>
  
  <script>
  // Import Axios at the top of your script
  import axios from 'axios';
  import Cookies from 'js-cookie';
  export default {
    data() {
      return {
        isLoggedIn: false, // Default to not logged in
        buttons: [
          { text: 'Home', to: '/' },
          { text: 'User Profiling', to: '/UserProfiling' },
          { text: 'Plan Trip', to: '/StartPlanning' },
          { text: 'Saved Trips', to: '/SavedTrips' },
        ],
      };
    },
    created() {
      this.checkLoginStatus();
    },
    methods: {
      logout() {
        const url = 'http://localhost:8000/api/LogoutUser'; // Update with your Flask app's URL

        // Remove the user token or session ID from the cookie
        Cookies.remove('login_token', { httpOnly: true });

        // Send a request to the Flask API to handle logout
        axios.post(url)
          .then(response => {
            console.log('Logout successful!', response);
            this.message = 'Logout successful.';
            this.isLoggedIn = false;
            //window.location.reload();
          })
          .catch(error => {
            console.error('Error logging out', error);
            this.message = 'Error logging out.';
          });
        //this.checkLoginStatus()
      },
      async checkLoginStatus() {
        const url = 'http://localhost:8000/api/check_login_status'; // Update with your Flask app's URL

        // Send a request to the Flask API to check the login status
        axios.get(url, { withCredentials: true })
          .then(response => {
            console.log('Login status:', response.data.message);
            this.message = response.data.message;
            if (this.message == 'User is logged in'){
              this.isLoggedIn = true;
            }
            else if (this.message == 'User is not logged in'){
              this.isLoggedIn = false;
            }
          })
          .catch(error => {
            console.error('Error checking login status', error);
            this.message = 'Error checking login status.';
            this.isLoggedIn = false;
          });
      },
    },
  };
  </script>
  