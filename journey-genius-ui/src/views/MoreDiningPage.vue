<template>
    <!-- Header -->
    <v-row justify="center" class="mt-4">
        <v-col cols="12" md="8" class="text-center">
            <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">
                Explore Dining Options
            </h2>
            <p style="font-size: 0.75rem;" class="headline text-deep-purple-accent-2">
                Planned for February 13 - February 15. High budget, traveling with friends.
            </p>
            <p style="margin-top: 10px;">
                Discover diverse dining experiences in San Francisco. Your selected options will be part of your
                personalized Vacation Overview. Click the "Go Back" button when you're ready to proceed to the next step.
            </p>
            <br />
            <hr />
        </v-col>
    </v-row>

    <!-- Category: Dining Options -->
    <v-row justify="center" class="mt-4">
        <v-col cols="12" md="8">
            <h3 class="headline text-deep-purple-accent-2">Choose Your Dining Options</h3>
            <br>
            <v-row>
                <v-col v-for="(food, index) in diningOptions" :key="index" cols="12">
                    <v-checkbox v-model="selectedDiningOptions[index]" :label="food" class="mb-1"></v-checkbox>
                </v-col>
            </v-row>
            <v-col class="d-flex justify-center">
                <router-link to="/Itinerary">
                    <v-btn @click="goBack" color="deep-purple-accent-2">Go Back</v-btn>
                </router-link>
            </v-col>
        </v-col>
    </v-row>
</template>
  
<script>
export default {
    data() {
        return {
            diningOptions: [
                'Tartine Bakery (600 Guerrero St): Famous for its pastries and bread, Tartine is a beloved bakery with a cozy atmosphere.',
                'Zuni Café (1658 Market St): A San Francisco classic, Zuni Café offers a seasonal menu with a focus on local, organic ingredients. Their roasted chicken is legendary.',
                'Boba Guys (Multiple Locations): Known for their high-quality ingredients and innovative flavors, Boba Guys has multiple locations in San Francisco.',
                'Liholiho Yacht Club (871 Sutter St): A unique blend of Hawaiian and Asian flavors in a stylish and lively atmosphere.',
                'The House (1230 Grant Ave): This North Beach gem is known for its Asian fusion cuisine and cozy ambiance. Don\'t miss their famous garlic noodles.',
                'Foreign Cinema (2534 Mission St): A unique dining experience featuring eclectic American cuisine and outdoor film screenings in the courtyard.',
                'House of Prime Rib (1906 Van Ness Ave): A classic steakhouse serving prime rib in a timeless setting. Reservations are highly recommended.',
                'Mama\'s on Washington Square (1701 Stockton St): A popular breakfast spot in North Beach, Mama\'s is famous for its delicious omelets and long lines.',
                'Gary Danko (800 North Point St): Indulge in a sophisticated dining experience at Gary Danko, known for its fine dining and excellent service.',
                // Add more dining options here
            ],

            selectedDiningOptions: [],
        };
    },
    methods: {
        goBack() {
            // Add your navigation logic here
            console.log('Navigating back to the previous step');
        },
    },
};
</script>
  
<style></style>
  