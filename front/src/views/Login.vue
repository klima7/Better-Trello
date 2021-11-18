<template>
  <v-container fluid>
    <v-row align="center" justify="center" class="mt-5 mb-12">
            <v-col cols="12" md="6" align="center" justify="center">
        <lottie-player src="https://assets7.lottiefiles.com/packages/lf20_87uabjh2.json"  background="transparent"  speed="1" style="width: 70%" loop autoplay></lottie-player>
      </v-col>
      <v-col cols="12" md="6">
    <v-layout align-center justify-center>
      <v-flex>
        <v-card class="elevation-4 mt-12 ml-6 mr-6">
          <v-toolbar dark color="primary">
            <v-toolbar-title>Login</v-toolbar-title>
          </v-toolbar>
          <v-card-text class="px-8">
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
            <div class="mt-4">
              <span class="red--text">{{error}}</span>
            </div>
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
      </v-col>
    </v-row>
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
      error: "",

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
        .catch(_ => {
          this.error = "Invalid email or password"
        })
    },

    resetClicked() {
      this.$refs.form.reset();
    },

  },
};
</script>

