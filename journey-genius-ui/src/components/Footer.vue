<template>
    <v-footer class="bg-grey-lighten-1">
      <v-row justify="center" no-gutters>
        <router-link
          v-for="link in links"
          :key="link.text"
          :to="link.to"
        >
          <v-btn
            color="white"
            variant="text"
            class="mx-2"
            rounded="xl"
          >
            {{ link.text }}
          </v-btn>
        </router-link>
        <v-col class="text-center mt-4" cols="12">
          {{ new Date().getFullYear() }} — <strong>Journey Genius</strong>
          <!-- <strong>Journey Genius - It's not about the destination, it's about the journey.</strong> -->
        </v-col>
      </v-row>
    </v-footer>
  </template>
  
  <script>
  export default {
    data: () => ({
      // links: [
      //   { text: 'Home', to: '/' },
      //   { text: 'User Profiling', to: '/UserProfiling' },
      //   { text: 'Plan Trip', to: '/StartPlanning' },
      //   { text: 'Saved Trips', to: '/SavedTrips' },
      // ],
    }),
  };
  </script>
  