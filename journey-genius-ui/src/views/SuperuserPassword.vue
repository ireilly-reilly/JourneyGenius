<template>
    <div class="password-page dark-mode">
      <div class="lock-icon">
        <v-icon size="100" color="white">mdi-lock</v-icon>
      </div>
      <div class="password-input">
        <v-text-field
          v-model="password"
          :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          :type="showPassword ? 'text' : 'password'"
          @click:append="showPassword = !showPassword"
          label="Password"
          outlined
          color="white"
        ></v-text-field>
      </div>
      <div class="submit-button">
        <v-btn @click="submitPassword" color="deep-purple-accent-2">Submit</v-btn>
      </div>
      <v-snackbar v-model="toast.show" :timeout="toast.timeout" color="deep-purple-accent-2" class="snackbar">
        {{ toast.message }}
      </v-snackbar>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        password: '',
        showPassword: false,
        toast: {
          show: false,
          message: '',
          timeout: 2000,
          color: 'error', // Change color to 'success' or any other Vuetify color class for different styles
        },
      };
    },
    methods: {
      submitPassword() {
        // Check if the password is correct
        if (this.password === 'your_superuser_password') {
          // Redirect to the superuser page
          this.$router.push({ name: 'SuperuserLogin' });
        } else {
          // Display an error message as a toast
          this.toast.message = 'Incorrect password. Please try again.';
          this.toast.show = true;
        }
      },
    },
  };
  </script>
  
  <style>
  .password-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #333; /* Dark background color */
    color: white; /* Light text color */
  }
  
  .lock-icon {
    margin-bottom: 20px;
  }
  
  .password-input {
    width: 300px;
  }
  
  .submit-button {
    margin-top: 20px;
  }
  
  .snackbar {
  display: flex;
  align-items: center;
  justify-content: center;
}

  </style>
  