<template>
  <v-container>
    <v-row>
      <v-col>
        <BoardName :board="board_info"/>
      </v-col>
    </v-row>
    <v-container fluid class="d-flex flex-row pr-6 pt-3 pl-0">
      <v-card
        v-for="column in board_info.columns"
        class="d-flex flex-column pt-3 mr-6 list"
        v-bind:key="column.name"
        color="#89cff0"
      >
        <h2 class="ms-3">{{ column.name }}</h2>
        <v-container>
          <Card v-for="card in column.cards" :key="card.id" :card="card"/>
        </v-container>
      </v-card>
    </v-container>
  </v-container>
</template>

<script>
import BoardName from "@/components/BoardName.vue";
import Card from "@/components/Card.vue";

const axios = require("axios").default;

export default {
  components: {
    BoardName,
    Card,
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

