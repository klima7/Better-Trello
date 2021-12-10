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
        :id="column.id"
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
      const cardId = this.cardMoveEvent.draggedContext.element.id;
      const sourceColumn = parseInt(this.cardMoveEvent.from.id);
      const targetColumn = parseInt(this.cardMoveEvent.to.id);
      const sourcePosition = this.cardMoveEvent.draggedContext.index;
      const targetPosition = this.cardMoveEvent.draggedContext.futureIndex;

      console.log("Element:", cardId);
      console.log("From column:", sourceColumn);
      console.log("To column:", targetColumn);
      console.log("From position:", sourcePosition)
      console.log("To position:", targetPosition)
      console.log("-----------")

      this.moveCard(cardId, targetColumn, targetPosition)
    },

    showCardDetails: function(e) {
      this.$emit("show-card-details", e);
    },

    moveCard(cardId, targetColumn, targetPosition) {
      console.log("Moving card");
      this.axios
        .patch(`/cards/${cardId}`, {column: targetColumn, order: targetPosition})
        .then((res) => {
          console.log("Card moved")
        });
    }
  }
};
</script>
