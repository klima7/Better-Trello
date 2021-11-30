<template>
  <v-container class="my-1">
    <!-- not editing -->
    <v-row align="center" v-if="!editing">
      <h1 class="d-inline">{{ board.board_name }}</h1>
      <v-btn icon class="ml-4" @click="editClicked()">
        <v-icon color="black">mdi-pencil</v-icon>
      </v-btn>
    </v-row>

    <!-- editing -->
    <v-row v-else class="pt-3 pb-2">
      <v-form>
        <v-col>
          <v-row align="center">
            <v-text-field
              dense
              hide-details
              outlined
              type="text"
              v-model="newName"
              style="background: white; width: 250pt;"
            />
            <v-btn icon class="ml-2" @click="saveClicked">
              <v-icon color="black">mdi-check</v-icon>
            </v-btn>
            <v-btn icon @click="cancelClicked">
              <v-icon color="black">mdi-close</v-icon>
            </v-btn>
          </v-row>
        </v-col>
      </v-form>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    board: null,
  },

  data() {
    return {
      editing: false,
      newName: "",
    };
  },

  methods: {
    editClicked() {
      this.newName = this.board.board_name;
      this.editing = true;
      console.log(this.editing);
    },

    cancelClicked() {
      this.editing = false;
    },

    saveClicked() {
      if(this.newName.length == 0) return

      console.log('/boards/' + this.board.id);
      this.axios
      .patch('/boards/' + this.board.id, {name: this.newName})
      .then((res) => {
        this.board.board_name = this.newName
        this.editing = false
      })
    },
  },
};
</script>
