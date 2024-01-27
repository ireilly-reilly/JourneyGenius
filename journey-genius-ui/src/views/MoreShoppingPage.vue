<template>
    <!-- Header -->
    <v-row justify="center" class="mt-4">
        <v-col cols="12" md="8" class="text-center">
            <h2 style="font-size: 2.5rem;" class="headline text-deep-purple-accent-2">
                Explore Shopping Options
            </h2>
            <p style="font-size: 0.75rem;" class="headline text-deep-purple-accent-2">
                Planned for February 13 - February 15. High budget, traveling with friends.
            </p>
            <p style="margin-top: 10px;">
                Explore a variety of shopping destinations in San Francisco. Your chosen selections will be
                incorporated into your personalized Vacation Overview. Click the "Go Back" button when
                you're prepared to move on to the next step.
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
                <v-col v-for="(food, index) in shoppingOptions" :key="index" cols="12">
                    <v-checkbox v-model="selectedShoppingOptions[index]" :label="food" class="mb-1"></v-checkbox>
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
            shoppingOptions: [
                'Union Square: Known as the city\'s premier shopping destination, Union Square is home to flagship stores of major brands such as Macy\'s, Saks Fifth Avenue, Neiman Marcus, and Apple. You\'ll also find a variety of luxury boutiques and department stores in the surrounding area.',
                'Westfield San Francisco Centre (865 Market St): This large shopping mall in the heart of downtown features a mix of high-end and mainstream retailers, including Bloomingdale\'s, Nordstrom, and a variety of other shops.',
                'Ghirardelli Square (900 North Point St): While primarily known for its chocolate shops, Ghirardelli Square also houses boutique stores, galleries, and restaurants. It\'s a great place to shop while enjoying views of the bay.',
                'Valencia Street (Mission District): Valencia Street in the Mission District is known for its hip and eclectic shops, including vintage stores, bookshops, and unique boutiques.',
                'Embarcadero Center (4 Embarcadero Center): This waterfront shopping complex offers stunning views of the Bay Bridge. Explore a mix of shops, restaurants, and entertainment options.',
                'Chestnut Street (Marina District): A charming street in the Marina District, Chestnut Street is lined with boutique shops, cafes, and restaurants. It\'s a great place for leisurely strolls and unique finds.',
                'Ferry Building Marketplace (1 Ferry Building): Located along the Embarcadero, the Ferry Building houses a marketplace with a diverse selection of gourmet shops, artisanal products, and restaurants.',
                'Haight-Ashbury: Known for its bohemian and counterculture history, Haight-Ashbury offers a mix of vintage clothing stores, record shops, and unique boutiques.',
                'Stonestown Galleria (3251 20th Ave): Situated near San Francisco State University, Stonestown Galleria features a range of shops, including apparel, home goods, and eateries.',
                // Add more shopping options here
            ],

            selectedShoppingOptions: [],
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
  