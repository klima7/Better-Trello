<template>
  <v-container fluid>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md4>
        <v-card class="elevation-4 mt-12">
          <v-toolbar dark color="primary">
            <v-toolbar-title>Login Form</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form ref="form" v-model="isValid" validation>
              <v-text-field
                prepend-icon="mdi-at"
                name="email"
                label="Email"
                type="text"
                v-model="email"
                clearable
                :rules="emailRules"
                required
              ></v-text-field>
              <v-text-field
                id="password"
                prepend-icon="mdi-lock"
                name="password"
                label="Password"
                type="password"
                v-model="password"
                clearable
                :rules="passwordRules"
                required
              ></v-text-field>
              <v-switch v-model="rememberMe" label="Remember Me"></v-switch>
            </v-form>
          </v-card-text>
          <v-card-actions class="pa-5">
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="resetClicked">Reset</v-btn>
            <v-btn color="primary" @click="loginClicked" :disabled="!isValid"
              >Login</v-btn
            >
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
      isValid: false,

      emailRules: [(v) => !!v || "Email is required"],
      passwordRules: [(v) => !!v || "Password is required"],
    };
  },

  methods: {
    loginClicked() {
      if (this.$refs.form.validate()) {
        this.login(this.email, this.password, this.rememberMe)
      }
    },

    login(email, password, rememberMe) {
      let data = {
        email: email,
        password: password,
        rememberMe: rememberMe
      };

      this.$store
        .dispatch('login', data)
        .then(() => {
          console.log('login success')
        }, (res) => {
          console.log('login failure')
        });
    },

    resetClicked() {
      this.$refs.form.reset();
    },

  },
};
</script>

