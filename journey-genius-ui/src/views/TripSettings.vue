<template>
    <v-container>
        <!-- Header -->
        <v-row justify="center" class="mt-4">
            <v-col cols="12" md="8" class="text-center">
                <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">Trip Settings</h2>
                <p>Configure your trip preferences below. Adjust the settings to tailor the trip generation process to
                    your needs, optimizing the experience for your convenience and satisfaction. By selecting the number
                    of options you wish to generate, you can control the breadth of choices available. Fewer selections
                    will result in faster generation times, making the process more efficient, while more selections
                    will provide a wider range of options at the expense of increased loading times.</p>
                <br>
                <hr>
            </v-col>
        </v-row>

        <!-- Number of Selections -->
        <v-row justify="center">
            <v-col cols="12" md="8">
                <v-card class="pa-4 mb-4">
                    <h2 class="headline text-deep-purple-accent-2">How many selections?</h2>
                    <p>Choose how many options to generate. The number you select represents how many activities,
                        landmarks, restaurants, shopping options, and hotels will be generated for each category. Adjust
                        the slider below: </p>
                    <br>
                    <v-slider v-model="sliderValue" :min="5" :max="15" :step="1" :thumb-label="true"
                        class="deep-purple-accent-2" color="deep-purple-accent-2"></v-slider>
                </v-card>
            </v-col>
        </v-row>

        <!-- Description Generation Toggle -->
        <v-row justify="center">
            <v-col cols="12" md="8">
                <v-card class="pa-4 mb-4">
                    <h2 class="headline text-deep-purple-accent-2">Description Generation Toggle</h2>
                    <p>Enable this to use OpenAI to generate descriptions for the selected options. Please note that
                        these descriptions are crafted to provide a broad overview rather than detailed specifics. This
                        approach ensures that you receive a general idea of what to expect.</p>
                    <v-row align="center" justify="center" class="my-3 align-center">
                        <v-col cols="12" class="d-flex justify-center"> <!-- Using d-flex on v-col directly -->
                                <v-switch v-model="descriptionToggle" color="deep-purple-accent-2" class="centered-text"
                                    :label="`Generate Descriptions: ${descriptionToggle ? 'On' : 'Off'}`"
                                    large></v-switch>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>



        <!-- Estimated Loading Time -->
        <v-row justify="center">
            <v-col cols="12" md="8">
                <v-card class="pa-4 mb-4 justify-center">
                    <!-- Header aligned to the left -->
                    <h2 class="headline text-deep-purple-accent-2" style="text-align: left;">Estimated Loading Time</h2>
                    <p>The system calculates the expected loading time based on current settings. Enabling 'Description
                        Generation' may increase loading times due to the detailed content creation, while the number of
                        selections generally has less impact unless descriptions are being generated.</p>
                    <br>
                    <!-- Centralized button and output message layout -->
                    <v-row justify="center" align="center" no-gutters>
                        <v-col cols="12" class="text-center">
                            <v-btn size="large" color="deep-purple-accent-2" @click="estimateTime">
                                <v-icon left>mdi-timer</v-icon>
                                Generate Estimated Wait Time
                            </v-btn>
                            <!-- Display the estimated time message if it exists -->
                            <div v-if="estimatedTimeMessage" class="mt-3">
                                <h4 style="color: #7C4DFF">{{ estimatedTimeMessage }}</h4>
                            </div>
                        </v-col>
                    </v-row>
                    <br>
                </v-card>
            </v-col>
        </v-row>




        <!-- Generate button -->
        <v-row justify="center">
            <v-col cols="12" md="8" class="text-center">
                <br>
                <v-btn size="large" class="generate-btn" color="deep-purple-accent-2" @click="startPlanning">
                    Start Planning
                </v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    data() {
        return {
            sliderValue: 5, // Default slider value set to the mid-point
            descriptionToggle: false,
            estimatedTimeMessage: '', // Initially empty
            selections: '',

        };
    },
    methods: {
        estimateTime() {
            // Placeholder function for estimating time based on user selections
            this.estimatedTimeMessage = 'Estimated wait time is approximately 3 minutes.';
        },
        startPlanning() {
            this.$router.push({ name: 'StartPlanning' });
            console.log(this.sliderValue);
            console.log(this.descriptionToggle);

            this.$router.push({
                name: 'StartPlanning',
                query: {
                    amountOfSelections: JSON.stringify(this.sliderValue),
                    descriptionToggle: JSON.stringify(this.descriptionToggle),
                }


            });

        }
    },
};
</script>
