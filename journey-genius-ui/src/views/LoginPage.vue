<template>
  <v-app>
    <v-content>
      <template>
        <div class="text-center">
          <!-- Other template markup -->
          <v-snackbar v-model="showSnackbar" color="deep-purple-accent-2" top>
            <span class="centered-text">Login Successful!</span>
          </v-snackbar>
        </div>
      </template>

      <v-card width="500" class="mx-auto mt-9">
        <br>
        <div class="d-flex justify-center">
          <v-icon size="56" class="display-1" color="deep-purple-accent-2">
            mdi-account-circle
          </v-icon>
        </div>
        <v-card-title class="display-1 mb-5">Login</v-card-title> <!-- Added margin bottom -->
        <v-card-text>
          <v-text-field v-model="email" label="Email" prepend-icon="mdi-email"
            :class="{ 'error-outline': showLoginError }" @keyup.enter="login" />
          <v-text-field v-model="password" label="Password" :type="showPassword ? 'text' : 'password'"
            prepend-icon="mdi-lock" :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword" :class="{ 'error-outline': showLoginError }"
            @keyup.enter="login" />
          <div v-if="loginErrorMessage" class="error-message">{{ loginErrorMessage }}</div>
        </v-card-text>

        <v-divider></v-divider>
        <v-card-actions>
          <v-btn class="ml-3" color="deep-purple-accent-2" @click="login">Login</v-btn>
          <router-link :to="{ name: 'RegisterPage' }">
            <v-btn color="deep-purple-accent-2">New User?</v-btn>
          </router-link>
        </v-card-actions>
      </v-card>

      <br>
    </v-content>

    <v-footer dark padless>
      <v-card class="flex" flat tile>
        <v-card-title class="teal">
          <v-spacer></v-spacer>
          <v-btn v-for="icon in icons" :key="icon" class="mx-4" dark icon>
            <v-icon size="24px">{{ icon }}</v-icon>
          </v-btn>
        </v-card-title>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
//Imports
import axios from 'axios';
import Cookies from 'js-cookie';
import { ref } from 'vue';

export default {
  data() {
    return {
      showPassword: false,
      email: '',
      password: '',
      loginErrorMessage: '',
      registrationErrorMessage: '',
      showLoginError: false,
      showRegistrationError: false,
      token: Cookies.get('login_token') || '', // Retrieve token from Cookies
      showSnackbar: false,


    };
  },
  created() {
    this.checkLoginStatus();
  },
  methods: {
    //Login Request to flask server
    login() {
      //Make an AJAX request to Flask application
      const url = 'http://localhost:8000/api/LoginUser'; //The localhost port I have Flask running on

      // Check if both username and password are provided
      if (!this.email || !this.password) {
        this.loginErrorMessage = 'Email and password are required.';
        this.showLoginError = true;
        console.error('Email and password are required.');
        return;
      }

      axios.post(url, { email: this.email, password: this.password }, { withCredentials: true })

        .then(response => {
          const token = response.data.access_token;
          const databaseID = response.data.user_id;
          const refresh_token = response.data.refresh_token;
          console.log('login token: ', token) //Display token after recieved

          //Store the token in a secure manner (e.g., HttpOnly cookie) with expiration date
          Cookies.set('login_token', token, { secure: false });
          Cookies.set('database_id', databaseID, { secure: false });
          Cookies.set('refresh_token', refresh_token, { secure: false });
          //console.log('Login token:', token) //Display token after cookies set
          console.log('User logged in successfully, login token: ', token);
          console.log('User ID from database: ', databaseID);
          this.checkLoginStatus();

          this.showSnackbar = true; // Show the Snackbar

          setTimeout(() => {
            window.location = '/'; // Directly navigate to home and refresh
          }, 1000);

        })

        .catch(error => {
          console.error('Error logging in', error);


          //Handle different status codes and display appropriate messages
          if (error.response) {
            this.showLoginError = true;
            if (error.response.status === 401) {
              console.error('Login failed: Incorrect username or password.');
              this.loginErrorMessage = 'Incorrect username or password.';
            }
            if (error.response.status === 403) {
              this.loginErrorMessage = 'Your account has been frozen. Please contact support for assistance.';
            } 
          } else {
            this.loginErrorMessage = 'Network error or server unreachable.';
          }
        });

      console.log('Logging in...');
    },

    //Check login status (mostly for testing purposes on this page)
    async checkLoginStatus() {
      const url = 'http://localhost:8000/api/check_login_status';

      try {
        if (!this.token) {
          // Token is not available, handle accordingly
          this.isLoggedIn = false;
          console.log('Token not available');
          return;
        }

        const response = await axios.get(url, { headers: { Authorization: `Bearer ${this.token}` } });
        console.log('Response from checkLoginStatus:', response.data);

        this.isLoggedIn = true;
        response.data.message === 'User is logged in';
        console.log('User is logged in:', this.isLoggedIn);
        console.log("From Login page checkLoginStatus:")
      } catch (error) {
        console.error('Error checking login status', error);
        this.isLoggedIn = false;
        console.log("From Login page checkLoginStatus:")
        console.log("Logged in: ", this.isLoggedIn)
      }
    },

  }
};
</script>

<style scoped>
/* Add custom styles if needed */
.error-message {
  color: red;
  margin-top: 10px;
  font-size: medium;
  text-align: left;
  margin-right: 10px;
}

.error-outline {
  border-color: red;
}

.centered-text {
  display: block;
  text-align: center;
  font-size: medium;
}

.display-1 {
  font-size: 1.25rem;
  text-align: center;
}
</style>
