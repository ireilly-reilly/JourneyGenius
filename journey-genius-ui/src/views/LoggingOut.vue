<template>
    <v-app>
      <v-container fluid fill-height>
        <v-row align="center" justify="center">
          <v-col
            :xs="12"
            :sm="8"
            :md="6"
            :lg="4"
            :xl="3"
            class="text-center"
          >
            <h1 class="headline">Logging out</h1>
            <br>
            <v-progress-circular
              v-if="loading"
              :size="loadingCircleSize"
              indeterminate
              color="deep-purple-accent-2"
            ></v-progress-circular>
            <br>
            <br>
            <div v-if="loading" :style="{ fontSize: loadingTextSize }" class="caption mt-2">
              You will be redirected shortly.
            </div>
            <v-btn
              v-else
              @click="logout"
              color="deep-purple-accent-2"
            >
              Logout
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-app>
  </template>
  
  <script>
  export default {
    mounted() {
      setTimeout(() => {
        this.$router.push({ name: 'Home' });
      }, 2000); // 3000 milliseconds = 3 seconds
    },
    data() {
      return {
        loading: true,
        loadingCircleSize: 50, // Adjust this size based on your needs
        loadingTextSize: "1rem", // Adjust this size based on your needs
      };
    },
    methods: {
      logout() {
        console.log('Logging out...');
        // Implement your logout logic here
        // Redirect or perform other actions after logout
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles if needed */
  </style>
  