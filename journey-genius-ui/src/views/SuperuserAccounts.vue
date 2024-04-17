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

        <!-- Labels for the table columns -->
        <!-- <v-row class="mb-2">
            <v-col v-for="header in headers" :key="header.value" cols="auto">
                <strong>{{ header.text }}</strong>
            </v-col>
        </v-row> -->

        <!-- User accounts table -->
        <table class="user-accounts-table">
            <thead>
                <tr>
                    <th v-for="header in headers" :key="header.value" @click="sortByColumn(header.value)">
                        <strong>{{ header.text }}</strong>
                        <span v-if="sortBy === header.value"
                            :class="[sortDesc ? 'mdi mdi-arrow-down' : 'mdi mdi-arrow-up']"></span>
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="user in sortedUsers" :key="user.DatabaseID" @click="selectUser(user)">
                    <td>{{ user.DatabaseID }}</td>
                    <td>{{ user.FirstName }}</td>
                    <td>{{ user.LastName }}</td>
                    <td>{{ user.Email }}</td>
                    <td>{{ user.LastLoggedIn }}</td>
                </tr>
            </tbody>
        </table>

        <!-- Dialog for displaying and editing user details -->
        <v-dialog v-model="dialogVisible" max-width="700px">
            <v-card>
                <v-card-title class="headline">User Information</v-card-title>
                <v-card-text>
                    <!-- ID, Last Name, First Name, Email -->
                    <v-row>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>ID:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedUser.DatabaseID }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Last Name:</strong>
                                </v-col>
                                <v-col cols="9">
                                    <span v-if="!isEditingUser">{{ selectedUser.LastName }}</span>
                                    <v-text-field v-model="editedUser.LastName" v-else></v-text-field>
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>First Name:</strong>
                                </v-col>
                                <v-col cols="9">
                                    <span v-if="!isEditingUser">{{ selectedUser.FirstName }}</span>
                                    <v-text-field v-model="editedUser.FirstName" v-else></v-text-field>
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Email:</strong>
                                </v-col>
                                <v-col cols="9">
                                    <span v-if="!isEditingUser">{{ selectedUser.Email }}</span>
                                    <v-text-field v-model="editedUser.Email" v-else></v-text-field>
                                </v-col>
                            </v-row>
                        </v-col>
                    </v-row>
                    <!-- Date Created -->
                    <v-row>
                        <v-col cols="3">
                            <strong>Date Created:</strong>
                        </v-col>
                        <v-col cols="9">
                            {{ selectedUser.DateCreated }}
                        </v-col>
                    </v-row>
                    <!-- Last Logged In -->
                    <v-row>
                        <v-col cols="3">
                            <strong>Last Logged In:</strong>
                        </v-col>
                        <v-col cols="9">
                            {{ selectedUser.LastLoggedIn }}
                        </v-col>
                    </v-row>
                    <br>
                    <!-- Saved Trips -->
                    <v-card class="mt-4">
                        <v-card-title class="headline">Saved Trips</v-card-title>
                        <v-card-text>
                            <v-data-table :headers="tripHeaders" :items="savedTrips" hide-default-footer>
                                <template v-slot:items="props">
                                    <td>{{ props.item.tripID }}</td>
                                    <td>{{ props.item.tripName }}</td>
                                    <td>{{ props.item.tripDescription }}</td>
                                    <td>
                                        <v-btn color="primary" @click="editTrip(props.item)">Edit</v-btn>
                                    </td>
                                    <td>
                                        <v-btn color="primary" @click="deleteTrip(props.item)">Delete</v-btn>
                                    </td>
                                </template>
                            </v-data-table>
                        </v-card-text>
                    </v-card>
                </v-card-text>
                <v-card-actions>
                    <!-- Freeze, Delete, Reset Password Buttons -->
                    <v-btn color="deep-purple-accent-2" class="mr-4">Freeze</v-btn>
                    <v-btn color="deep-purple-accent-2" class="mr-4">Delete</v-btn>
                    <v-btn color="deep-purple-accent-2">Reset Password</v-btn>
                    <v-btn color="deep-purple-accent-2" class="ml-auto" @click="toggleEditingUser">{{ isEditingUser ?
                        'Save' :
                        'Edit Profile' }}</v-btn>
                    <v-btn color="deep-purple-accent-2" @click="closeDialog">Close</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>


    </div>
</template>

<!-- i would add this under the data table -->
<!-- :sort-by="sortBy" -->
<!-- :sort-desc="sortDesc" -->
<!--:sort-direction="sortDirection" -->

<script>
import axios from 'axios';
export default {
    data() {
        return {
            selectedUser: null, // Newly added property to store selected user
            dialogVisible: false, // Property to control dialog visibility
            isEditingUser: false, // Flag to indicate whether user information is being edited
            tripHeaders: [
                { text: 'Trip ID', value: 'tripID' },
                { text: 'Trip Name', value: 'tripName' },
                { text: 'Trip Description', value: 'tripDescription' },
                { text: 'Edit', value: 'edit', sortable: false },
                { text: 'Delete', value: 'delete', sortable: false }
            ],


            searchQuery: '',
            sortBy: 'Database ID',
            sortDesc: false,
            sortDirection: 'asc',
            buttons: [
                { text: 'Home', to: '/SuperuserDashboard' },
                { text: 'User Accounts', to: '/SuperuserAccounts' },
                { text: 'Analytics', to: '/SuperuserAnalytics' },
            ],
            sortOptions: [
                { text: 'Database ID', value: 'DatabaseID' },
                { text: 'First Name', value: 'FirstName' },
                { text: 'Last Name', value: 'LastName' },
                { text: 'Email', value: 'Email' },
                { text: 'Last Logged In', value: 'LastLoggedIn' },
            ],
            headers: [
                { text: 'Database ID', value: 'DatabaseID' },
                { text: 'First Name', value: 'FirstName' },
                { text: 'Last Name', value: 'LastName' },
                { text: 'Email', value: 'Email' },
                // { text: 'Saved Trips', value: 'SavedTrips' },
                { text: 'Last Logged In', value: 'LastLoggedIn' },
            ],
            users: [],
            savedTrips: [],
        };
    },
    mounted() {
        this.fetchUserAccounts();
        this.fetchSavedTrips();
    },
    computed: {
        filteredUsers() {
            // Convert search query to lowercase for case-insensitive search
            const query = this.searchQuery.toLowerCase().trim();
            // Filter user accounts based on search query
            return this.users.filter(user => {
                return (
                    user.FirstName.toLowerCase().includes(query) ||
                    user.LastName.toLowerCase().includes(query) ||
                    user.Email.toLowerCase().includes(query)
                );
            });
        },
        sortedUsers() {
            let sortedUsers = this.filteredUsers.slice(); // Create a copy of filtered users array

            if (this.sortBy) {
                sortedUsers.sort((a, b) => {
                    const modifier = this.sortDesc ? -1 : 1;
                    const propA = this.getPropertyValue(a, this.sortBy);
                    const propB = this.getPropertyValue(b, this.sortBy);

                    if (propA < propB) return -1 * modifier;
                    if (propA > propB) return 1 * modifier;
                    return 0;
                });
            }

            return sortedUsers;
        },
    },
    methods: {
        // Method to set selected user and open dialog
        selectUser(user) {
            this.selectedUser = { ...user }; // Create a copy of the user object
            this.editedUser = { ...user }; // Initialize edited user object
            this.dialogVisible = true;
            this.isEditingUser = false; // Reset editing flag
        },

        // Method to close dialog
        closeDialog() {
            // this.selectedUser = null;
            this.dialogVisible = false;
            this.isEditing = false; // Reset editing flag

        },

        // Method to toggle editing mode
        toggleEditingUser() {
            this.isEditingUser = !this.isEditingUser;
            console.log(this.isEditingUser)
        },


        // Have fun doing this, Isaac!!!!!!!! FIGHT ON!!!!
        // Method to save user changes
        saveUserChanges() {
            // Send request to update user information
            // For example, using axios:
            axios.put(`http://localhost:8000/api/user_accounts/${this.selectedUser.DatabaseID}`, this.selectedUser)
                .then(response => {
                    // Handle success
                    console.log('User information updated:', response.data);
                    this.isEditing = false; // Exit editing mode
                })
                .catch(error => {
                    // Handle error
                    console.error('Error updating user information', error);
                });
        },

        editTrip(trip) {
            // Implement edit trip functionality
            console.log("Editing trip:", trip);
        },
        deleteTrip(trip) {
            // Implement delete trip functionality
            console.log("Deleting trip:", trip);
        },






        fetchSavedTrips() {
            axios.get('http://localhost:8000/api/fetch_saved_trips')
                .then(response => {
                    this.savedTrips = response.data.savedTrips;
                    console.log('Saved trips data:', this.savedTrips);
                })
                .catch(error => {
                    console.error('Error fetching saved trips', error);
                });
        },

        fetchUserAccounts() {
            // Assuming your Flask backend is running on http://localhost:8000
            axios.get('http://localhost:8000/api/user_accounts')
                .then(response => {
                    this.users = response.data;
                    console.log('User accounts data:', response.data);
                })
                .catch(error => {
                    console.error('Error fetching user accounts', error);
                });
        },
        redirectToUser(selectedUser) {
            this.$router.push({ name: 'UserDetail', params: { id: selectedUser.DatabaseID } });
        },
        getPropertyValue(obj, path) {
            // Helper function to get nested property value
            return path.split('.').reduce((o, p) => o[p], obj);
        },
        sortByColumn(column) {
            if (this.sortBy === column) {
                this.sortDesc = !this.sortDesc;
            } else {
                this.sortBy = column;
                this.sortDesc = false;
            }
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
    background-color: rgb(51, 44, 44);
    /* Darker background color for odd rows */
}

.user-accounts-page .v-data-table .v-data-table-body tr:hover {
    background-color: #171515;
    position: fixed;
    /* Darker background color for hover effect */
}

/* Add your CSS styles for table formatting here */
.user-accounts-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

.user-accounts-table th,
.user-accounts-table td {
    border: 1px solid #ddd;
    padding: 8px;
}

.user-accounts-table th {
    background-color: #e0e0e0;
    color: #333;
}

.user-accounts-table tbody tr:nth-child(even) {
    background-color: #f2f2f2;
    color: #000;
    /* Black text color */
}

.user-accounts-table tbody tr:hover {
    background-color: #ddd;
}

.v-card-title.headline {
    font-size: 24px;
}

.v-card-text {
    font-size: 18px;
    margin-top: 16px;
}

.v-card-actions {
    justify-content: flex-end;
    margin-top: 16px;
}

.v-btn {
    font-size: 18px;
    margin-top: 16px;
}

.user-info-header div {
    /* font-weight: bold; */
    font-size: 30px;
}
</style>