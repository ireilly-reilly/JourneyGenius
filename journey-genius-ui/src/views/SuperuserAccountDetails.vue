<template>
    <div class="user-details-page dark-mode">
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

        <h1>User Details</h1>
        
      <v-card>
        <v-list>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>Database ID</v-list-item-title>
              <v-list-item-subtitle>{{ user.DatabaseID }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>First Name</v-list-item-title>
              <v-list-item-subtitle>{{ user.FirstName }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>Last Name</v-list-item-title>
              <v-list-item-subtitle>{{ user.LastName }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>Email</v-list-item-title>
              <v-list-item-subtitle>{{ user.Email }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>Saved Trips</v-list-item-title>
              <v-list-item-subtitle>{{ user.SavedTrips }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>Last Logged In</v-list-item-title>
              <v-list-item-subtitle>{{ user.LastLoggedIn }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card>
     
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: null,

            buttons: [
                { text: 'Home', to: '/SuperuserDashboard' },
                { text: 'User Accounts', to: '/SuperuserAccounts' },
                { text: 'Analytics', to: '/SuperuserAnalytics' },
            ],
        };
    },
    mounted() {
        // Fetch user data based on route parameter
        //const userId = this.$route.params.id; // Assuming the route param is named 'id'
        // this.user = this.getUserById(userId); // Implement this method to fetch user data
    },
    methods: {
        // getUserById(id) {
        // Implement method to fetch user data from a store or API
        // Return the user object based on the provided id
        // },
    },
};
</script>

<style>
.user-details-page {
    padding: 20px;
}

/* Add your dark-mode styles here */
</style>