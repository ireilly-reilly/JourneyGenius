<template>
    <!-- Password change snackbar -->
    <v-snackbar v-model="showPasswordSnackbar" color="deep-purple-accent-2" top>
            <span class="centered-text">Password changed successfully.</span>
    </v-snackbar>
    <!-- Freeze User snackbar -->
    <v-snackbar v-model="showFreezeSnackbar" color="deep-purple-accent-2" top>
            <span class="centered-text">Freeze status updated successfully.</span>
    </v-snackbar>
    <!-- Delete User snackbar -->
    <v-snackbar v-model="showDeleteUserSnackbar" color="deep-purple-accent-2" top>
            <span class="centered-text">Account deleted successfully.</span>
    </v-snackbar>
    <!-- Edit User profile snackbar -->
    <v-snackbar v-model="editUserProfileSnackbar" color="deep-purple-accent-2" top>
            <span class="centered-text">User information updated successfully.</span>
    </v-snackbar>
    <!-- Delete single trip snackbar -->
    <v-snackbar v-model="showTripDeletedSnackbar" color="deep-purple-accent-2" top>
            <span class="centered-text">Trip deleted successfully.</span>
    </v-snackbar>
    <div class="user-accounts-page">
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
        <h1 style="color: black;">User Accounts</h1>
        <br>

        <!-- Search bar -->
        <v-text-field v-model="searchQuery" label="Search" outlined dense color="black"></v-text-field>

        <!-- Sort bar -->
        <v-select v-model="sortBy" :items="sortOptions" label="Sort By" outlined dense color="black"></v-select>

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
                    <td>{{ user.LastName }}</td
                    ><td>{{ user.Email }}</td>
                    <td>{{ user.LastLoggedIn }}</td>
                </tr>
            </tbody>
        </table>

        <!-- Dialog for resetting a user password-->
<v-dialog v-model="resetPasswordDialogVisible" max-width="650">
    <v-card>
        <v-card-title class="headline" style="padding-left: 25px; padding-top: 15px;">Reset User Password</v-card-title>
        <v-card-text>
            <span style="color: red;">Important: This action should only be done with user consent!</span>
            <v-spacer></v-spacer>
            Passwords must contain 1 uppercase letter, 1 lowercase letter, 1 number, 1 special character, and be at least 8 characters long.
        </v-card-text>
        <v-card-text>
            Enter new password:
            <v-text-field v-model="newPassword" label="New Password" type="password" :class="{ 'error-outline': showLoginError }" @keyup.enter="login" />
            <v-spacer></v-spacer>
            Confirm new password:
            <v-text-field v-model="confirmPassword" label="Confirm Password" type="password" :class="{ 'error-outline': showLoginError }" @keyup.enter="login" />
            <span v-if="passwordsDoNotMatch" class="error-message">Passwords do not match.</span>
            <v-spacer></v-spacer>
            <span v-if="!this.validatePassword(this.newPassword)" class="error-message">Password does not meet requirements.</span>
        </v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="deep-purple-accent-2" text @click="resetPasswordDialogVisible = false">Cancel</v-btn>
            <v-btn color="red darken-1" text @click="resetPassword">Reset Password</v-btn>
        </v-card-actions>
    </v-card>
</v-dialog>
        <!-- Dialog for confirming user account delete-->
        <v-dialog v-model="confirmationDialogVisible" max-width="650">
                  <v-card>
                    <v-card-title class="headline"
                      style="padding-left: 25px; padding-top: 15px;">Confirmation</v-card-title>
                    <v-card-text>
                      Are you sure you want to delete this User? This action cannot be undone.
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="deep-purple-accent-2" text @click="confirmationDialogVisible = false">No</v-btn>
                      <v-btn color="red darken-1" text @click="confirmDeleteUser(index)">Yes</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>

                <!-- Dialog for confirming individual user trip delete-->
        <v-dialog v-model="confirmDeleteTripDialog" max-width="650">
                  <v-card>
                    <v-card-title class="headline"
                      style="padding-left: 25px; padding-top: 15px;">Confirmation</v-card-title>
                    <v-card-text>
                      Are you sure you want to delete this user's trip? This action cannot be undone.
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="deep-purple-accent-2" text @click="confirmDeleteTripDialog = false">No</v-btn>
                      <v-btn color="red darken-1" text @click="confirmDeleteTrip">Yes</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
        <!-- Dialog for displaying and editing user details -->
        <v-dialog v-model="dialogVisible" max-width="700px">
            <v-card>
                <v-card-title class="headline">User Information</v-card-title>
                
                <v-card-text>
                    <!-- Additional row for Frozen status -->
            <v-row v-if="selectedUser && selectedUser.FreezeFlag === 1">
                <v-col cols="3">
                    <strong>Freeze Status:</strong>
                </v-col>
                <v-col cols="9">
                    <span style="color: red;">Frozen</span>
                </v-col>
            </v-row>
                    <!-- ID, Last Name, First Name, Email -->
                    <v-row>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Database ID:</strong>
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

        
        

<!-- User Trips table -->
<table class="user-accounts-table">
            <thead>
                <tr>
                    <th v-for="tripHeaders in tripHeaders" :key="tripHeaders.value" @click="sortByColumn(tripHeaders.value)">
                        <strong>{{ tripHeaders.text }}</strong>
                        <span v-if="sortBy === tripHeaders.value"
                            :class="[sortDesc ? 'mdi mdi-arrow-down' : 'mdi mdi-arrow-up']"></span>
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="trip in savedTrips" :key="trip.id" @click="selectTrip(trip)">
                    <td>{{ trip.id }}</td>
                    <td>{{ trip.city }}</td>
                    <td>{{ trip.state }}</td
                    ><td>{{ trip.dates }}</td>
                    <td>
                    <v-btn color="deep-purple-accent-2" @click="editTrip(props.item)">Edit</v-btn>
                </td>
                <td>
                    <v-btn color="deep-purple-accent-2" @click="confirmDeleteTrip">Delete</v-btn>
                </td>
                    <!-- <td>{{ trip.budget }}</td> -->
                </tr>
            </tbody>
        </table>




    </v-card-text>
</v-card>

                </v-card-text>
                <v-card-actions>
                    <!-- Freeze, Delete, Reset Password Buttons -->
                    <v-btn color="deep-purple-accent-2" class="mr-4" @click="freezeAccount">{{ selectedUser && selectedUser.FreezeFlag === 1 ? 'Unfreeze' : 'Freeze' }}</v-btn>
                        
                    <v-btn color="deep-purple-accent-2" class="mr-4" @click="confirmationDialogVisible = true">Delete</v-btn>
                    <v-btn color="deep-purple-accent-2" @click="resetPasswordDialogVisible = true">Reset Password</v-btn>
                    <v-btn color="deep-purple-accent-2" class="ml-auto" @click="toggleEditingUser">{{ isEditingUser ? 'Save' : 'Edit Profile' }}</v-btn>
                    <v-btn color="deep-purple-accent-2" @click="closeDialog">Close</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>


        <!-- Dialog for confirming user account delete-->
        <v-dialog v-model="confirmationDialogVisible" max-width="650">
                  <v-card>
                    <v-card-title class="headline"
                      style="padding-left: 25px; padding-top: 15px;">Confirmation</v-card-title>
                    <v-card-text>
                      Are you sure you want to delete this User? This action cannot be undone.
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="deep-purple-accent-2" text @click="confirmationDialogVisible = false">No</v-btn>
                      <v-btn color="red darken-1" text @click="confirmDeleteUser(index)">Yes</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>





        <!-- Dialog for displaying and editing trip details -->
        <v-dialog v-model="tripDetailsDialog" max-width="800px">
            <v-card>
                <v-card-title class="headline">Trip Information</v-card-title>
                
                <v-card-text>
                    <!-- ID, City, State, Dates, Edit, Delete -->
                    <v-row>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Database ID:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.id }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Dates:</strong>
                                </v-col>
                                <v-col cols="9">
                                    <!-- <span v-if="!isEditingUser">{{ selectedUser.Email }}</span>
                                    <v-text-field v-model="editedUser.Email" v-else></v-text-field> -->
                                    {{ selectedTrip.dates }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>City:</strong>
                                </v-col>
                                <v-col cols="9">
                                    <!-- <span v-if="!isEditingUser">{{ selectedTrip.city }}</span> -->
                                    <!-- <v-text-field v-model="editedUser.LastName" v-else></v-text-field> -->
                                    {{ selectedTrip.city }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>State:</strong>
                                </v-col>
                                <v-col cols="9">
                                    <!-- <span v-if="!isEditingUser">{{ selectedUser.FirstName }}</span>
                                    <v-text-field v-model="editedUser.FirstName" v-else></v-text-field> -->
                                    {{ selectedTrip.state }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Latitude:</strong>
                                </v-col>
                                <v-col cols="9">
                                    <!-- <span v-if="!isEditingUser">{{ selectedUser.Email }}</span>
                                    <v-text-field v-model="editedUser.Email" v-else></v-text-field> -->
                                    {{ selectedTrip.latitude }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Longitude:</strong>
                                </v-col>
                                <v-col cols="9">
                                    <!-- <span v-if="!isEditingUser">{{ selectedUser.Email }}</span>
                                    <v-text-field v-model="editedUser.Email" v-else></v-text-field> -->
                                    {{ selectedTrip.longitude }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Budget:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.budget }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>City Slogan:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.city_slogan }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>City Description:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.city_description }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Selected Activities:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.activities }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Selected Shopping:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.shops }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Selected Restaurants:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.foods }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Selected Landmarks:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.landmarks }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Selected Accommodations:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.hotels }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Generated Activities:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.generated_activities }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Generated Shopping:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.generated_shops }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Generated Restaurants:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.generated_foods }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Generated Landmarks:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.generated_landmarks }}
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12">
                            <v-row>
                                <v-col cols="3">
                                    <strong>Generated Accommodations:</strong>
                                </v-col>
                                <v-col cols="9">
                                    {{ selectedTrip.generated_hotels }}
                                </v-col>
                            </v-row>
                        </v-col>
                    </v-row>
                    <br>

                </v-card-text>
                <v-card-actions>
                    <v-btn color="deep-purple-accent-2" class="mr-4" @click="confirmDeleteTripDialog = true">Delete</v-btn>
                    <v-btn color="deep-purple-accent-2" class="ml-auto" @click="toggleEditingUser">{{ isEditingUser ? 'Save' : 'Edit Trip' }}</v-btn>
                    <v-btn color="deep-purple-accent-2" @click="tripDetailsDialog = false">Close</v-btn>
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
            showPasswordSnackbar: false,
            showFreezeSnackbar: false,
            showDeleteUserSnackbar: false,
            editUserProfileSnackbar: false,
            showTripDeletedSnackbar: false,
            newPassword: '',
            confirmPassword: '',
            selectedUser: null, // Newly added property to store selected user
            editedUser: null,
            selectedTrip: null,
            editedTrip: null,
            dialogVisible: false, // Property to control dialog visibility
            confirmationDialogVisible: false,
            resetPasswordDialogVisible: false,
            tripDetailsDialog: false,
            confirmDeleteTripDialog: false,
            isEditingUser: false, // Flag to indicate whether user information is being edited
            tripHeaders: [
                { text: 'Database ID', value: 'id' },
                { text: 'City', value: 'city' },
                //{ text: 'City Description', value: 'city_description' },
                //{ text: 'Activities', value: 'activities' },
                { text: 'State', value: 'state' },
                { text: 'Dates', value: 'dates' },
                //{ text: 'Budget', value: 'budget' },
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
        //this.fetchSavedTrips();
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
        passwordsDoNotMatch() {
            return this.newPassword !== this.confirmPassword;
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
            this.fetchUserTrips();
        },
        //Method to set selected trip and open dialog for trip details
        selectTrip(trip) {
            this.selectedTrip = { ...trip }; //Creates copy of trip object
            this.editedTrip = { ...trip }; //Initialize edited trip object
            this.tripDetailsDialog = true;
            //this.isEditingTrip = false;
        },

        // Method to close dialog
        closeDialog() {
            // this.selectedUser = null;
            this.dialogVisible = false;
            this.isEditing = false; // Reset editing flag

        },

        // Method to toggle editing mode
        toggleEditingUser() {
            if (this.isEditingUser) {
                // Save changes to user profile
                this.saveUserChanges();
            } else {
                this.isEditingUser = true;
            }
        },


        // Have fun doing this, Isaac!!!!!!!! FIGHT ON!!!!
        // Method to save user changes
        saveUserChanges() {
            // Send PUT request to update user profile
            axios.put(`http://localhost:8000/api/edit_user_account/${this.selectedUser.DatabaseID}`, this.editedUser)
                .then(response => {
                    console.log('User profile updated successfully:', response.data);
                    // Update selectedUser with changes from editedUser
                    this.selectedUser = { ...this.editedUser };
                    this.isEditingUser = false; // Exit edit mode
                    this.fetchUserAccounts();
                    this.editUserProfileSnackbar = true;
                })
                .catch(error => {
                    console.error('Error updating user profile:', error);
                    // Handle error
                });
        },
        fetchUserTrips() {
            axios.get(`http://localhost:8000/api/fetch_user_trips/${this.selectedUser.DatabaseID}`)
            .then(response => {
                this.savedTrips = response.data.savedTrips;
            })
            .catch(error => {
                console.error('Error fetching saved trips:', error);
            });
        },

        editTrip(trip) {
            // Implement edit trip functionality
            console.log("Editing trip:", trip);
        },
        confirmDeleteTrip() {
            // Implement delete trip functionality
            const trip_id = this.selectedTrip.id;

            //Delete Trip from user
            axios.delete(`http://localhost:8000/api/delete_single_user_trip/${trip_id}`)
                .then(response => {
                    //Once the trip is successfully deleted, close the dialog
                    console.log('User trip deleted successfully:', response.data);
                    this.confirmDeleteTripDialog = false;
                    this.tripDetailsDialog = false;
                    this.showTripDeletedSnackbar = true;
                    this.fetchUserTrips;
                    
                })
                .catch(error => {
                    console.error('Error deleting trip:', error);
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
        freezeAccount() {
            const userId = this.selectedUser.DatabaseID; // Assuming you have a property 'DatabaseID' in your selectedUser object

            // Toggle the freeze flag based on its current value
            const newFreezeFlag = this.selectedUser.FreezeFlag === 1 ? 0 : 1;

            // Send a PUT request to update the freeze flag in the database
            axios.put(`http://localhost:8000/api/user_accounts/${userId}/freeze`, { freezeFlag: newFreezeFlag })
            .then(response => {
                console.log('Account freeze status updated successfully:', response.data);
                this.showFreezeSnackbar = true;
        
                // Update the freeze flag locally
                this.selectedUser.FreezeFlag = newFreezeFlag;
            })
            .catch(error => {
                console.error('Error updating account freeze status:', error);
            });
        },
        confirmDeleteUser(index) {
            const userId = this.selectedUser.DatabaseID;

            // Step 1: Delete all trips associated with the user
            axios.delete(`http://localhost:8000/api/delete_user_trips/${userId}`)
                .then(response => {
                    console.log('Trips deleted successfully:', response.data);
            
                    // Step 2: Delete the user account
                    axios.delete(`http://localhost:8000/api/delete_user_account/${userId}`)
                        .then(response => {
                            console.log('User account deleted successfully:', response.data);
                            //Once the user account is deleted, close the confirmation dialog
                            this.confirmationDialogVisible = false;
                            this.dialogVisible = false;
                            this.fetchUserAccounts();
                            this.showDeleteUserSnackbar = true;

                        })
                        .catch(error => {
                            console.error('Error deleting user account:', error);
                        });
                })
                .catch(error => {
                    console.error('Error deleting trips:', error);
                });
        },
        validatePassword(password) {
            const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]{8,}$/;
            return regex.test(password);
        },
        resetPassword() {
            if (this.newPassword !== this.confirmPassword) {
                // Show an error message or handle the mismatched passwords
                console.log("Passwords do not match");
                return;
            }
            //this.validatePassword(this.newPassword);
            if (!this.validatePassword(this.newPassword)) {
                return;
            }
            // Send a PUT request to update the user's password
            const userId = this.selectedUser.DatabaseID; // Assuming you have a property 'DatabaseID' in your selectedUser object
            axios.put(`http://localhost:8000/api/reset_user_password/${userId}`, { newPassword: this.newPassword })
                .then(response => {
                    console.log('User password reset successfully:', response.data);
                    // Close the reset password dialog
                    this.resetPasswordDialogVisible = false;
                    this.showPasswordSnackbar = true;
                })
                .catch(error => {
                    console.error('Error resetting user password:', error);
                    // Show an error message or handle the error
                });
        },
        showPasswordError() {
        return this.newPassword && !this.validatePassword(this.newPassword);
    },
    passwordErrorMessage() {
        return 'Password must contain 1 uppercase letter, 1 lowercase letter, 1 number, 1 special character, and be at least 8 characters long.';
    },
    },
};
</script>

<style scoped>
.user-accounts-page {
    padding: 20px;
    background-color: #FFF;
    color: black;
}

.user-accounts-page h1 {
    margin-bottom: 20px;
    color: black;
}

.user-accounts-page .v-text-field,
.user-accounts-page .v-select {
    margin-bottom: 10px;
    color: black;
}

.user-accounts-page .v-data-table {
    background-color: white;
    color: black;
}

.user-accounts-page .v-data-table .v-data-table-header th {
    color: black;
}

.user-accounts-page .v-data-table .v-data-table-body tr:nth-child(odd) {
    background-color: #f2f2f2;
}

.user-accounts-page .v-data-table .v-data-table-body tr:hover {
    background-color: #ddd;
}

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
}

.user-accounts-table tbody tr:hover {
    background-color: #D1C4E9
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
</style>
