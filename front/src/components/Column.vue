<template>
  <v-card
    class="d-flex flex-column pt-3 mr-6 list"
    v-bind:key="column.name"
    color="#89cff0"
  >
    <h2 class="ms-3">{{ column.name }}</h2>
    <v-container>
      <Card v-for="card in column.cards" :key="card.id" :card="card"/>
    </v-container>
  </v-card>
</template>

<script>
import Card from "@/components/Card.vue";

export default {
  props: {
    column: Object
  },
  components: {
    Card
  },
};
</script>
