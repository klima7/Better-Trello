<template>
  <Board :board="board" />
</template>

<script>
import Board from "@/components/Board.vue";
import SocketIO from "socket.io-client";

const axios = require("axios").default;

export default {
  components: {
    Board,
  },
  data() {
    return {
      socket: SocketIO(process.env.VUE_APP_BACKEND_URL+'/boardss/'+this.$route.params.board_id, { transports : ['websocket']}),
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
    this.socket.on("board-changed", (socket) => {
      console.log("refreshing");
      this.fetchBoardInfo();
    });
  },
};
</script>

