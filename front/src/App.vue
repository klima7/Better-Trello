<template>
  <v-app>
    <AppBar />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import AppBar from "./components/AppBar.vue";
import "@lottiefiles/lottie-player";

export default {
  name: "Trello",
  components: {
    AppBar,
  },
  data: () => ({}),
};
</script>

<style>
body {
  background: url('~@/assets/images/background.jpg') no-repeat top left fixed !important;
  background-size: cover !important;
}
#app {
  background: inherit;
  background-size: inherit;
}
html {
  overflow-x: auto !important;
}
</style>