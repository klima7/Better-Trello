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
        :scroll-sensitivity="200"
        :force-fallback="true"
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
        />
      </draggable>
    </div>
  </div>
</template>

<script>
import BoardName from "@/components/BoardName.vue";
import Column from "@/components/Column.vue";
import ColumnAdd from "@/components/ColumnAdd.vue";
import draggable from "vuedraggable";

export default {
  props: {
    board: null,
  },
  components: {
    BoardName,
    Column,
    ColumnAdd,
    draggable,
  },
};
</script>

<style scoped>
.columns-container {
  display: flex;
  align-items:flex-start;
  align-content:flex-start;
}
</style>