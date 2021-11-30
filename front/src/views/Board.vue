<template>
  <v-container>
    <v-row>
      <v-col>
        <BoardName :board="board_info"/>
      </v-col>
    </v-row>
    <v-container fluid class="d-flex flex-row pr-6 pt-3 pl-0">
      <Column v-for="column in board_info.columns" :key="column.id" :column="column"/>
    </v-container>
  </v-container>
</template>

<script>
import BoardName from "@/components/BoardName.vue";
import Column from "@/components/Column.vue";

const axios = require("axios").default;

export default {
  components: {
    BoardName,
    Column,
  },
  data() {
    return {
      id: this.$route.params.board_id,
      board_info: [],
    };
  },
  methods: {
    fetchBoardInfo() {
      if (this.id == null) {
        return;
      }
      let data = {
        id: this.id,
      };
      axios
        .post("/info", data)
        .then((response) => {
          console.log("Successfully fetched board with id: " + this.id);
          this.board_info = response.data;
        })
        .catch((error) => {
          console.log(
            "Error occurred while fetching board with id: " + this.id
          );
        });
    },
  },
  created() {
    this.fetchBoardInfo();
  },
};
</script>

