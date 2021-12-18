<template>
  <v-card v-bind:key="card.title" @click="showDetails">
    <v-card-title>{{ card.title }}</v-card-title>
    <v-card-subtitle>{{ card.description }}</v-card-subtitle>
  </v-card>
</template>

<script>
export default {
  props: {
    card: Object,
  },
  methods: {
    showDetails: function(event) {
      this.$emit('show-card-details', this.card.id);
    }
  }
};
</script>
