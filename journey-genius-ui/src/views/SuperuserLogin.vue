<template>
  <div class="login-page">
    <v-app-bar app color="grey lighten-2">
      <v-toolbar-title>Journey Genius - Admin Portal</v-toolbar-title>
      <!-- Buttons that link to other parts of the site -->
      <div class="d-flex align-center ml-16">
        <v-btn v-for="button in buttons" :key="button.to" text color="black" :to="button.to">
          {{ button.text }}
        </v-btn>
      </div>
      <v-spacer></v-spacer>
    </v-app-bar>

    <div class="login-form">
      <div class="form-title">
        <v-icon size="50" color="deep-purple-accent-2">mdi-account-circle</v-icon>
        <span>Admin Portal</span>
      </div>
      <div class="form-input">
        <v-text-field v-model="email" label="Email" outlined color="black" @keyup.enter="login"></v-text-field>
      </div>
      <div class="form-input">
        <v-text-field v-model="password" label="Password" outlined color="black" type="password" @keyup.enter="login"></v-text-field>
      </div>
      <div class="form-actions">
        <v-btn @click="login" color="deep-purple-accent-2">Login</v-btn>
      </div>
    </div>
    <v-snackbar v-model="showSnackbar" color="deep-purple-accent-2" top>
      <span class="centered-text">Login Successful!</span>
    </v-snackbar>
  </div>
</template>


<script>
//Imports
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
      showRegistrationError: false,
      token: Cookies.get('login_token') || '', // Retrieve token from Cookies
      showSnackbar: false,
      toast: {
        show: false,
        message: '',
        timeout: 2000,
        color: 'error',
      },
    };
  },
  methods: {
    //Login Request to flask server
    login() {
      //Make an AJAX request to Flask application
      const url = 'http://localhost:8000/api/LoginSuperUser'; //The localhost port I have Flask running on

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
          console.log('login token: ', token) //Display token after recieved
          //Make cookies expire after 7 days
          const expirationDate = new Date();
          expirationDate.setDate(expirationDate.getDate() + 7);

          //Store the token in a secure manner (e.g., HttpOnly cookie) with expiration date
          Cookies.set('super_token', token, { secure: false, expires: expirationDate });
          Cookies.set('login_token', token, { secure: false, expires: expirationDate });
          //console.log('Login token:', token) //Display token after cookies set
          console.log('User logged in successfully, login token: ', token)
          this.checkLoginStatus();
          this.toast.message = 'Login successful!'; // Replace with actual login logic
          this.toast.color = 'success';
          this.toast.show = true;

          this.showSnackbar = true; // Show the Snackbar
          setTimeout(() => {
            this.$router.push({ name: 'SuperuserDashboard' });
          }, 1000);

          // Redirect to the home page
          // this.$router.push({ name: 'Home' });

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
      } catch (error) {
        console.error('Error checking login status', error);
        this.isLoggedIn = false;
      }
    },

  }
};

</script>

<style>
.login-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #FFF; /* Light background color */
  color: black; /* Dark text color */
}

.login-form {
  max-width: 400px;
  width: 100%;
  padding: 20px;
  border-radius: 5px;
  background-color: #FFF; /* Light background color */
  text-align: center;
}

.form-title {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.form-title v-icon {
  margin-bottom: 10px;
}

.form-input {
  margin-bottom: 20px;
}

.form-actions {
  margin-top: 20px;
}

.error-message {
  color: red;
  margin-top: 10px;
}

.error-outline {
  border-color: red;
}

.centered-text {
  display: block;
  text-align: center;
  font-size: medium;
}
</style>
