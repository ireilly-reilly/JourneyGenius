<template>
    <div class="login-page dark-mode">
      <div class="login-form">
        <div class="form-title">
          <v-icon size="50" color="white">mdi-account-circle</v-icon>
          <span>Login</span>
        </div>
        <div class="form-input">
          <v-text-field v-model="email" label="Email" outlined color="white"></v-text-field>
        </div>
        <div class="form-input">
          <v-text-field v-model="password" label="Password" outlined color="white" type="password"></v-text-field>
        </div>
        <div class="form-actions">
          <v-btn @click="login" color="deep-purple-accent-2">Login</v-btn>
        </div>
      </div>
      <v-snackbar v-model="toast.show" :timeout="toast.timeout" color="deep-purple-accent-2">
        {{ toast.message }}
      </v-snackbar>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: '',
        password: '',
        toast: {
          show: false,
          message: '',
          timeout: 2000,
          color: 'error',
        },
      };
    },
    methods: {
      login() {
        // Perform login logic (e.g., send login request to server)
        // For demonstration, just show a toast message
        this.toast.message = 'Login successful!'; // Replace with actual login logic
        this.toast.color = 'success';
        this.toast.show = true;
      },
      
    },
  };
  </script>
  
  <style>
  .login-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #333; /* Dark background color */
    color: white; /* Light text color */
  }
  
  .login-form {
    max-width: 400px;
    width: 100%;
    padding: 20px;
    border-radius: 5px;
    background-color: #555;
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
  </style>
  