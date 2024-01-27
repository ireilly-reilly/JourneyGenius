<template>
    <v-card>
      <v-card-title class="headline">{{ label }}</v-card-title>
      <v-card-text>
        <v-date-picker v-model="selectedDate" no-title></v-date-picker>
      </v-card-text>
    </v-card>
  </template>
  
  <script>
  export default {
    props: {
      label: String,
    },
    data() {
      return {
        selectedDate: null,
      };
    },
  };
  </script>
  