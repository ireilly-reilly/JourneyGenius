<template>
  <div class="analytics-page dark-mode">
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

    <h1>Analytics</h1>

    <v-container>
      <v-row>
        <v-col cols="12" sm="6" md="4">
          <v-card class="stat-card">
            <v-card-title>Total Accounts</v-card-title>
            <v-card-text class="stat-number">{{ totalAccounts }}</v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" sm="6" md="4">
          <v-card class="stat-card">
            <v-card-title>Users Online</v-card-title>
            <v-card-text class="stat-number">{{ usersOnline }}</v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" sm="6" md="4">
          <v-card class="stat-card">
            <v-card-title>Total Trips Saved</v-card-title>
            <v-card-text class="stat-number">{{ totalTripsSaved }}</v-card-text>
          </v-card>
        </v-col>
        <!-- Add more statistics cards as needed -->
      </v-row>

      <v-row>
        <v-col>
          <v-card class="changelog-card">
            <v-card-title>View Admin Changelog</v-card-title>
            <v-card-actions>
              <v-btn @click="viewAdminChangelog" color="deep-purple-accent-2">View Changelog (PDF)</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      totalAccounts: 1000,
      usersOnline: 50,
      totalTripsSaved: 5000,
      revenueGenerated: 1000000,
      // Add more statistics data as needed
      buttons: [
        { text: 'Home', to: '/SuperuserDashboard' },
        { text: 'User Accounts', to: '/SuperuserAccounts' },
        { text: 'Analytics', to: '/SuperuserAnalytics' },
      ],
    };

  },
  methods: {
    viewAdminChangelog() {
      // Implement logic to open PDF for admin changelog
      alert('Opening admin changelog PDF');
    },
  },
};
</script>

<style>
.analytics-page {
  padding: 20px;
  background-color: #333;
  /* Dark background color */
  color: #dcdcdc;
  /* Light text color */
}

.stat-card {
  text-align: center;
  padding: 20px;
  background-color: #444;
  /* Darker background color */
  border-radius: 8px;
}

.stat-number {
  font-size: 32px;
  font-weight: bold;
}

.changelog-card {
  margin-top: 20px;
  text-align: center;
  background-color: #444;
  /* Darker background color */
  border-radius: 8px;
  padding: 20px;
}

.v-app-bar {
  background-color: #333;
  /* Dark background color */
  color: #dcdcdc;
  /* Light text color */
}

.v-btn {
  color: #fff;
  /* White text color */
}

.v-btn:hover {
  background-color: rgba(255, 255, 255, 0.1);
  /* Lighten button color on hover */
}

.v-btn:active {
  background-color: rgba(255, 255, 255, 0.2);
  /* Darken button color on click */
}

.v-toolbar-title {
  font-weight: bold;
}

.v-card-title {
  font-weight: bold;
}
</style>