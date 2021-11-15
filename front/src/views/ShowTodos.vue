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
export default {
  data() {
    return {
      todos: [],
    }
  },
  methods: {
    fetchTodos() {
      const path = '/todos';
      this.axios.get(path)
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