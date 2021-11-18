<template>
  <v-container>
    <v-row justify="center" class="mt-12">
      <h1>Boards</h1>
    </v-row>
    <v-row justify="center">
      <h3>Here should be list of user boards</h3>
    </v-row>
    <v-row justify="center" class="mt-12">
      <h4>// You can get current user this way:</h4>
    </v-row>
    <v-row justify="center">
      <h4>{{ this.$store.getters.user }}</h4>
    </v-row>
  </v-container>
</template>

<script>
export default {};
</script>