<template>
  <!-- Navigation Drawer -->
  <v-navigation-drawer v-model="drawer" location="right" temporary>
    <v-list dense>
      <v-list-item @click="logout" prepend-icon="mdi-logout">
        <v-list-item-title>Logout</v-list-item-title>
      </v-list-item>
      <v-list-item @click="home" prepend-icon="mdi-account-edit">
        <v-list-item-title>Return to Home</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>

  <div class="dashboard-page">
    <v-app-bar app color="grey lighten-2">
      <v-toolbar-title class="white--text">Journey Genius - Admin</v-toolbar-title>
      <!-- Buttons that link to other parts of the site -->
      <div class="d-flex align-center ml-16">
        <v-btn v-for="button in buttons" :key="button.to" text color="white" :to="button.to">
          {{ button.text }}
        </v-btn>
      </div>
      <v-spacer></v-spacer>
      <v-btn text color="white" @click="drawer = !drawer">
        <span style="margin-right: 5px;">Account</span>
        <v-icon right color="white">mdi-account-circle</v-icon>
      </v-btn>
    </v-app-bar>

    <h1 style="color: black;">Dashboard</h1>

    <!-- Welcome message -->
    <div class="welcome-message">
      <h1>Welcome, <span text color="#7C4DFF">{{ adminName }}</span></h1>
    </div>


    <!-- Status section -->
    <div class="status-section">
      <h2>Status</h2>
      <div class="status-item">
        <p>TF-IDF Status:</p>
        <div class="status-content">
          <p>{{ tfidfStatus }}</p>
          <p>{{ tfidfUpdatedStatus }}</p>
          <div>
            <v-icon class="mr-2" color="black">{{ tfidfIcon }}</v-icon>
            <v-btn @click="updateStatus('tfidf')">Update</v-btn>
          </div>
        </div>
      </div>
      <div class="status-item">
        <p>Authentication Status:</p>
        <div class="status-content">
          <p>{{ authenticationStatus }}</p>
          <p>{{ authenticationUpdatedStatus }}</p>
          <div>
            <v-icon class="mr-2" color="black">{{ authenticationIcon }}</v-icon>
            <v-btn @click="updateStatus('authentication')">Update</v-btn>
          </div>
        </div>
      </div>
      <div class="status-item">
        <p>Scraping Status:</p>
        <div class="status-content">
          <p>{{ scrapingStatus }}</p>
          <p>{{ scrapingUpdatedStatus }}</p>
          <div>
            <v-icon class="mr-2" color="black">{{ scrapingIcon }}</v-icon>
            <v-btn @click="updateStatus('scraping')">Update</v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
import Cookies from 'js-cookie';
export default {
  data() {
    return {
      drawer: false, // Control the navigation drawer
      adminName: "Admin Name", // Assuming this is dynamically set
      tfidfStatus: "Status", // Assuming these statuses are dynamically set
      authenticationStatus: "Status",
      scrapingStatus: "Status",
      tfidfIcon: "mdi-checkbox-marked-circle",
      authenticationIcon: "mdi-checkbox-marked-circle",
      scrapingIcon: "mdi-checkbox-marked-circle",

      buttons: [
        { text: 'Home', to: '/SuperuserDashboard' },
        { text: 'User Accounts', to: '/SuperuserAccounts' },
        { text: 'Analytics', to: '/SuperuserAnalytics' },
      ],

    };
  },
  computed: {
    tfidfIcon() {
      return this.tfidfStatus === 'Success' ? 'mdi-check-circle' : 'mdi-alert-circle';
    },
    authenticationIcon() {
      return this.authenticationStatus === 'Success' ? 'mdi-check-circle' : 'mdi-alert-circle';
    },
    scrapingIcon() {
      return this.scrapingStatus === 'Success' ? 'mdi-check-circle' : 'mdi-alert-circle';
    },
  },
  methods: {
    home() {
      const url = 'http://localhost:8000/api/LogoutUser';
      Cookies.remove('login_token');

      axios.post(url)
        .then(response => {
          console.log('Logout successful!', response);
          this.message = 'Logout successful.';
          this.isLoggedIn = false;
          setTimeout(() => {
            window.location = '/'; // Directly navigate to home and refresh
          }, 1000);
        })
        .catch(error => {
          console.error('Error logging out', error);
          this.message = 'Error logging out.';
        })
    },
    logout() {
      const url = 'http://localhost:8000/api/LogoutUser';
      Cookies.remove('login_token');

      axios.post(url)
        .then(response => {
          console.log('Logout successful!', response);
          this.message = 'Logout successful.';
          this.isLoggedIn = false;
          this.$router.push({ name: 'SuperuserLogin' });
        })
        .catch(error => {
          console.error('Error logging out', error);
          this.message = 'Error logging out.';
        })
      this.buttons = [
        { text: 'SuperuserLogin', to: '/SuperuserLogin' },
      ];

    },
    updateStatus(type) {
      // Update the status based on the type (tfidf, authentication, scraping)
      switch (type) {
        case "tfidf":
          this.tfidfStatus = "Updated Status";
          break;
        case "authentication":
          this.authenticationStatus = "Updated Status";
          break;
        case "scraping":
          this.scrapingStatus = "Updated Status";
          break;
        default:
          break;
      }
    },
    fetchSuperuserName() {
      const token = Cookies.get('login_token'); // Assuming you store login token in cookies
      const url = 'http://localhost:8000/api/GetSuperuserName'; // Replace with your endpoint to fetch super user's name

      axios.get(url, {
        headers: {
          Authorization: `Bearer ${token}` // If your backend requires authentication
        }
      })
        .then(response => {
          this.adminName = response.data.name; // Assuming the name is returned in the response data
        })
        .catch(error => {
          console.error('Error fetching super user name', error);
        });
    },
  },
  mounted() {
    // Call fetchSuperuserName when the component is mounted, i.e., when the dashboard is loaded
    this.fetchSuperuserName();
  }
};
</script>

<style>
.dashboard-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #FFF;
  /* Light background color */
  color: black;
  /* Dark text color */
}

.welcome-message {
  margin-bottom: 20px;
}

.status-section {
  text-align: left;
  color: black;
  /* Ensure text color is suitable for a light theme */
}

.status-item {
  margin-bottom: 10px;
}

.status-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  /* Ensures the content stretches to fill the space */
}
</style>
