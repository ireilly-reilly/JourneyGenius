<template>
  <v-app>
    <NavBar/>
    <v-content class="mx-15 mb-15 mt-5">
      <router-view></router-view>
    </v-content>
    <Footer/>
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar'
import Footer from '@/components/Footer'
import LoadingScreen from '@/components/LoadingScreen';


export default {
  name: 'App',
  components: { NavBar, Footer, LoadingScreen },
  data: () => ({
    
  }),
}
</script> 
 