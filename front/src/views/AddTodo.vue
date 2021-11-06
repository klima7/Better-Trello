<template>
  <div class="about">
    <h1>Add todo</h1>
    <input class="form-control" type="text" v-model="content" />
    <button type='button' @click="addPressed">Add</button>
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