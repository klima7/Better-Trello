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
      v-model="detailsVisible"
      v-on:visibility-change="hideCardDetails"
      :card="selectedCard" 
      :key="selectedCard.id"
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
      selectedCard: {id: -1, title: "Title", description: "description"}
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
      console.log("Column:", columnId);
      console.log("From position:", oldPosition);
      console.log("To position:", newPosition);
      console.log("-----------");
      this.moveColumn(columnId, newPosition);
    },
    
    showCardDetails: function(event) {
      this.selectedCard = event;
      this.detailsVisible = true;
    },

    hideCardDetails: function(event) {
      this.detailsVisible = event;
    },

    moveColumn(columnId, targetPosition) {
      console.log("Moving column");
      console.log("Board id:", this.board.id)
      this.axios
        .patch(`/columns/${columnId}`, {order: targetPosition})
        .then((res) => {
          console.log("Column moved")
        });
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