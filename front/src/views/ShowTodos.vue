<template>
  <div class="about pa-8">
    <ul>
      <v-card
        v-for="todo in todos" :key="todo"
        class="pa-2 mt-2"
      >{{ todo.content }}</v-card>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
import constants from '../constants.js'

export default {
  data() {
    return {
      todos: [],
    }
  },
  methods: {
    fetchTodos() {
      const path = constants.BACKEND_URL+'/todos';
      axios.get(path)
        .then((res) => {
          this.todos = res.data
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.fetchTodos()
  }
}
</script>