<template>
    <!-- Header -->
    <v-row justify="center" class="mt-4">
        <v-col cols="12" md="8" class="text-center">
            <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">
                Explore More Landmarks
            </h2>
            <p style="font-size: 0.75rem;" class="headline text-deep-purple-accent-2">
                Planned for February 13 - February 15. High budget, traveling with friends.
            </p>
            <p style="margin-top: 10px;">
                Explore these additional iconic landmarks and photo opportunities. Your chosen options will be featured in
                your customized Vacation Overview. Once you've made your selections, click the "Go Back" button to complete
                the remaining user inputs.
            </p>
            <br />
            <hr />
        </v-col>
    </v-row>

    <!-- Category: Choose the Landmarks -->
    <v-row justify="center" class="mt-4">
        <v-col cols="12" md="8">
            <h3 class="headline text-deep-purple-accent-2">Choose More Landmarks</h3>
            <br>
            <v-row>
                <v-col v-for="(landmark, index) in landmarks" :key="index" cols="12">
                    <v-checkbox v-model="selectedLandmarks[index]" :label="landmark" class="mb-1"></v-checkbox>
                </v-col>
            </v-row>
            <v-col class="d-flex justify-center">
                <router-link to="/Itinerary">
                    <v-btn @click="redirectToItinerary" color="deep-purple-accent-2">Go Back</v-btn>
                </router-link>
            </v-col>
        </v-col>
    </v-row>
</template>
  
<script>
export default {
    data() {
        return {
            landmarks: [
                'Golden Gate Bridge: An absolute classic, the Golden Gate Bridge is one of the most recognizable landmarks in the world. Head to viewpoints like Battery Spencer or the Golden Gate Overlook for breathtaking shots.',
                'Alcatraz Island: Capture the eerie beauty of the abandoned Alcatraz prison from various angles. Take a ferry to the island for a unique perspective of the city skyline.',
                'Lombard Street: Known as the "Crookedest Street in the World," Lombard Street\'s winding turns make for a quirky and photogenic scene.',
                'Chinatown: Explore the vibrant and historic Chinatown, known for its unique shops, markets, and delicious restaurants.',
                'Painted Ladies: Visit Alamo Square to see the famous row of Victorian houses known as the Painted Ladies, with the city skyline in the background.',
                'Chinatown Gate: The Dragon Gate at the entrance to Chinatown is a colorful and iconic landmark. Explore the vibrant streets within for additional photo opportunities.',
                'Fisherman\'s Wharf: Experience the lively atmosphere at Fisherman\'s Wharf, where you can enjoy seafood, visit Pier 39 with its sea lions, and explore the Muse Mecanique, a vintage arcade.',
                'San Francisco Cable Cars: Ride the historic cable cars, an iconic symbol of San Francisco. The Powell-Mason and Powell-Hyde lines provide scenic routes with city views.',
                'Japanese Tea Garden: Located within Golden Gate Park, the Japanese Tea Garden is a peaceful oasis featuring traditional Japanese architecture, serene ponds, and beautiful flora.',
                'Muir Woods National Monument: Just north of the city, Muir Woods is home to towering redwood trees, creating a magical forest environment that\'s perfect for a day trip.',
            ],
            selectedLandmarks: [],
        };
    },
    methods: {
        redirectToItinerary() {
            // Add your navigation logic here
            console.log('Navigating to the Itinerary page');
        },
    },
};
</script>
  
<style>
/* Your component's styles */
</style>
  