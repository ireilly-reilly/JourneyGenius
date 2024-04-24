<template>
    <v-container>
      <v-card class="mx-auto pa-5" max-width="500">
        <v-card-title class="text-center text-h5">
          User Information
        </v-card-title>
        <br>
        <v-card-text>
          <v-form>
            <v-text-field
              v-model="user.firstName"
              :readonly="!editInfo"
              label="First Name"
              prepend-icon="mdi-account"
              :class="{'v-input--is-focused': editInfo}"
            ></v-text-field>
            <v-text-field
              v-model="user.lastName"
              :readonly="!editInfo"
              label="Last Name"
              prepend-icon="mdi-account"
              :class="{'v-input--is-focused': editInfo}"
            ></v-text-field>
            <v-text-field
              v-model="user.email"
              :readonly="!editInfo"
              label="Email"
              prepend-icon="mdi-email"
              :class="{'v-input--is-focused': editInfo}"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions class="justify-center">
          <v-btn icon @click="editInfo = !editInfo">
            <v-icon color="deep-purple-accent-2">{{ editInfo ? 'mdi-close' : 'mdi-pencil' }}</v-icon>
            <span :class="{'ml-3': !editInfo}">{{ editInfo ? '' : 'Edit' }}</span>
          </v-btn>
          <v-btn
            v-if="editInfo"
            color="deep-purple accent-2"
            @click="confirmChanges"
            dark
          >
            Confirm Changes
          </v-btn>
          <v-btn
            v-if="editInfo"
            color="red"
            @click="resetPassword"
            dark
          >
            Reset Password
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </template>
  
  <script>
  export default {
    data: () => ({
      editInfo: false,
      user: {
        firstName: "John",
        lastName: "Doe",
        email: "john.doe@example.com",
      },
    }),
    methods: {
      confirmChanges() {
        this.editInfo = false;
        console.log("Changes confirmed:", this.user);
        // Add code here to handle the actual update logic, such as API calls
      },
      resetPassword() {
        // Implement logic to handle password reset, e.g., showing a modal to enter a new password
        console.log("Password reset requested");
      },
    },
  };
  </script>
  
  <style scoped>
  .v-input--is-focused .v-input__control .v-input__slot {
    border-bottom: 2px solid var(--v-deep-purple-accent-2-base);
    outline: none !important;
  }
  </style>
