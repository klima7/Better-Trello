<template>
  <div class="about pa-8">
    <v-row align="center" justify="center">
      <h1 class="mb-4">Add todo</h1>
    </v-row>
    <v-row>
      <v-text-field
        label="Content"
        v-model="content"
        outlined>Add</v-text-field>
      </v-row>
      <v-row align="center" justify="center">
      <v-btn
        color="primary"
        elevation="2"
        class="px-12"
        @click="addPressed"
        outlined
      >Add</v-btn>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios';
import constants from '../constants.js'

export default {
  data() {
    return {
      content: "",
    }
  },
  methods: {
    addPressed() {
      const todo = {content: this.content};
      this.addTodo(todo);
    },
    addTodo(todo) {
      const path = constants.BACKEND_URL+'/todos';
      axios.post(path, todo)
      // eslint-disable-next-line no-unused-vars
      .then((_res) => {
        this.content = "";
        alert("Todo added")
      })
        .catch((error) => {
          alert('ERror occurred');
          console.log(error);
        });
    },
  },
  created() {
    // this.performRequest()
  }
}
</script>