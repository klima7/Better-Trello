<template>
  <div class="about">
    <ul>
      <li style="list-style-type: none;" v-for="todo in todos" :key="todo">{{ todo.content }}</li>
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