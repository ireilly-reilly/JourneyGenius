<template>
  <div class="dashboard-page dark-mode">


    <v-app-bar app color="grey">
      <v-toolbar-title>Journey Genius - Admin</v-toolbar-title>
      <!-- Buttons that link to other parts of the site -->
      <div class="d-flex align-center ml-16">
        <v-btn v-for="button in buttons" :key="button.to" flat color="white" :to="button.to">
          {{ button.text }}
        </v-btn>
      </div>

      <v-spacer></v-spacer>

      <v-btn text @click="logout">
        <span style="margin-right: 5px;">Logout</span>
        <v-icon right>mdi-exit-to-app</v-icon></v-btn>
    </v-app-bar>

    <h1>Dashboard</h1>


    <!-- Welcome message -->
    <div class="welcome-message">
      <h1>Welcome, {{ adminName }}</h1>
    </div>

    <!-- Status section -->
    <div class="status-section">
      <h2>Status</h2>
      <div class="status-item">
        <p>TF-IDF Status:</p>
        <div class="status-content">
          <p>{{ tfidfStatus }}</p>
          <v-icon>{{ tfidfIcon }}</v-icon>
        </div>
      </div>
      <div class="status-item">
        <p>Authentication Status:</p>
        <div class="status-content">
          <p>{{ authenticationStatus }}</p>
          <v-icon>{{ authenticationIcon }}</v-icon>
        </div>
      </div>
      <div class="status-item">
        <p>Scraping Status:</p>
        <div class="status-content">
          <p>{{ scrapingStatus }}</p>
          <v-icon>{{ scrapingIcon }}</v-icon>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      adminName: 'Isaac Reilly',
      tfidfStatus: 'Running',
      authenticationStatus: 'Pending',
      scrapingStatus: 'Success',

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
};
</script>

<style>
.dashboard-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #333;
  /* Dark background color */
  color: white;
  /* Light text color */
}

.welcome-message {
  margin-bottom: 20px;
}

.status-section {
  text-align: left;
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