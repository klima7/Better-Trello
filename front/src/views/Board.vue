<template>
  <Board :board="board" />
</template>

<script>
import Board from "@/components/Board.vue";

const axios = require("axios").default;

export default {
  components: {
    Board,
  },
  data() {
    return {
      id: this.$route.params.board_id,
      board: []
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
          this.board = response.data;
          console.log("board: ", response.data);
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

