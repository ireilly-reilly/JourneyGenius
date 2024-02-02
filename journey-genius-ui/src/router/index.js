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


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
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
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
