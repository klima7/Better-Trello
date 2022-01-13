<template>
  <v-dialog max-width="600px" v-model="value" @click:outside="closeDialog">
    <v-container fluid class="grey lighten-3">
      <h1 class="mb-3">Board labels</h1>
      <h2>Add new</h2>
      <v-row>
        <v-col>
          <v-text-field
            v-model="labelText"
            dense
            hide-details
            outlined
            type="text"
            class="mx-2 mt-2"
            dark
            :background-color="labelColor"
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn
          depressed
          color="primary"
          @click="addLabelClicked"
          >Add</v-btn>

    <v-btn
      v-for="color in colors"
      :key="color"
      class="mx-2"
      fab
      dark
      small
      :color="color"
      @click="colorClicked(color)"
    />
          
        </v-col>
      </v-row>

      <v-row>
        <v-col>
          <h2>Existing</h2>
        </v-col>
      </v-row>

      <v-row class="pa-2 pl-3">
        <BoardLabel
          v-for="label in board.labels"
          :key="label.id"
          :label="label"
          :board="board"
          />
      </v-row>

    </v-container>
  </v-dialog>
</template>

<script>
import BoardLabel from "./BoardLabel.vue";

export default {
  props: {
    value: Boolean,
    board: Object,
  },
  components: {
    BoardLabel,
  },
  data() {
    return {
      labelText: "",
      colors: ["green", "blue", "red", "orange", "purple", "brown"],
      labelColor: "green",
    };
  },
  methods: {
    closeDialog: function (event) {
      this.$emit("visibility-change", false);
    },

    colorClicked(color) {
      this.labelColor = color;
    },

    addLabelClicked() {
      const text = this.labelText;
      if(text.length > 0) {
        this.addLabel(text, this.labelColor);
      }
      this.labelText = "";
    },

    addLabel(text, color) {
      this.axios
            .post(`/boards/${this.board.id}/labels`, {text: text, color: color})
      
    },

  },
};
</script>

<style>
.circle {
  height: 50px;
  width: 60px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
}
</style>