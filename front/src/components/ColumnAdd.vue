<template>
  <v-card
    class="d-flex flex-column list"
    width="350px"
    color="#89cff0"
  >
    <v-text-field
      v-if="adding"
      ref="nameField"
      v-model="columnName"
      dense
      hide-details
      outlined
      type="text"
      class="mx-2 mt-2"
      style="background: white;"
    />
    <v-btn
      v-if="!adding"
      @click="firstAddClicked"
      color="blue-grey"
      class="ma-2 white--text"
    >
      <v-icon
        left
        dark
      >
        mdi-plus-thick
      </v-icon>
      Add next column
    </v-btn>
    <div v-if="adding">
      <v-btn
        @click="secondAddClicked"
        color="blue-grey"
        class="ma-2 white--text"
        width="200px"
      >
        <v-icon
          left
          dark
        >
          mdi-plus-thick
        </v-icon>
        Add column
      </v-btn>
      <v-btn 
        icon
        @click="cancelClicked"
      >
        <v-icon color="black">mdi-close-thick</v-icon>
      </v-btn>
    </div>
  </v-card>
</template>

<script>
export default {
  props: {
    board: null,
  },

  data() {
    return {
      adding: false,
      columnName: "",
    };
  },

  methods: {
    firstAddClicked() {
      this.columnName = "";
      this.adding = true;
      this.setFocusOnTextField();
    },

    cancelClicked() {
      this.adding = false;
    },

    secondAddClicked() {
      const columnName = this.columnName.trim();
      if(columnName.length == 0) return;

      console.log("Adding column: " + this.columnName);
      this.board.columns.push({name: columnName, cards: []});
      this.addColumn(columnName);
      this.columnName = "";
      this.setFocusOnTextField();
    },

    setFocusOnTextField() {
      setTimeout(() => {  this.$refs.nameField.focus(); }, 50);
    },

    addColumn(columnName) {
      this.axios
      .post(`/boards/${this.board.id}/columns`, {name: columnName})
      .then((res) => {
        console.log("Column added")
      });
    }
  },
};
</script>
