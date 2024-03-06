<template>
    <v-app>
      <v-content>
        <v-card width="500" class="mx-auto mt-9">
          <v-card-title>Create an Account</v-card-title>
          <v-card-text>
            <v-text-field v-model="email" label="Email" prepend-icon="mdi-account-circle"/>
            <v-text-field v-model="firstname" label="First Name" prepend-icon="mdi-account-circle"/>
            <v-text-field v-model="lastname" label="Last Name" prepend-icon="mdi-account-circle"/>
            <v-text-field 
              v-model="password"
              label="Create Password" 
              :type="showPassword ? 'text' : 'password'"
              prepend-icon="mdi-lock"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="showPassword = !showPassword"/>
              <div v-if="RegistrationErrorMessage" class="error-message">{{ RegistrationErrorMessage }}</div>
          </v-card-text>
  
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn color="deep-purple-accent-2" @click="register">Create Account</v-btn>
            <router-link :to="{ name: 'LoginPage' }">
                <v-btn color="deep-purple-accent-2">Existing User?</v-btn>
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
        firstname: '',
        lastname: '',
        password: '',
        RegistrationErrorMessage: '',
        message: ''
      };
    },
    methods: {
      //Checks to see if the email address is valid
      isValidEmail(email) {
        // Regular expression for basic email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
      },

      //Checks to see if password has at least 1 uppercase letter, 1 lowercase letter, 1 number, 1 special character, and be at least 8 characters long.
      isValidPassword(password) {
        // Regular expression for password validation
        const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
        return passwordRegex.test(password);
      },

      //Register account with flask server database
      register() {
        // Make an AJAX request to Flask application
        const url = 'http://localhost:8000/api/RegisterUser'; //The localhost port I have Flask running on
  
        //Checks for valid email address format
        if (!this.isValidEmail(this.email)) {
          this.RegistrationErrorMessage = 'Please enter a valid email address.';
          return;
        }

        //Validate password format
        if (!this.isValidPassword(this.password)) {
          this.RegistrationErrorMessage = 'Password must contain at least 1 uppercase letter, 1 lowercase letter, 1 number, 1 special character, and be at least 8 characters long.';
          return;
        }

        // Check if both username and password are provided
        if (!this.password || !this.firstname || !this.lastname || !this.email) {
          this.RegistrationErrorMessage = 'All fields are required.'
          console.error('All text fields are required.');
          return;
        }
  
        //Use Axios library for AJAX requests
        // Send user info to the Flask API
        axios.post(url, { email: this.email, firstname: this.firstname, lastname: this.lastname, password: this.password })
          .then(response => {
            console.log('User registered successfully!', response);
            this.message = 'User registered successfully.';
            this.login();
          })
          .catch(error => {
            console.error('Error registering user', error);
            if (error.response) {
              if (error.response.status === 400) {
                console.error('Registration failed: Email already exists.');
                this.RegistrationErrorMessage = 'Registration failed: Email already exists.';
              } else {
                console.error('Registration failed: Server error.');
                this.RegistrationErrorMessage = 'Registration failed: Server error.';
              }
            } else {
              this.RegistrationErrorMessage = 'Network error or server unreachable.';
            }
          });
        console.log('Registering...');
      },
      //Login request sent to flask server
      login() {
        //Make an AJAX request to Flask application
        const url = 'http://localhost:8000/api/LoginUser'; //The localhost port I have Flask running on

        //Check if both username and password are provided
        if (!this.email || !this.password) {
          this.loginErrorMessage = 'Email and password are required.';
          this.showLoginError = true;
          console.error('Email and password are required.');
          return;
        }

        axios.post(url, { email: this.email, password: this.password }, { withCredentials: true })

          .then(response => {
            const token = response.data.access_token;
            console.log('login token: ', token) //Display token after recieved to browser console
            //Make cookies expire after 7 days
            const expirationDate = new Date();
            expirationDate.setDate(expirationDate.getDate() + 7);

            //Store the token with expiration date in the form of a cookie
            Cookies.set('login_token', token, { secure: false, expires: expirationDate });
            //console.log('Login token:', token) //Display token after cookies set
            console.log('User logged in successfully, login token: ', token)
            this.checkLoginStatus();
            //Redirect to the home page
            this.$router.push({ name: 'EmailVerification' });
          
          })
          .catch(error => {
            console.error('Error logging in', error);

            console.log('Error response:', error.response);
            console.log('Error status:', error.response.status);
            console.log('Error data:', error.response.data);

            //Handle different status codes and display appropriate messages
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
      //Logout request sent to flask server
      logout() {
        const url = 'http://localhost:8000/api/LogoutUser'; // Update with your Flask app's URL
  
        //Remove the user token or session ID from the cookie
        Cookies.remove('login_token', { httpOnly: true });
  
        //Send a request to the Flask API to handle logout
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
      //Check login status (mostly for testing on this page)
      async checkLoginStatus() {
        const url = 'http://localhost:8000/api/check_login_status';

        try {
          if (!this.token) {
            //Token is not available, handle accordingly
            this.isLoggedIn = false;
            console.log('Token not available');
            return;
          }

          const response = await axios.get(url, { headers: { Authorization: `Bearer ${this.token}` } });
          console.log('Response from checkLoginStatus:', response.data);

          this.isLoggedIn = true;
          response.data.message === 'User is logged in';
          console.log('User is logged in:', this.isLoggedIn);
        } catch (error) {
          console.error('Error checking login status', error);
          this.isLoggedIn = false;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  .error-message {
  color: red;
  margin-top: 10px;
}
  </style>
  