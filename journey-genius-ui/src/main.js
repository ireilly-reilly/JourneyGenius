import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import 'vuetify/dist/vuetify.min.css';
//import 'materialize-css/dist/css/materialize.min.css';
import store from './store/store.js';

import axios from 'axios';
import Cookies from 'js-cookie';

// //-------------------------------------Token Refreshing-----------------------------------------
// // Define a function to refresh the access token
// function refreshToken() {
//   // Implementation of refreshToken function
//   const refreshToken = Cookies.get('refresh_token');
//   console.log("Refresh Token: ", refreshToken);
//   return axios.post('http://localhost:8000/api/refresh_token', null, {
//     headers: {
//       Authorization: `Bearer ${refreshToken}`,
//     },
//   })
//   .then(response => {
//     const newAccessToken = response.data.access_token;
//     Cookies.remove('login_token');
//     Cookies.set('login_token', newAccessToken, { secure: false });
//     return Promise.resolve(newAccessToken);
//   })
//   .catch(error => {
//     return Promise.reject(error);
//   });
// }

// // Add request and response interceptors for axios
// axios.interceptors.request.use(
//   config => {
//       const accessToken = Cookies.get('login_token');
//       if (accessToken) {
//           config.headers.Authorization = `Bearer ${accessToken}`;
//       }
//       return config;
//   },
//   error => {
//       return Promise.reject(error);
//   }
// );

// axios.interceptors.response.use(
//   response => {
//       return response;
//   },
//   error => {
//       const originalRequest = error.config;
//       if (error.response.status === 401 && !originalRequest._retry) {
//           originalRequest._retry = true;
//           return refreshToken().then(newAccessToken => {
//               originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
//               return axios(originalRequest);
//           }).catch(refreshTokenError => {
//               return Promise.reject(refreshTokenError);
//           });
//       }
//       return Promise.reject(error);
//   }
// );
// //-------------------------------------End Token Refreshing--------------------------------------------

loadFonts()

createApp(App)
  .use(router)
  .use(vuetify)
  .use(store)
  .mount('#app')
