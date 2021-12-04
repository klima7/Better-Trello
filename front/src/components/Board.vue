<template>
  <div class="px-6">
    <div>
      <BoardName :board="board" />
      <p> {{ detailsVisible }}</p>
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
        />
        <ColumnAdd 
          slot="footer" 
          class="mr-5"
          :board="board"
        />
      </draggable>
    </div>
    <CardDetails
      v-model="detailsVisible" />
      <v-btn @click="tempShowDialog">Test</v-btn>
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
      detailsVisible: true
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
    tempShowDialog: function(event) {
      this.detailsVisible = true;
      console.log(`this.detailsVisible: ${this.detailsVisible}`);
    },
    onColumnDrop: function(event) {
      console.log("Column:", this.board.columns[event.newIndex].name)
      console.log("From position:", event.oldIndex)
      console.log("To position:", event.newIndex)
      console.log("-----------")
    },
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