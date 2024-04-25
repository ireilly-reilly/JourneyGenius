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

      <!-- Login/Account Details Button -->
      <v-btn color="grey darken-2" flat @click="drawer = !drawer">
        <span style="margin-right: 5px;">{{ isLoggedIn ? 'Account' : 'Login' }}</span>
        <v-icon right>mdi-account-circle</v-icon>
      </v-btn>
    </v-toolbar>

    <!-- Navigation Drawer -->
    <v-navigation-drawer
      v-model="drawer"
      location="right"
      temporary
      class="custom-drawer-height"

    >
      <v-list dense>
        <!-- Items for logged out users -->
        <v-list-item v-if="!isLoggedIn" @click="login" prepend-icon="mdi-login">
          <v-list-item-title>Login</v-list-item-title>
        </v-list-item>
        <v-list-item v-if="!isLoggedIn" @click="register" prepend-icon="mdi-account-plus">
          <v-list-item-title>Create Account</v-list-item-title>
        </v-list-item>

        <!-- Items for logged in users -->
        <v-list-item
            subtitle= "email"
            title= "test"
          ></v-list-item>
          <br>
        <v-list-item v-if="isLoggedIn" @click="userProfile" prepend-icon="mdi-account-edit">
          <v-list-item-title>Edit User Profile</v-list-item-title>
        </v-list-item>
        <v-list-item v-if="isLoggedIn" @click="logout" prepend-icon="mdi-logout">
          <v-list-item-title>Logout</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  data() {
    return {
      isLoggedIn: false,
      firstname: '',
      buttons: [
        { text: 'Home', to: '/' },
      ],
      drawer: false, // Control the navigation drawer
    };
  },
  mounted() {
    this.checkLoginStatus();
    this.getUserInfoAndGenerateGreeting();

  },
  methods: {
    async getUserInfoAndGenerateGreeting() {
      const url = 'http://localhost:8000/api/user_account/fetch_user_info';
      const jwtToken = Cookies.get('login_token')
      axios.get(url, {
        headers: {
          Authorization: `Bearer ${jwtToken}` // Include the JWT token in the Authorization header
        }
      })
        .then(response => {
          this.firstname = response.data.firstName;
          // this.generateGreetingMessage(firstname)
        })
        .catch(error => {
          console.error('Error fetching user data:', error);
        });
    },

    logout() {
      const url = 'http://localhost:8000/api/LogoutUser';
      Cookies.remove('login_token');
      Cookies.remove('database_id');
      Cookies.remove('refresh_token');

      axios.post(url)
        .then(response => {
          console.log('Logout successful!', response);
          this.isLoggedIn = false;
          this.$router.push({ name: 'LoggingOut' });
        })
        .catch(error => {
          console.error('Error logging out', error);
        });

      this.buttons = [
        { text: 'Home', to: '/' },
      ];
    },
    register() {
      this.$router.push({ name: 'RegisterPage' });
    },
    login() {
      this.$router.push({ name: 'LoginPage' });
    },
    userProfile() {
      this.$router.push({ name: 'UserAccount' });
    },
    
    checkLoginStatus() {
      const token = Cookies.get('login_token');
      // If the token is available, it means the user is logged in
      if (token) {
        this.isLoggedIn = true;
        this.buttons = [
          { text: 'Home', to: '/' },
          { text: 'Trip Preferences', to: '/UserProfiling' },
          { text: 'Plan Trip', to: '/StartPlanning' },
          { text: 'Saved Trips', to: '/SavedTrips' }
        ];
      } else {
        this.isLoggedIn = false;
      }
    },
  },
};
</script>
