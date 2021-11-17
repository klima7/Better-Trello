<template>
  <v-app>
    <AppBar/>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import AppBar from './components/AppBar.vue'
import '@lottiefiles/lottie-player';

export default {
  name: 'Trello',
  components: {
    AppBar
  },
  data: () => ({
  }),
};
</script>
