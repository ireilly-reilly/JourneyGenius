<template>
<v-app>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="8">
          <v-card>
            <v-card-title class="headline">How to Use Journey Genius</v-card-title>
            <v-card-text>
              <v-stepper v-model="step">
                <v-stepper-header>
                  <v-stepper-step :complete="step > 1" step="1">Step 1</v-stepper-step>
                  <v-divider></v-divider>
                  <v-stepper-step :complete="step > 2" step="2">Step 2</v-stepper-step>
                  <v-divider></v-divider>
                  <v-stepper-step :complete="step > 3" step="3">Step 3</v-stepper-step>
                  <v-divider></v-divider>
                  <v-stepper-step :complete="step > 4" step="4">Step 4</v-stepper-step>
                  <v-divider></v-divider>
                  <v-stepper-step :complete="step > 5" step="5">Step 5</v-stepper-step>
                </v-stepper-header>

                <v-stepper-items>
                  <v-stepper-content step="1">
                    <v-card>
                      <v-card-title>Step 1: Fill out Trip Preferences</v-card-title>
                      <v-card-text>
                        <p>On this page, provide your interests, such as adventure, culture, or relaxation. These preferences will be used to tailor your trip options.</p>
                      </v-card-text>
                    </v-card>
                  </v-stepper-content>

                  <v-stepper-content step="2">
                    <v-card>
                      <v-card-title>Step 2: Customize Trip Settings</v-card-title>
                      <v-card-text>
                        <p>Choose the number of options you want Journey Genius to generate and format them. This customization will affect loading times.</p>
                      </v-card-text>
                    </v-card>
                  </v-stepper-content>

                  <v-stepper-content step="3">
                    <v-card>
                      <v-card-title>Step 3: Enter Travel Details</v-card-title>
                      <v-card-text>
                        <p>Specify your destination, travel dates, and budget. This information will be used to tailor your trip recommendations.</p>
                      </v-card-text>
                    </v-card>
                  </v-stepper-content>

                  <v-stepper-content step="4">
                    <v-card>
                      <v-card-title>Step 4: Select Interests</v-card-title>
                      <v-card-text>
                        <p>Choose activities, landmarks, foods, shopping spots, and hotels that interest you. This will refine your trip options.</p>
                      </v-card-text>
                    </v-card>
                  </v-stepper-content>

                  <v-stepper-content step="5">
                    <v-card>
                      <v-card-title>Step 5: Enjoy Your Trip Overview</v-card-title>
                      <v-card-text>
                        <p>Explore your personalized trip overview and day-to-day itinerary. Save and customize features are available for your convenience.</p>
                      </v-card-text>
                    </v-card>
                  </v-stepper-content>
                </v-stepper-items>
              </v-stepper>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>