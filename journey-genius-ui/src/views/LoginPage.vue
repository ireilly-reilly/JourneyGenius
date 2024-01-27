<template>
  <v-app>
    <v-content>
      <v-card width="500" class="mx-auto mt-9">
        <v-card-title>Login</v-card-title>
        <v-card-text>
          <v-text-field v-model="email" label="Email" prepend-icon="mdi-account-circle" :class="{ 'error-outline': showLoginError }"/>
          <v-text-field 
            v-model="password"
            label="Password" 
            :type="showPassword ? 'text' : 'password'"
            prepend-icon="mdi-lock"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword"
            :class="{ 'error-outline': showLoginError }"/>
            <div v-if="loginErrorMessage" class="error-message">{{ loginErrorMessage }}</div>
        </v-card-text>

        <v-divider></v-divider>
        <v-card-actions>
          <v-btn color="deep-purple-accent-2" @click="login">Login</v-btn>
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
// Import Axios at the top of your script
import axios from 'axios';
import Cookies from 'js-cookie';
export default {
  data() {
    return {
      showPassword: false,
      email: '',
      password: '',
      loginErrorMessage: '',
      registrationErrorMessage: '',
      showLoginError: false,
      showRegistrationError: false
    };
  },
  methods: {
    login() {
      // Implement your login logic here
      // Make an AJAX request to Flask application
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
          console.log('User logged in successfully!', response);

          // Store the user token or session ID in a secure HTTP-only cookie
          Cookies.set('login_token', response.data.token, { httpOnly: true });
          
          this.message = 'User logged in successfully.';

          this.checkLoginStatus(); //Not sure where to put this yet
          // Redirect to the home page
          this.$router.push({ name: 'Home' });
          
        })
        .catch(error => {
          console.error('Error logging in', error);
          // Handle different status codes and display appropriate messages
          if (error.response) {
            this.showLoginError = true;
            if (error.response.status === 401) {
              console.error('Login failed: Incorrect username or password.');
              this.loginErrorMessage = 'Incorrect username or password.';
            } else {
              console.error('Login failed: Server error.');
              this.loginErrorMessage = 'Error logging in.';
            }
          } else {
            this.loginErrorMessage = 'Network error or server unreachable.';
          }
        });

      console.log('Logging in...');
    },
    logout() {
      const url = 'http://localhost:8000/api/LogoutUser'; // Update with your Flask app's URL

      // Remove the user token or session ID from the cookie
      Cookies.remove('login_token', { httpOnly: true });

      // Send a request to the Flask API to handle logout
      axios.post(url)
        .then(response => {
          console.log('Logout successful!', response);
          this.message = 'Logout successful.';
        })
        .catch(error => {
          console.error('Error logging out', error);
          this.message = 'Error logging out.';
        });
    },
    checkLoginStatus() {
      const url = 'http://localhost:8000/api/check_login_status'; // Update with your Flask app's URL

      // Send a request to the Flask API to check the login status
      axios.get(url, { withCredentials: true })
        .then(response => {
          console.log('Login status:', response.data.message);
          this.message = response.data.message;
        })
        .catch(error => {
          console.error('Error checking login status', error);
          this.message = 'Error checking login status.';
        });
    },
  }
};
</script>

<style scoped>
/* Add custom styles if needed */
.error-message {
  color: red;
  margin-top: 10px;
}
.error-outline {
  border-color: red;
}
</style>
