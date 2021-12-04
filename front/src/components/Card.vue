<template>
  <v-card v-bind:key="card.title" @click="setActive">
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
    setActive: function(event) {
      console.log("active emmited, parent ", this.$parent);
      this.$emit('borger', this.card);
    }
  }
};
</script>
