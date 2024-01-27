<template>
    <div style="max-width: 1200px;"> 
    <!-- Header -->
    <v-row justify="center" class="mt-4">
        <v-col cols="12" md="8" class="text-center">
            <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">
                Plan Your Next Adventure
            </h2>
            <p style="font-size: 0.75rem;" class="headline text-deep-purple-accent-2">
                Planned for February 13 - February 15. High budget, traveling with friends.
            </p>
            <p style="margin-top: 10px;">
                Explore these additional activities you can do while on your stay. Your chosen
                options will be featured in your customized Vacation Overview. Once you've made
                your selections, click the "Go Back" button to complete the remaining user inputs.
            </p>
            <br />
            <hr />
        </v-col>
    </v-row>

    <!-- Category: Choose the Activities that Peak Your Interest -->
    <v-row justify="center" class="mt-4">
        <v-col cols="12" md="8">
            <h3 class="headline text-deep-purple-accent-2">Choose the Activities that Peak Your Interest</h3>
            <br>
            <v-row>
                <v-col v-for="(activity, index) in activities" :key="index" cols="12">
                    <v-checkbox v-model="selectedActivities[index]" :label="activity" class="mb-1"></v-checkbox>
                </v-col>
            </v-row>
            <v-col class="d-flex justify-center">
                <router-link to="/Itinerary">
                    <v-btn @click="redirectToMoreActivitiesPage" color="deep-purple-accent-2">Go Back</v-btn>
                </router-link>
            </v-col>
        </v-col>
    </v-row>
    </div>
</template>

<script>
export default {
    data() {
        return {
            activities: [
                'Biking Across the Golden Gate Bridge: Rent a bike and pedal across the iconic Golden Gate Bridge. Once on the other side, explore the trails in the Marin Headlands for stunning views of the bridge and the city.',
                'Land\'s End Trail: Hike the Land\'s End Trail for breathtaking views of the Pacific Ocean, the Golden Gate Bridge, and the Marin Headlands. Don\'t miss the historic Sutro Baths and the labyrinth along the way.',
                'Kayaking on the Bay: Rent a kayak and paddle around the San Francisco Bay. You can get unique views of the city skyline and might even spot some sea lions near Pier 39.',
                'Sailing on the Bay: Charter a sailboat or join a sailing tour to experience the beauty of San Francisco from the water.',
                'Explore Golden Gate Park: Spend a day exploring Golden Gate Park, home to attractions like the California Academy of Sciences, the de Young Museum, and the Japanese Tea Garden.',
                'Visit San Francisco Zoo: Enjoy a day at the San Francisco Zoo, home to a diverse collection of animals from around the world. Don\'t miss the interactive exhibits and feeding sessions.',
                'Take a Ferry to Angel Island: Hop on a ferry to Angel Island State Park for panoramic views of the bay and the city. Explore hiking trails and historical sites on the island.',
                'Museum-Hopping in SoMa: Explore the museums in the South of Market (SoMa) district, including the San Francisco Museum of Modern Art (SFMOMA) and the Contemporary Jewish Museum.',
                'Attend a Broadway Show: Catch a Broadway-style show in San Francisco\'s Theater District. The Orpheum Theatre and the Golden Gate Theatre host a variety of performances.',
                'Climb Twin Peaks: Hike or drive to the top of Twin Peaks for breathtaking panoramic views of San Francisco and the surrounding Bay Area.',
                'Picnic at Dolores Park: Enjoy a leisurely afternoon at Dolores Park, a popular spot for picnics, sunbathing, and people-watching in the Mission District.',
                'Take a Historic Streetcar Ride: Experience a ride on one of San Francisco\'s historic streetcars along the Embarcadero. Choose from different vintage streetcar lines.',
            ],

            selectedActivities: [],
        };
    },
    methods: {
        redirectToMoreActivitiesPage() {
            // Add your navigation logic here
            console.log('Navigating to more activities page');
        },
    },
};
</script>

<style></style>