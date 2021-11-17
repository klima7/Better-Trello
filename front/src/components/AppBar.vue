<template>
    <v-app-bar
      app
      color="primary"
      dark
    >

      <!-- logo -->
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

        <span class="text-h4">Trello</span>

      </div>

      <v-spacer />

      <!-- authentication buttons -->
      <div>

        <!-- login button -->
        <v-btn
          to="/"
          class="mr-2"
          text
        >
          <span>Login</span>
        </v-btn>

        <!-- register button -->
        <v-btn
          to="/addtodo"
          text
        >
          <span>Register</span>
        </v-btn>

      </div>

    </v-app-bar>
</template>