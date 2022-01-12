<template>
  <div class="px-6">
    <div class="d-flex justify-start">
      <BoardName :board="board" />
      <v-btn icon @click="toggleArchived()">
        <v-icon color="black">mdi-archive</v-icon>
      </v-btn>
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
      v-on:card-archive-change="hideCard(board.columns[selectedCard.column_id].cards[selectedCard.card_id])"
      v-on:show-labels-dialog="showLabelsDialog"
      v-bind:card="board.columns[selectedCard.column_id].cards[selectedCard.card_id]" 
      :key="board.columns[selectedCard.column_id].cards[selectedCard.card_id].id"
      />
    <BoardLabelsDialog
      v-model="labelsDialogVisible" 
      v-on:visibility-change="hideLabelsDialog"
    />
    <v-navigation-drawer v-model="drawer" app right>
      <ArchivedCards
        :columns="board.columns"
        v-on:card-archive-change="showCard"
      />
    </v-navigation-drawer>
  </div>
</template>

<script>
import BoardName from "@/components/BoardName.vue";
import Column from "@/components/Column.vue";
import ColumnAdd from "@/components/ColumnAdd.vue";
import CardDetails from "@/components/CardDetails.vue";
import draggable from "vuedraggable";
import ArchivedCards from "@/components/ArchivedCards.vue";
import BoardLabelsDialog from "./BoardLabelsDialog.vue";

export default {
  data() {
    return {
      drawer: false,
      detailsVisible: false,
      selectedCard: null,//{id: -1, title: "Title", description: "description"}
      labelsDialogVisible: false,
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
    ArchivedCards,
    BoardLabelsDialog,
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

    hideCard: function(card) {
      console.log("card archived: " + JSON.stringify(this.selectedCard));
      this.board.columns[this.selectedCard.column_id].archived_cards.push(card);
      this.board.columns[this.selectedCard.column_id].cards.splice(this.selectedCard.card_id, 1);
      this.selectedCard = null;
      this.detailsVisible = false;      
    },

    showCard: function(card, column_id) {
      for (var i = 0; i < this.board.columns.length; i++) {
        if (this.board.columns[i].id == column_id) {
          this.board.columns[i].cards.push(card);
        }
      }
      console.log("brought back card from archive");
    },

    moveColumn(columnId, targetPosition) {
      this.axios
        .patch(`/columns/${columnId}`, {order: targetPosition})
    },

    toggleArchived() {
      this.drawer = !this.drawer;
    },

    showLabelsDialog() {
      this.labelsDialogVisible = true;
    },

    hideLabelsDialog(event) {
      this.labelsDialogVisible = event;
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