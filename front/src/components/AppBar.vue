<template>
    <v-app-bar
      app
      color="primary"
      dark
    >
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

      <v-btn
        to="/"
        class="ml-8"
        text
      >
        <span class="mr-2">Todos list</span>
        <v-icon>mdi-format-list-checkbox</v-icon>
      </v-btn>

      <v-btn
        to="/addtodo"
        text
      >
        <span class="mr-2">Add todo</span>
        <v-icon>mdi-plus-circle</v-icon>
      </v-btn>

    </v-app-bar>
</template>