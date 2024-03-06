<template>
    <v-app>
      <v-container fluid fill-height>
        <v-row align="center" justify="center" class="fill-height">
          <v-col class="text-center">
            <v-card width="100%" max-width="700" class="mx-auto">
              <v-row align="center">
                <v-col>
                  <br />
                  <v-avatar color="deep-purple-accent-2" size="80">
                    <v-icon color="deep-purple-accent-1" size="58">mdi-email</v-icon>
                  </v-avatar>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-card-title>
                    <h1 class="headline">Verify your email address</h1>
                  </v-card-title>
                </v-col>
              </v-row>
              <v-card-text>
                <div v-if="!verificationComplete" class="text-container">
                  <p class="caption">
                    Please confirm that you want to use this as your Journey Genius account email address. Once it's done, you will be able to start planning!
                  </p>
                  <br />
                  <v-btn
                    rounded="lg"
                    @click="verifyAndStartResendTimer"
                    color="deep-purple-accent-2"
                    class="mt-2 mr-2"
                    size="large"
                  >
                    Verify Email
                  </v-btn>
                </div>
                <div v-else class="text-container">
                  <p class="caption">
                    We have sent a verification link to your email. Click on the link to complete the verification process.
                  </p>
                  <br />
                  <v-row justify="center">
                    <v-col>
                      <v-btn
                        rounded="lg"
                        @click="resendEmail"
                        color="deep-purple-accent-2"
                        :disabled="resendDisabled"
                        class="mt-2"
                        size="large"
                      >
                        <template v-if="!resendTimer">
                          Resend Email
                        </template>
                        <template v-else>
                          Resend in {{ resendTimer }}s
                          <v-progress-circular
                            indeterminate
                            size="20"
                            color="deep-purple-accent-1"
                          ></v-progress-circular>
                        </template>
                      </v-btn>
                      <router-link to="/">
                        <v-btn
                          variant="text"
                          @click="returnToSite"
                          color="deep-purple-accent-2"
                          class="mt-2"
                          size="large"
                          append-icon="mdi-arrow-right"
                        >
                          Return to Site
                        </v-btn>
                      </router-link>
                    </v-col>
                  </v-row>
                </div>
                <br />
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-app>
  </template>
  
  <script>
  export default {
    data() {
      return {
        verificationComplete: false,
        resendTimer: 0,
        resendDisabled: false,
      };
    },
    methods: {
      verifyAndStartResendTimer() {
        // Simulate the email verification process
        setTimeout(() => {
          this.verificationComplete = true;
  
          // Start the resend timer
          this.startResendTimer();
        }, 2000);
      },
      startResendTimer() {
        this.resendDisabled = true;
        this.resendTimer = 60;
        const countdownInterval = setInterval(() => {
          if (this.resendTimer > 0) {
            this.resendTimer--;
          } else {
            this.resendDisabled = false;
            clearInterval(countdownInterval);
          }
        }, 1000);
  
        // Simulate sending a new verification email
        // Replace the following setTimeout with your actual email sending logic
        setTimeout(() => {
          // ... (your email sending logic)
        }, 2000);
      },
      resendEmail() {
        this.resendDisabled = true;
        this.resendTimer = 60;
        const countdownInterval = setInterval(() => {
          if (this.resendTimer > 0) {
            this.resendTimer--;
          } else {
            this.resendDisabled = false;
            clearInterval(countdownInterval);
          }
        }, 1000);
  
        // Simulate sending a new verification email
        // Replace the following setTimeout with your actual email sending logic
        setTimeout(() => {
          // ... (your email sending logic)
        }, 2000);
      },
      returnToSite() {
        // Add logic for returning to the site
      },
    },
  };
  </script>
  
  <style scoped>
  .text-container {
    max-width: 400px;
    margin: 0 auto;
  }
  </style>
  