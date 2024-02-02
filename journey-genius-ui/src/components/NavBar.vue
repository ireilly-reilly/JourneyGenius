<template>
    <nav :key="isLoggedIn">
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
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  data() {
    return {
      isLoggedIn: false,
      buttons: [
        { text: 'Home', to: '/' },
        { text: 'User Profiling', to: '/UserProfiling' },
        { text: 'Plan Trip', to: '/StartPlanning' },
        { text: 'Saved Trips', to: '/SavedTrips' },
      ],
      token: Cookies.get('login_token'),
    };
  },
  mounted() {
    this.checkLoginStatus();
  },
  methods: {
    // getToken() {
    //   return Cookies.get('login_token');
    // },
    logout() {
      const url = 'http://localhost:8000/api/LogoutUser';
      Cookies.remove('login_token');

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
    },
    async checkLoginStatus() {
      const url = 'http://localhost:8000/api/check_login_status';

      const token = Cookies.get('login_token');
      console.log('token from navbar: ', token)
      this.isLoggedIn = true;

      if (!token) {
        console.log('Token not available.');
        this.isLoggedIn = false;
        return;
      }

    },
    reloadComponent() {
      // Manually reload the component
      const currentRoute = this.$route;
      this.$router.replace({ name: 'dummy' }).then(() => {
        this.$router.replace(currentRoute);
      });
    },
    
  },
};
</script>
  
  