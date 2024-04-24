import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import UserProfiling from '../views/UserProfiling.vue'
import SavedTrips from '../views/SavedTrips.vue'
import StartPlanning from '../views/StartPlanning.vue'
import LoginPage from '../views/LoginPage.vue'
import RegisterPage from '../views/RegisterPage.vue'
import Itinerary from '../views/Itinerary.vue'
import MoreActivitiesPage from '../views/MoreActivitiesPage.vue'
import MoreLandmarksPage from '../views/MoreLandmarksPage.vue'
import MoreDiningPage from '../views/MoreDiningPage.vue'
import MoreShoppingPage from '../views/MoreShoppingPage.vue'
import Itinerary2 from '../views/Itinerary2.vue'
import GeneratedItinerary from '../views/GeneratedItinerary.vue'
import GeneratedItinerary2 from '../views/GeneratedItinerary2.vue'
import LoggingOut from "../views/LoggingOut.vue"
import EmailVerification from "../views/EmailVerification.vue"

import SuperuserPassword from '../views/SuperuserPassword.vue'
import SuperuserLogin from '../views/SuperuserLogin.vue'
import SuperuserDashboard from '../views/SuperuserDashboard.vue'
import SuperuserAccounts from '../views/SuperuserAccounts.vue'
import SuperuserAccountDetails from '../views/SuperuserAccountDetails.vue'
import SuperuserAnalytics from '../views/SuperuserAnalytics.vue'

import SavedItinerary from '../views/SavedItinerary.vue'
import SavedItinerary2 from '../views/SavedItinerary2.vue'


import DefaultLayout from '@/layouts/DefaultLayout.vue'
import SuperuserLayout from '@/layouts/SuperuserLayout.vue'



const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    {
      path: '/',
      layout: DefaultLayout,
      name: 'Home',
      component: Home,
      // meta: { layout: 'DefaultLayout' }, // Use DefaultLayout for this route
    },
    {
      path: '/loading',
      name: 'dummy',
      //component: NavBar,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    },
    {
      path: '/UserProfiling',
      name: 'UserProfiling',
      component: UserProfiling,
    },
    {
      path: '/StartPlanning',
      name: 'StartPlanning',
      component: StartPlanning,
    },
    {
      path: '/SavedTrips',
      name: 'SavedTrips',
      component: SavedTrips,
      props: true
    },
    {
      path: '/LoginPage',
      name: 'LoginPage', 
      component: LoginPage, 
    },
    {
      path: '/register',
      name: 'RegisterPage', 
      component: RegisterPage, 
    },
    {
      path: '/Itinerary',
      name: 'Itinerary',
      component: Itinerary,
    },
    {
      path: '/MoreActivitiesPage',
      name: 'MoreActivitiesPage',
      component: MoreActivitiesPage,
    },
    {
      path: '/MoreDiningPage',
      name: 'MoreDiningPage',
      component: MoreDiningPage,
    },
    {
      path: '/MoreLandmarksPage',
      name: 'MoreLandmarksPage',
      component: MoreLandmarksPage,
    },
    {
      path: '/MoreShoppingPage',
      name: 'MoreShoppingPage',
      component: MoreShoppingPage,
    },
    {
      path: '/Itinerary2',
      name: 'Itinerary2',
      component: Itinerary2,
    },
    {
      path: '/GeneratedItinerary',
      name: 'GeneratedItinerary',
      component: GeneratedItinerary,
      props: true
    },
    {
      path: '/GeneratedItinerary2',
      name: 'GeneratedItinerary2',
      component: GeneratedItinerary2,
    },
    {
      path: '/LoggingOut',
      name: 'LoggingOut',
      component: LoggingOut,
    },
    {
      path: '/EmailVerification',
      name: 'EmailVerification',
      component: EmailVerification,
    },
    {
      path: '/SuperuserPassword',
      // layout: SuperuserLayout,
      name: 'SuperuserPassword',
      component: SuperuserPassword,
      meta: { requiresSuperuser: true } 
    }, // Superuser page  }
    {
      path: '/SuperuserLogin',
      // layout: SuperuserLayout,
      name: 'SuperuserLogin',
      component: SuperuserLogin,
      meta: { requiresSuperuser: true } 
    },
    {
      path: '/SuperuserDashboard',
      // layout: SuperuserLayout,
      name: 'SuperuserDashboard',
      component: SuperuserDashboard,
      meta: { requiresSuperuser: true } 
    },
    {
      path: '/SuperuserAccounts',
      // layout: SuperuserLayout,
      name: 'SuperuserAccounts',
      component: SuperuserAccounts,
      meta: { requiresSuperuser: true } 
    },
    {
      path: '/SuperuserAccountDetails',
      // layout: SuperuserLayout,
      name: 'SuperuserAccountDetails',
      component: SuperuserAccountDetails,
      meta: { requiresSuperuser: true } 
    },
    {
      path: '/SuperuserAnalytics',
      // layout: SuperuserLayout,
      name: 'SuperuserAnalytics',
      component: SuperuserAnalytics,
      meta: { requiresSuperuser: true } 
    },
    {
      path: '/SavedItinerary',
      name: 'SavedItinerary',
      component: SavedItinerary,
      props: true,
    },
    {
      path: '/SavedItinerary2',
      name: 'SavedItinerary2',
      component: SavedItinerary2,
      props: true,
    },
  ],
  scrollBehavior (to, from, savedPosition) {
    console.log("Scrolling!")
    return { top: 0, left: 0 }
  }
})


export default router
