<template>
    <v-app-bar
      app
      color="primary"
      dark
    >

      <!-- logo -->
      <router-link to="/" class='white--text' >
        <div class="d-flex">
          <v-img
            alt="Vuetify Logo"
            class="shrink mr-2"
            contain
            src="https://logodix.com/logo/1144058.png"
            transition="scale-transition"
            width="40"
            height="40"
          />
          <span class="text-h4">BetterTrello</span>
        </div>
      </router-link>

      <v-spacer />

      <div v-if="!this.$store.getters.isLogged">

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

      <!-- logout button -->
      <div v-else>

        <v-btn
          @click="logout"
          text
        >
          <span>Logout</span>
        </v-btn>

      </div>

    </v-app-bar>
</template>

<script>
export default {
  methods: {
    logout() {
      console.log('logout')
      this.$store.dispatch('logout')
    }
  }
}
</script>
