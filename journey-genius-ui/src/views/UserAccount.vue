<template>
    <!-- Password change snackbar -->
    <v-snackbar v-model="showPasswordSnackbar" color="deep-purple-accent-2" top>
            <span class="centered-text">Password changed successfully.</span>
    </v-snackbar>
    <!-- Edit User profile snackbar -->
    <v-snackbar v-model="editUserProfileSnackbar" color="deep-purple-accent-2" top>
            <span class="centered-text">Profile updated successfully.</span>
    </v-snackbar>
    <v-container>
        <v-card class="mx-auto pa-5" max-width="500">
            <v-card-title class="text-center text-h5">
                Profile
            </v-card-title>
            <br>
            <v-card-text>
                <v-form>
                    <v-text-field v-model="user.firstName" :readonly="!editInfo" label="First Name"
                        prepend-icon="mdi-account" :class="{ 'v-input--is-focused': editInfo }"></v-text-field>
                    <v-text-field v-model="user.lastName" :readonly="!editInfo" label="Last Name"
                        prepend-icon="mdi-account" :class="{ 'v-input--is-focused': editInfo }"></v-text-field>
                    <v-text-field v-model="user.email" :readonly="!editInfo" label="Email" prepend-icon="mdi-email"
                        :class="{ 'v-input--is-focused': editInfo }"></v-text-field>
                    <span v-if="editInfo && errorMessage" class="error-message">{{ errorMessage }}</span>
                </v-form>
            </v-card-text>
            <v-card-actions class="justify-center">
                <v-btn text @click="toggleEdit">
                    <span :class="{ 'purple--text text--darken-2': !editInfo, 'mr-3': editInfo }">
                        {{ editInfo ? '' : 'Edit Profile ' }}
                    </span>
                    <v-icon color="deep-purple-accent-2" right>{{ editInfo ? 'mdi-close' : 'mdi-pencil' }}</v-icon>
                </v-btn>

                <v-btn v-if="editInfo" color="deep-purple accent-2" @click="saveUserChanges" dark>
                    Confirm Changes
                </v-btn>
                <v-btn v-if="editInfo" color="red" @click="resetPasswordDialogVisible = true" dark>
                    Reset Password
                </v-btn>
            </v-card-actions>
        </v-card>
        <!-- Dialog for resetting a user password-->
<v-dialog v-model="resetPasswordDialogVisible" max-width="650">
    <v-card>
        <v-card-title class="headline" style="padding-left: 25px; padding-top: 15px;">Reset Password</v-card-title>
        <v-card-text>
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
    </v-container>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie'
export default {
    data: () => ({
        editInfo: false,

        newPassword: '',
        confirmPassword: '',

        newFirstName: '',
        newLastName: '',
        newEmail: '',

        resetPasswordDialogVisible: false,
        showPasswordSnackbar: false,
        editUserProfileSnackbar: false,
        errorMessage: '',
        user: {
            firstName: "",
            lastName: "",
            email: "",
        },
    }),
    computed: {
        passwordsDoNotMatch() {
            return this.newPassword !== this.confirmPassword;
        },
    },
    mounted() {
        this.fetchUserInfo();
    },
    methods: {
        toggleEdit() {
            this.editInfo = !this.editInfo //Toggle edit mode
            this.fetchUserInfo(); //Fetch user info again to revert any unsaved changes
        },
        resetPassword() {
            // Implement logic to handle password reset, e.g., showing a modal to enter a new password
            console.log("Password reset requested");
        },
        validatePassword(password) {
            const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]{8,}$/;
            return regex.test(password);
        },
        showPasswordError() {
            return this.newPassword && !this.validatePassword(this.newPassword);
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
            //const userId = this.selectedUser.DatabaseID; // Assuming you have a property 'DatabaseID' in your selectedUser object
            const token = Cookies.get('login_token');
            axios.put(`http://localhost:8000/api/user_account/reset_user_password`, { newPassword: this.newPassword }, {
                headers: {
                Authorization: `Bearer ${token}`,
                },
            })
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
        fetchUserInfo(){
            const token = Cookies.get('login_token');
            axios.get(`http://localhost:8000/api/user_account/fetch_user_info`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            })
            .then(response => {
                console.log('User info fetched successfully:', response.data);
                this.user.firstName = response.data.firstName;
                this.user.lastName = response.data.lastName;
                this.user.email = response.data.email;
                //this.user.firstName = data.get(firstName, this.user.firstName);
            })
            .catch(error => {
                console.error('Error fetching user info:', error);
                // Show an error message or handle the error
            });
        },
        saveUserChanges() {
            this.newFirstName = this.user.firstName;
            this.newLastName = this.user.lastName;
            this.newEmail = this.user.email;

            //Email validation regular expression
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            // Check if the email is valid
            if (!emailRegex.test(this.newEmail)) {
                // Show an error message or handle invalid email
                this.errorMessage = 'Please enter a valid email address.';
                return;
            }

            
            const token = Cookies.get('login_token');
            // Send PUT request to update user profile
            axios.put(`http://localhost:8000/api/user_account/edit_user_account`, { newFirstName: this.newFirstName, newLastName: this.newLastName, newEmail: this.newEmail }, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            })
                .then(response => {
                    console.log('User profile updated successfully:', response.data);
                    
                    
                    this.editInfo = false; // Exit edit mode
                    this.fetchUserInfo();
                    this.editUserProfileSnackbar = true;
                })
                .catch(error => {
                    console.error('Error updating user profile:', error);
                });
        },
        
    },
};
</script>

<style scoped>
.v-input--is-focused .v-input__control .v-input__slot {
    border-bottom: 2px solid var(--v-deep-purple-accent-2-base);
    outline: none !important;
}
</style>
