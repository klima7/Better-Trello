<template>
  <v-container>
    <v-row justify="center" class="mt-6">
      <v-img
        height="300"
        src="~@/assets/images/logo.png"
        transition="scale-transition"
        contain
      ></v-img>
    </v-row>
    <v-row justify="center">
      <h1>Welcome on Trello!</h1>
    </v-row>
    <v-row justify="center">
      <h3>Better Trello</h3>
    </v-row>
  </v-container>
</template>

<script>
import store from '../store'

export default {
  beforeRouteEnter(to, from, next) {
    if(store.getters.isLogged) {
      next('/boards')
    }
    else {
      next()
    }
  }
}
</script>