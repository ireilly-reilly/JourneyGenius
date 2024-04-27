<template>
    <v-layout align-center justify-center>
        <v-row align="center" justify="center" class="my-3" v-if="!isLoggedIn">
        <v-col cols="12" md="10" lg="8" class="text-center">
          <h1 class="display-1 font-weight-black">
            Hey! This destination is reserved for VIP travelers only.
          </h1>
          <h2 class="display-1 font-weight-black mb-2">
            <span class="text-deep-purple-accent-2"> Keep exploring the world with us elsewhere!</span>
          </h2>
          <!-- Additional smaller text -->
          <!-- <h3 class="subtitle-1 text-grey-darken-2">
            This application serves as your dedicated travel curator, crafting distinctive itineraries
          </h3>
          <h3 class="subtitle-1 text-grey-darken-2">
            tailored to your interests and budget.
          </h3> -->
          </v-col>
        </v-row>
    <div>
      <v-row justify="center" style="height: 100vh; align-content: center;">
       
        
      </v-row>
    </div>
  </v-layout>
  
  </template>
  
  <script>
  export default {
    props: {
      isLoading: Boolean,
      progress: Number
    }
  };
  </script>
  
  <style>
  .loading-screen {
    display: flex;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    justify-content: center;
    align-items: center;
    z-index: 9999;
  }
  
  .loading-spinner {
    border: 4px solid #f3f3f3;
    border-top: 4px solid #7c4dff;
    border-radius: 50%;
    width: 80px;
    height: 80px;
    animation: spin 1s linear infinite;
    /* display: inline-block; Remove inline-block */
    text-align: center;
    /* align-items: center; justify-content: center; Remove these */
    display: flex; /* Add this */
    align-items: center; /* Add this */
    justify-content: center; /* Add this */
    margin-top: 15px;
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
  
  
  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  
  .loading-text {
    color: #f3f3f3;
    margin-bottom: 40px;
    align-content: center;
    font-size: 40px;
  }
  
  .loading-text2 {
    color: #f3f3f3;
    /* margin-top: 15px; */
    font-size: 25px;
    align-content: center;
    margin-bottom: 60px;
  }
  </style>
  