<template>
    <v-container fluid>
    <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
            <v-card class="elevation-12 mt-12">
                <v-toolbar dark color="primary">
                <v-toolbar-title>Login Form</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                <v-form lazy-validation>
                    <v-text-field
                        prepend-icon="mdi-at"
                        name="email"
                        label="Email"
                        type="text"
                        v-model="email"
                    ></v-text-field>
                    <v-text-field
                        id="password"
                        prepend-icon="mdi-lock"
                        name="password"
                        label="Password"
                        type="password"
                        v-model="password"
                    ></v-text-field>
                    <v-switch
                        v-model="rememberMe"
                        label="Remember Me"
                        ></v-switch>
                </v-form>
                </v-card-text>
                <v-card-actions class="pa-5">
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="loginClicked">Login</v-btn>
                </v-card-actions>
            </v-card>
        </v-flex>
    </v-layout>
    </v-container>
</template>

<script>
export default {
    data() {
        return {
            email: "",
            password: "",
            rememberMe: false,
        }
    },

    methods: {

        loginClicked() {
            alert("Login clicked " + this.rememberMe)
        },
    }
};
</script>

