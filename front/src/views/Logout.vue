<template>
  <v-container>
    <v-row justify="center mt-6">
      <lottie-player
        src="https://assets6.lottiefiles.com/packages/lf20_vmlm0zew.json"
        background="transparent"
        speed="1"
        style="width: 400px; height: 400px"
        autoplay
      />
    </v-row>
    <v-row justify="center">
      <h1>You have been logged out!</h1>
    </v-row>
    <v-row justify="center">
      <v-btn to="/" class="mt-4" outlined color="primary" style="background: white;">To home page</v-btn>
    </v-row>
  </v-container>
</template>

<script>
export default {};
</script>