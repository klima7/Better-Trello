<template>
  <v-card v-bind:key="card.title">
    <v-card-title>{{ card.title }}</v-card-title>
    <v-card-subtitle>{{ card.description }}</v-card-subtitle>
  </v-card>
</template>

<script>
export default {
  props: {
    card: Object,
  },
};
</script>
