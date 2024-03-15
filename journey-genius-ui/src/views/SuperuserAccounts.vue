<template>
    <div class="user-accounts-page dark-mode">
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
        <h1>User Accounts</h1>
        <br>

        <!-- Search bar -->
        <v-text-field v-model="searchQuery" label="Search" outlined dense></v-text-field>

        <!-- Sort bar -->
        <v-select v-model="sortBy" :items="sortOptions" label="Sort By" outlined dense></v-select>

        <!-- User accounts table -->
        <v-data-table :headers="headers" :items="filteredUsers" :search="searchQuery"
            @click:row="redirectToUser"></v-data-table>
    </div>
</template>

<!-- i would add this under the data table -->
<!-- :sort-by="sortBy" -->
<!-- :sort-desc="sortDesc" -->
<!--:sort-direction="sortDirection" -->

<script>
export default {
    data() {
        return {
            searchQuery: '',
            sortBy: 'DatabaseID',
            sortDesc: false,
            sortDirection: 'asc',
            buttons: [
                { text: 'Home', to: '/SuperuserDashboard' },
                { text: 'User Accounts', to: '/SuperuserAccounts' },
                { text: 'Analytics', to: '/SuperuserAnalytics' },
            ],
            sortOptions: [
                { text: 'DatabaseID', value: 'DatabaseID' },
                { text: 'First Name', value: 'FirstName' },
                { text: 'Last Name', value: 'LastName' },
                { text: 'Email', value: 'Email' },
                { text: 'Saved Trips', value: 'SavedTrips' },
                { text: 'Last Logged In', value: 'LastLoggedIn' },
            ],
            headers: [
                { text: 'DatabaseID', value: 'DatabaseID' },
                { text: 'First Name', value: 'FirstName' },
                { text: 'Last Name', value: 'LastName' },
                { text: 'Email', value: 'Email' },
                { text: 'Saved Trips', value: 'SavedTrips' },
                { text: 'Last Logged In', value: 'LastLoggedIn' },
            ],
            users: [
                { DatabaseID: 1, FirstName: 'John', LastName: 'Doe', Email: 'john.doe@example.com', SavedTrips: 2, LastLoggedIn: '2022-03-15' },
                // Add more user objects as needed
            ],
        };
    },
    // computed: {
    //   filteredUsers() {
    //     return this.users.filter(user => {
    //       const propertyValue = user[this.sortBy.toLowerCase()];
    //       return (
    //         user &&
    //         propertyValue &&
    //         propertyValue.toLowerCase().includes(this.searchQuery.toLowerCase())
    //       );
    //     });
    //   },
    // },
    methods: {
        redirectToUser(selectedUser) {
            this.$router.push({ name: 'UserDetail', params: { id: selectedUser.DatabaseID } });
        },
    },
};
</script>

<style>
.user-accounts-page {
    padding: 20px;
    background-color: #333;
    /* Dark background color */
    color: white;
    /* Light text color */
}

.user-accounts-page h1 {
    margin-bottom: 20px;
}

.user-accounts-page .v-text-field,
.user-accounts-page .v-select {
    margin-bottom: 10px;
}

.user-accounts-page .v-data-table {
    background-color: white;
    /* Darker background color for table */
}

.user-accounts-page .v-data-table .v-data-table-header th {
    color: white;
    /* Light text color for table header */
}

.user-accounts-page .v-data-table .v-data-table-body tr:nth-child(odd) {
    background-color: whitesmoke;
    /* Darker background color for odd rows */
}

.user-accounts-page .v-data-table .v-data-table-body tr:hover {
    background-color: #666;
    /* Darker background color for hover effect */
}
</style>