<template>
  <v-card
    class="d-flex flex-column list"
    v-bind:key="column.name"
    width="500px"
    color="#89cff0"
  >
    <v-card-title class="text-h5">{{ column.name }}</v-card-title>
    <div>
      <draggable
        class="draggable-list"
        group="my-group"
        animation="200"
        :scroll-sensitivity="200"
        :force-fallback="true"
      >
        <Card
          v-for="card in column.cards"
          :key="card.id"
          :card="card"
          class="mb-2 mx-2"
        />
      </draggable>
    </div>
  </v-card>
</template>

<script>
import Card from "@/components/Card.vue";
import draggable from "vuedraggable";

export default {
  props: {
    column: Object,
  },
  components: {
    Card,
    draggable,
  },
};
</script>
