<template>
    <v-card>
      <v-card-title class="headline">Location</v-card-title>
      <v-card-text>
        <v-text-field v-model="location" label="Enter your destination" outlined></v-text-field>
      </v-card-text>
    </v-card>
  </template>
  
  <script>
  export default {
    data() {
      return {
        location: '',
      };
    },
  };
  </script>
  