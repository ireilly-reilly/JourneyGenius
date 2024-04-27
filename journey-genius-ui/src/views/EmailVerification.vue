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
                
                <div class="text-container">
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
                          <!-- <v-progress-circular
                            indeterminate
                            size="20"
                            color="deep-purple-accent-1"
                          ></v-progress-circular> -->
                        </template>
                      </v-btn>
                      
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
                      
                      <!-- Dialog for confirming individual user trip delete-->
        <v-dialog v-model="emailNotVerified" max-width="650">
            <v-card>
                <v-card-title class="headline"
                    style="padding-left: 25px; padding-top: 15px;">Email Not Verified</v-card-title>
                <v-card-text>
                    Check your email for a verification link to access your account.
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="deep-purple-accent-2" text @click="emailNotVerified = false">Close</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
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
import axios from 'axios';
import Cookies from 'js-cookie'

  export default {
    data() {
      return {
        verificationComplete: false,
        emailNotVerified: false,
        resendTimer: 0,
        resendDisabled: false,
        email: '',
        token: '',
      };
    },
    mounted(){
      this.verifyAndStartResendTimer();
    },
    methods: {
      verifyAndStartResendTimer() {
        const token = Cookies.get('login_token');

        


        setTimeout(() => {
          
          this.verificationComplete = true;
  
          // Start the resend timer
          this.startResendTimer();
        }, );
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
        const token = Cookies.get('login_token');


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
        const { email } = this.$route.params;
        axios.post(`http://localhost:8000/api/auth/resend_verification_email/${email}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then(response => {
                console.log('User email verified successfully:', response.data);
                
            })
            .catch(error => {
                console.error('Error fetching user info:', error);
                // Show an error message or handle the error
            });
  
        // Simulate sending a new verification email
        // Replace the following setTimeout with your actual email sending logic
        setTimeout(() => {
          // ... (your email sending logic)
        }, 2000);
      },
      async returnToSite() {
  const { email } = this.$route.params;

  try {
    const response = await axios.get(`http://localhost:8000/api/auth/check_verification/${email}`);
    
    this.verificationComplete = true;
    // Email is verified, navigate to the home page
    this.$router.push({ path: '/' });
  } catch (error) {
    if (error.response && error.response.status === 401) {
      this.emailNotVerified = true;
    } else {
      console.log('Error checking email verification', error);
    }
  }
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
  