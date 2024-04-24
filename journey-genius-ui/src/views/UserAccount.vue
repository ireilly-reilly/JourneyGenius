<template>
    <v-container>
        <v-card class="mx-auto pa-5" max-width="500">
            <v-card-title class="text-center text-h5">
                User Information
            </v-card-title>
            <br>
            <v-card-text>
                <v-form>
                    <v-text-field v-model="user.firstName" :readonly="!edit" label="First Name"
                        prepend-icon="mdi-account" :class="{ 'v-input--is-focused': edit }"></v-text-field>
                    <v-text-field v-model="user.lastName" :readonly="!edit" label="Last Name" prepend-icon="mdi-account"
                        :class="{ 'v-input--is-focused': edit }"></v-text-field>
                    <v-text-field v-model="user.email" :readonly="!edit" label="Email" prepend-icon="mdi-email"
                        :class="{ 'v-input--is-focused': edit }"></v-text-field>
                    <v-text-field v-model="user.password" :readonly="!edit" :type="edit ? 'text' : 'password'"
                        label="Password" prepend-icon="mdi-lock"></v-text-field>

                </v-form>
            </v-card-text>
            <v-card-actions class="justify-center">
                <v-btn icon @click="edit = !edit">
                    <v-icon>{{ edit ? 'mdi-close' : 'mdi-pencil' }}</v-icon>
                </v-btn>
                <v-btn v-if="edit" color="deep-purple accent-2" @click="confirmChanges" dark>
                    Confirm Changes
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script>
export default {
    data: () => ({
        edit: false,
        user: {
            firstName: "John",
            lastName: "Doe",
            email: "john.doe@example.com",
            password: "securepassword123",
        },
    }),
    methods: {
        confirmChanges() {
            this.edit = false;
            // Add code here to handle the actual update logic, e.g., API calls
            console.log("Changes Confirmed:", this.user);
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