<template>
  <v-card
    class="d-flex flex-column list"
    v-bind:key="column.name"
    width="350px"
    color="#89cff0"
  >
    <v-card-title class="text-h5">{{ column.name }}</v-card-title>
    <div>
      <draggable
        :id="column.name"
        class="draggable-list"
        group="my-group"
        animation="200"
        :list="column.cards"
        :scroll-sensitivity="200"
        :force-fallback="true"
        :move="onCardMove"
        @end="onCardDrop"
      >
        <Card
          v-for="card in column.cards"
          :key="card.id"
          :card="card"
          v-on:show-card-details="showCardDetails"
          class="mb-2 mx-2"
        />
        
      </draggable>
      <CardAdd 
          class="mb-2 mx-2"
          :column="column"
        />
    </div>
  </v-card>
</template>

<script>
import Card from "@/components/Card.vue";
import draggable from "vuedraggable";
import CardAdd from "@/components/CardAdd.vue";

export default {
  props: {
    column: Object,
  },

  data() {
    return {
      cardMoveEvent: Object,
    }
  },

  components: {
    Card,
    draggable,
    CardAdd,
  },

  methods: {
    onCardMove: function(event) {
      this.cardMoveEvent = event;
    },

    onCardDrop: function(event) {
      console.log("Element:", this.cardMoveEvent.draggedContext.element.title)
      console.log("From column:", this.cardMoveEvent.from.id)
      console.log("To column:", this.cardMoveEvent.to.id)
      console.log("From position:", this.cardMoveEvent.draggedContext.index)
      console.log("To position:", this.cardMoveEvent.draggedContext.futureIndex)
      console.log("-----------")
    },

    showCardDetails: function(e) {
      this.$emit("show-card-details", e);
    }
  }
};
</script>
