<template>
    <v-app-bar
      app
      color="primary"
      dark
    >

      <!-- logo -->
      <router-link to="/" class='white--text' >
        <div class="d-flex" @click="goToHome()">
          <v-img
            alt="Vuetify Logo"
            class="shrink mr-2"
            contain
            src="https://logodix.com/logo/1144058.png"
            transition="scale-transition"
            width="40"
            height="40"
          />
          <span class="text-h4">Trello</span>
        </div>
      </router-link>

      <v-spacer />

      <!-- authentication buttons -->
      <div>

        <!-- login button -->
        <v-btn
          to="/login"
          class="mr-2"
          text
        >
          <span>Login</span>
        </v-btn>

        <!-- register button -->
        <v-btn
          to="/register"
          text
        >
          <span>Register</span>
        </v-btn>

      </div>

    </v-app-bar>
</template>

<script>
export default {
  methods: {
    goToHome() {
      this.$router.push({name: 'home'})
    }
  }
}
</script>

<style>
.active {
  background: transparent;
}
</style>