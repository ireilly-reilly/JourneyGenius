<template>
  <v-app>
    <component :is="layoutComponent">
      <NavBar/>
      <v-content class="mx-15 mb-15 mt-5">
        <router-view></router-view>
      </v-content>
      <Footer/>
    </component>
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar'
import Footer from '@/components/Footer'
import LoadingScreen from '@/components/LoadingScreen'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import SuperuserLayout from '@/layouts/SuperuserLayout.vue'

export default {
  name: 'App',
  components: { NavBar, Footer, LoadingScreen, DefaultLayout, SuperuserLayout },
  computed: {
    layoutComponent() {
      // Use DefaultLayout by default
      let layout = DefaultLayout;

      // Check if the route has a meta field and layout specified
      if (this.$route.meta && this.$route.meta.layout) {
        if (this.$route.meta.layout === 'SuperuserLayout') {
          layout = SuperuserLayout;
        }
      }

      return layout;
    },
  },
}
</script>
