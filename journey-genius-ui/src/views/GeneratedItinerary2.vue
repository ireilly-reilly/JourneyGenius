<template>
    <v-container fluid class="no-border">
      <v-row>
        <v-col v-for="(day, index) in itinerary" :key="index" cols="12">
          <v-card class="activity-card" style="display: flex; flex-direction: column; height: 100%;">
            <v-card-title :class="['headline', fontSizeClass(index)]">
              <v-icon v-if="timelineIcon(index)" :class="['mr-2', iconColorClass(index)]">
                {{ timelineIcon(index) }}
              </v-icon>
              {{ day.title }}
            </v-card-title>
            <br>
            <br>
            <br>
            <v-row style="flex: 1;">
              <v-col v-for="(activity, activityIndex) in day.activities" :key="activityIndex" cols="12" md="4">
                <v-card class="activity-box" style="flex: 1;">
                  <!-- Set a fixed height for the images -->
                  <v-img :src="activity.image" alt="Activity Image" class="activity-img-with-border" style="object-fit: cover; width: 100%; height: 100%;"></v-img>
                  <v-card-title>{{ activity.name }}</v-card-title>
                  <v-card-text class="description-height">{{ activity.description }}</v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    
    
        <!-- Two buttons on the bottom -->
        <v-row justify="center" class="mt-4">
            <v-col cols="12" md="8" class="text-center">
                <router-link to="/GeneratedItinerary">
                    <v-btn color="deep-purple-accent-2" class="white--text mt-6 mr-2" @click="previousStep"
                        style="min-width: 150px;">
                        Go Back
                    </v-btn>
                </router-link>
    
                <router-link to="/SavedTrips">
                    <v-btn color="deep-purple-accent-2" class="white--text mt-6 ml-2" style="min-width: 150px;">
                        Save Trip
                    </v-btn>
                </router-link>
            </v-col>
        </v-row>
    </template>
      
    <script>
    import axios from 'axios';
    export default {
        data() {
            return {
                itinerary: [
                    {
                        title: 'Day 1 - Tuesday, December 13',
                        activities: [
                            {
                                name: 'Check into your Hotel',
                                description: 'You\'ve selected Hotel Nikko San Francisco at 222 Mason St, San Francisco, CA 94102, USA. Head to your hotel to check in and settle in comfortably!',
                                image: require('@/assets/hotel.jpeg'),
                            },
                            {
                                name: 'Golden State Bridge',
                                description: 'An absolute classic, the Golden Gate Bridge is one of the most recognizable landmarks in the world. Head to viewpoints like Battery Spencer or the Golden Gate Overlook for breathtaking shots.',
                                image: require('@/assets/goldenstatebridge2.jpeg'),
                            },
                            {
                                name: 'Lunch at Local Restaurant',
                                description: 'Swan Oyster Depot (1517 Polk St) - A historic seafood counter that serves fresh and delicious seafood. It\'s a popular spot,so be prepared for a wait.',
                                image: require('@/assets/swanOyster.jpeg'),
                            },
                        ],
                    },
                    {
                        title: 'Day 2 - Wednesday, February 14',
                        activities: [
                            {
                                name: 'Botanical Garden at Strybing Arboretum',
                                description: 'Located in Golden Gate Park, this garden showcases a wide variety of plants from around the world in a beautifully landscaped setting.',
                                image: require('@/assets/garden.jpeg'),
                            },
                            {
                                name: 'Tea Hut (280 Golden Gate Ave)',
                                description: 'A Chinatown favorite, Tea Hut serves a variety of teas, including boba, fruit teas, and slushies.',
                                image: require('@/assets/boba2.jpeg'),
                            },
                            {
                                name: 'Union Square',
                                description: 'Known as the city\'s premier shopping destination, Union Square is home to flagship stores of major brands such as Macy\'s, Saks Fifth Avenue, Neiman Marcus, and Apple. You\'ll also find a variety of luxury boutiques and department stores in the surrounding area.',
                                image: require('@/assets/unionsquare2.jpeg'),
                            },
                            {
                                name: 'Fisherman\'s Wharf',
                                description: 'This popular tourist destination offers a mix of souvenir shops, specialty stores, and waterfront markets. It\'s a lively area with a variety of shopping options.',
                                image: require('@/assets/wharf2.jpeg'),
                            },
                            {
                                name: 'Ghirardelli Square (900 North Point St)',
                                description: 'While primarily known for its chocolate shops, Ghirardelli Square also houses boutique stores, galleries, and restaurants. It\'s a great place to shop while enjoying views of the bay.',
                                image: require('@/assets/gs.jpeg'),
                            },
                            {
                                name: 'Sailing on the Bay',
                                description: 'Charter a sailboat or join a sailing tour to experience the beauty of San Francisco from the water.',
                                image: require('@/assets/ferry.jpeg'),
                            }
    
                        ],
                    },
                    {
                        title: 'Day 3 - Thursday, February 15',
                        activities: [
                            {
                                name: 'Haight-Ashbury',
                                description: 'If you\'re into vintage and alternative fashion, head to Haight-Ashbury. This historic neighborhood is known for its eclectic mix of shops, including vintage clothing stores and quirky boutiques.',
                                image: require('@/assets/HaightAshbury.jpeg'),
                            },
                            {
                                name: 'Hiking in the Marin Headlands',
                                description: 'Explore the network of hiking trails in the Marin Headlands for stunning views of the Golden Gate Bridge, the Pacif ic Ocean, and the San Francisco skyline.',
                                image: require('@/assets/MarinHeadlands.jpg'),
                            },
                            {
                                name: 'Beach Day at Ocean Beach',
                                description: 'Enjoy a day at Ocean Beach, located on the western edge of the city. It\'s a great spot for a beach walk, picnics, and watching the sunset over the Pacific.',
                                image: require('@/assets/sfbeach.jpeg'),
                            },
                            {
                                name: 'Rich Table (199 Gough St)',
                                description: 'A Michelin-starred restaurant that offers creative and seasonal dishes in a relaxed and inviting setting.',
                                image: require('@/assets/food.jpeg'),
                            },
                            {
                                name: 'Flight Back Home',
                                description: 'Enjoy a smooth transition from the vibrant cityscape to the comfort of air travel as you drive to San Francisco International Airport (SFO), winding through iconic streets before arriving at the modern terminals for your journey home.',
                                image: require('@/assets/sfo2.jpeg'),
                            }
                        ],
                    }
    
                    // Add more days as needed
                ],
            };
        },
        methods: {
            getTimelineColor(index) {
                // Define colors for each day
                const colors = ['primary', 'info', 'success', 'error', 'warning'];
                return colors[index % colors.length];
            },
            getTimelineIcon(index) {
                // Define icons for each day
                const icons = ['mdi-hiking', 'mdi-map-marker', 'mdi-spa', 'mdi-food', 'mdi-coffee'];
                return icons[index % icons.length];
            },
        },
        computed: {
            fontSizeClass() {
                return (index) => {
                    // Define font sizes for each day
                    const fontSizes = ['text-h4', 'text-h4', 'text-h4']; // Adjust sizes as needed
                    return fontSizes[index % fontSizes.length];
                };
            },
            iconColorClass() {
                return (index) => {
                    // Define icon colors for each day
                    const colors = ['primary', 'info', 'success', 'error', 'warning'];
                    return colors[index % colors.length];
                };
            },
            timelineIcon() {
                return (index) => {
                    // Define icons for each day
                    const icons = ['mdi-hiking', 'mdi-map-marker', 'mdi-spa', 'mdi-food', 'mdi-coffee'];
                    return icons[index % icons.length];
                };
            }
        }
    };
    </script>
      
    
    <style scoped>
     .description-height {
        height: 100px; /* Set a fixed height for the descriptions */
        overflow: hidden; /* Hide overflow content if the description is longer */
        display: -webkit-box;
        -webkit-line-clamp: 3; /* Limit the number of lines to show */
        -webkit-box-orient: vertical;
      }
    
      .activity-img-with-border {
      border: 1px solid #ddd; /* Add a border for visual separation */
    }
    
    /* Additional styling for responsiveness, if needed */
    @media (max-width: 600px) {
    }
    </style>