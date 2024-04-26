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

import CustomizeTrips from '../views/CustomizeTrips.vue'
import CustomizeItinerary from '../views/CustomizeItinerary.vue'
import UserAccount from "../views/UserAccount.vue"

import Cookies from 'js-cookie'
import axios from 'axios'



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
      meta: { requiresAuth: true },
    },
    {
      path: '/StartPlanning',
      name: 'StartPlanning',
      component: StartPlanning,
      meta: { requiresAuth: true },
    },
    {
      path: '/SavedTrips',
      name: 'SavedTrips',
      component: SavedTrips,
      meta: { requiresAuth: true },
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
      meta: { requiresAuth: true } // Requires authentication to access
    },
    {
      path: '/MoreActivitiesPage',
      name: 'MoreActivitiesPage',
      component: MoreActivitiesPage,
      meta: { requiresAuth: true },
    },
    {
      path: '/MoreDiningPage',
      name: 'MoreDiningPage',
      component: MoreDiningPage,
      meta: { requiresAuth: true },
    },
    {
      path: '/MoreLandmarksPage',
      name: 'MoreLandmarksPage',
      component: MoreLandmarksPage,
      meta: { requiresAuth: true },
    },
    {
      path: '/MoreShoppingPage',
      name: 'MoreShoppingPage',
      component: MoreShoppingPage,
      meta: { requiresAuth: true },
    },
    {
      path: '/Itinerary2',
      name: 'Itinerary2',
      component: Itinerary2,
      meta: { requiresAuth: true },
    },
    {
      path: '/GeneratedItinerary',
      name: 'GeneratedItinerary',
      component: GeneratedItinerary,
      meta: { requiresAuth: true }, // Requires authentication to access
      props: true
    },
    {
      path: '/GeneratedItinerary2',
      name: 'GeneratedItinerary2',
      component: GeneratedItinerary2,
      meta: { requiresAuth: true },
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
      meta: { requiresAuth: true },
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
    },
    {
      path: '/SuperuserDashboard',
      // layout: SuperuserLayout,
      name: 'SuperuserDashboard',
      component: SuperuserDashboard,
      meta: { requiresAuth: true, requiresSuperuser: true }
    },
    {
      path: '/SuperuserAccounts',
      // layout: SuperuserLayout,
      name: 'SuperuserAccounts',
      component: SuperuserAccounts,
      meta: { requiresAuth: true, requiresSuperuser: true }
    },
    {
      path: '/SuperuserAccountDetails',
      // layout: SuperuserLayout,
      name: 'SuperuserAccountDetails',
      component: SuperuserAccountDetails,
      meta: { requiresAuth: true, requiresSuperuser: true }
    },
    {
      path: '/SuperuserAnalytics',
      // layout: SuperuserLayout,
      name: 'SuperuserAnalytics',
      component: SuperuserAnalytics,
      meta: { requiresAuth: true, requiresSuperuser: true }
    },
    {
      path: '/SavedItinerary',
      name: 'SavedItinerary',
      component: SavedItinerary,
      meta: { requiresAuth: true },
      props: true,
    },
    {
      path: '/SavedItinerary2',
      name: 'SavedItinerary2',
      component: SavedItinerary2,
      meta: { requiresAuth: true },
      props: true,
    },
    {
      path: '/CustomizeTrips',
      name: 'CustomizeTrips',
      component: CustomizeTrips,
      meta: { requiresAuth: true },
      props: true,
    },
    {
      path: '/CustomizeItinerary',
      name: 'CustomizeItinerary',
      component: CustomizeItinerary,
      meta: { requiresAuth: true },
      props: true,
    },
    {
      path: '/UserAccount',
      name: 'UserAccount',
      component: UserAccount,
      meta: { requiresAuth: true },
      props: true,
    }

  ],
  scrollBehavior (to, from, savedPosition) {
    console.log("Scrolling!")
    return { top: 0, left: 0 }
  }
})

// router.beforeEach(async (to, from, next) => {
//   // Check if the route requires authentication
//   if (to.meta.requiresAuth) {
//     try {
//       // Wait for the result of isAuthenticated()
//       const authenticated = await isAuthenticated();
//       console.log("Authenticated:", authenticated);

//       if (!authenticated) {
//         // If not authenticated, redirect to login page
//         next('/LoginPage');
//       } else {
//         // If authenticated, allow access to the route
//         next();
//       }
//     } catch (error) {
//       console.error('Error checking authentication:', error);
//       // If an error occurs, redirect to login page or handle accordingly
//       next('/LoginPage');
//     }
//   } else {
//     // If the route does not require authentication, allow access
//     next();
//   }
// });

// async function isAuthenticated() {
//   // Get the login_token cookie
//   const loginToken = Cookies.get('login_token');
//   console.log('loginToken:', loginToken);

//   // If loginToken is undefined, null, or an empty string, user is not logged in
//   if (!loginToken || loginToken === '' || loginToken === undefined) {
//     console.log('Reached this point');
//     return false;
//   } else {
//     try {
//       // Make an API call to verify the token's identity
//       const response = await axios.post('http://localhost:8000/api/verify-token', {}, {
//         headers: {
//           Authorization: `Bearer ${loginToken}`, // Use loginToken here
//         },
//       });

//       // Check if the API call was successful and the user is authenticated
//       if (response.data.authenticated) {
//         return true;
//       } else {
//         return false;
//       }
//     } catch (error) {
//       console.error('Error verifying token:', error);
//       // If there's an error, return false (user is not authenticated)
//       return false;
//     }
//   }
// }

router.beforeEach(async (to, from, next) => {
  if (to.meta.requiresAuth) {
    try {
      const authenticated = await isAuthenticated();
      console.log('Authenticated:', authenticated);

      if (!authenticated) {
        next('/LoginPage');
      } else {
        if (to.meta.requiresSuperuser) {
          const isSuperuser = await isSuperuserAuthenticated();
          console.log('Superuser:', isSuperuser);

          if (!isSuperuser) {
            // Redirect to unauthorized page or handle appropriately
            next('/');
          } else {
            next();
          }
        } else {
          next();
        }
      }
    } catch (error) {
      console.error('Error checking authentication:', error);
      next('/LoginPage');
    }
  } else {
    next();
  }
});

async function isAuthenticated() {
  const loginToken = Cookies.get('login_token');
  console.log('loginToken:', loginToken);

  if (!loginToken || loginToken === '' || loginToken === undefined) {
    console.log('User not logged in');
    return false;
  }

  try {
    const response = await axios.post(
      'http://localhost:8000/api/verify-token',
      {},
      {
        headers: {
          Authorization: `Bearer ${loginToken}`
        }
      }
    );

    return response.data.authenticated;
  } catch (error) {
    console.error('Error verifying token:', error);
    return false;
  }
}

async function isSuperuserAuthenticated() {
  const superToken = Cookies.get('super_token');
  console.log('superToken:', superToken);

  if (!superToken || superToken === '' || superToken === undefined) {
    console.log('Superuser not logged in');
    return false;
  }

  try {
    const response = await axios.post(
      'http://localhost:8000/api/verify_super_token',
      {},
      {
        headers: {
          Authorization: `Bearer ${superToken}`
        }
      }
    );

    return response.data.authenticated;
  } catch (error) {
    console.error('Error verifying super token:', error);
    return false;
  }
}



export default router
