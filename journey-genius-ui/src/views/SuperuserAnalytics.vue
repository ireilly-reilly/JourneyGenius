<template>
  <div class="analytics-page">
    <v-app-bar app color="grey lighten-2">
            <v-toolbar-title>Journey Genius - Admin</v-toolbar-title>
            <!-- Buttons that link to other parts of the site -->
            <div class="d-flex align-center ml-16">
                <v-btn v-for="button in buttons" :key="button.to" text color="white" :to="button.to">
                    {{ button.text }}
                </v-btn>
            </div>

            <v-spacer></v-spacer>

            <v-btn text color="white" @click="logout">
                <span style="margin-right: 5px;">Logout</span>
                <v-icon right color="white">mdi-exit-to-app</v-icon>
            </v-btn>
        </v-app-bar>

    <h1 style="color: black;">Analytics</h1>

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
              <v-btn @click="downloadAdminChangelog" color="deep-purple-accent-2">Download Changelog (CSV)</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>


<script>
import axios from 'axios';
export default {
  data() {
    return {
      totalAccounts: 0,
      usersOnline: 50,
      totalTripsSaved: 0,
      revenueGenerated: 1000000,
      // Add more statistics data as needed
      buttons: [
        { text: 'Home', to: '/SuperuserDashboard' },
        { text: 'User Accounts', to: '/SuperuserAccounts' },
        { text: 'Analytics', to: '/SuperuserAnalytics' },
      ],
    };

  },
  mounted() {
    this.fetchAnalyticsData();
  },
  methods: {
    async downloadAdminChangelog() {
      try {
        // Make a GET request to the Flask route to download the CSV file
        const response = await axios.get('http://localhost:8000/api/export_changelog_csv', {
          responseType: 'blob' // Important to specify the response type as 'blob'
        });

        // Create a blob from the response data
        const blob = new Blob([response.data], { type: 'text/csv' });

        // Create a temporary anchor element to trigger the download
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'admin_changelog.csv');
        document.body.appendChild(link);

        // Click the link to start the download
        link.click();

        // Cleanup
        window.URL.revokeObjectURL(url);
        document.body.removeChild(link);
      } catch (error) {
        console.error('Error downloading admin changelog:', error);
      }
    },
    async fetchAnalyticsData() {
        try {
          // Make API calls to fetch total accounts and total trips saved
          const accountsResponse = await axios.get('http://localhost:8000/api/total_accounts');
          const tripsResponse = await axios.get('http://localhost:8000/api/total_trips_saved');
  
          // Update data properties with API response data
          this.totalAccounts = accountsResponse.data.totalAccounts;
          this.totalTripsSaved = tripsResponse.data.totalTripsSaved;
        } catch (error) {
          console.error('Error fetching analytics data:', error);
        }
      },
  },
};
</script>

<style scoped>
.analytics-page {
  padding: 20px;
  background-color: #FFF; /* Light background color */
  /* color: white; Dark text color */

}

.stat-card {
  text-align: center;
  padding: 20px;
  background-color: #FFF; /* Light background color */
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Soft shadow for a subtle depth */
}

.stat-number {
  font-size: 32px;
  font-weight: bold;
  color: #7C4DFF; /* Dark gray text for numbers */
}

.changelog-card {
  margin-top: 20px;
  text-align: center;
  background-color: #FFF; /* Light background color */
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Consistent styling with stat cards */
}

.v-app-bar {
  background-color: #FFF; /* Light background color */
  color: black; /* Dark text color */
}

.v-btn {
  color: black; /* Black text color */
}

.v-btn:hover {
  background-color: rgba(0,0,0,0.05); /* Slight darkening on hover */
}

.v-btn:active {
  background-color: rgba(0,0,0,0.1); /* Further darkening on active click */
}

.v-toolbar-title {
  font-weight: bold;
  color: black; /* Ensure text color is consistent */
}

.v-card-title {
  font-weight: bold;
  color: black; /* Dark text for visibility against light background */
}
</style>
