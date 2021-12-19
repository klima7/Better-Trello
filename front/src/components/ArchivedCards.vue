<template>
  <div>
    <v-card-title class="text-h5">Archived cards</v-card-title>
    <div v-for="column in columns" :key="column.id">
        <v-card v-for="card in column.archived_cards" :key="card.id" class="mb-2 mx-2">
          <v-card-title>{{ card.title }}</v-card-title>
          <v-card-subtitle>{{ card.description }}</v-card-subtitle>

          <v-btn icon @click="bringBackFromArchive(card, column.id)">
            <v-icon color="green">mdi-archive-minus</v-icon>
          </v-btn>
          
          <v-btn icon @click="deleteCard(card, column.id)">
            <v-icon color="red">mdi-delete</v-icon>
          </v-btn>
        </v-card>
    </div>
  </div>
</template>

<script>


export default {
  props: {
    columns: Array,
  },
  // Warning: this code is atrocious.
  methods: {
    bringBackFromArchive: function(card, column_id) {
      this.axios
        .post("/cards/" + card.id + "/archive", {state: false})
        .then((res) => {
          this.$emit("card-archive-change", card, column_id);
          for (var i = 0; i < this.columns.length; i++) {
            if (this.columns[i].id == column_id) {
              this.columns[i].archived_cards.splice(card, 1);
              break;
            }
          }
      });
    },
    deleteCard: function (card, column_id) {
      this.axios
        .delete("/cards/" + card.id + "/delete", {})
        .then((res) => {
          for (var i = 0; i < this.columns.length; i++) {
            if (this.columns[i].id == column_id) {
              this.columns[i].archived_cards.splice(card, 1);
              break;
            }
          }
        });
    },
  }
};
</script>
