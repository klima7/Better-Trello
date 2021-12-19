<template>
  <div class="px-6">
    <div>
      <BoardName :board="board" />
    </div>
    <div class="d-flex flex-row">
      <draggable
        class="draggable-list columns-container"
        group="columns"
        animation="200"
        draggable=".item"
        :list="board.columns"
        :scroll-sensitivity="200"
        :force-fallback="true"
        @end="onColumnDrop"
      >
        <Column
          v-for="column in board.columns"
          :key="column.id"
          :column="column"
          class="item mr-5"
          v-on:show-card-details="showCardDetails"
        />
        <ColumnAdd 
          slot="footer" 
          class="mr-5"
          :board="board"
        />
      </draggable>
    </div>
    <CardDetails
      v-if="selectedCard"
      v-model="detailsVisible" 
      v-on:visibility-change="hideCardDetails"
      v-on:card-archive-change="hideCard"
      v-bind:card="board.columns[selectedCard.column_id].cards[selectedCard.card_id]" 
      :key="board.columns[selectedCard.column_id].cards[selectedCard.card_id].id"
      />
  </div>
</template>

<script>
import BoardName from "@/components/BoardName.vue";
import Column from "@/components/Column.vue";
import ColumnAdd from "@/components/ColumnAdd.vue";
import CardDetails from "@/components/CardDetails.vue";
import draggable from "vuedraggable";

export default {
  data() {
    return {
      detailsVisible: false,
      selectedCard: null//{id: -1, title: "Title", description: "description"}
    }
  },
  props: {
    board: null,
  },

  components: {
    BoardName,
    Column,
    ColumnAdd,
    CardDetails,
    draggable,
  },

  methods: {
    onColumnDrop: function(event) {
      const columnId = this.board.columns[event.newIndex].id;
      const oldPosition = event.oldIndex;
      const newPosition = event.newIndex;
      this.moveColumn(columnId, newPosition);
    },
    
    showCardDetails: function(event) {
      for (var i = 0; i < this.board.columns.length; i++) {
        if (this.board.columns[i].id == event.column_id) {
          for (var j = 0; j < this.board.columns[i].cards.length; j++) {
            if (this.board.columns[i].cards[j].id == event.card_id) {
              this.selectedCard = {column_id: i, card_id: j};//this.board.columns[i].cards[j];
            }
          }
        }
      }
      console.log("selecting " + JSON.stringify(event));
      this.detailsVisible = true;
    },

    hideCardDetails: function(event) {
      this.detailsVisible = event;
    },

    hideCard: function(event) {
      console.log("card archived: " + JSON.stringify(this.selectedCard));
      this.board.columns[this.selectedCard.column_id].cards.splice(this.selectedCard.card_id, 1);
      this.selectedCard = null;
      this.detailsVisible = false;
    },

    moveColumn(columnId, targetPosition) {
      this.axios
        .patch(`/columns/${columnId}`, {order: targetPosition})
    }
  }

};
</script>

<style scoped>
.columns-container {
  display: flex;
  align-items:flex-start;
  align-content:flex-start;
}
</style>