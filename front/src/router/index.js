import Vue from 'vue'
import VueRouter from 'vue-router'
import AddTodo from '../views/AddTodo.vue'
import ShowTodos from '../views/ShowTodos.vue'
import Redirect from '../views/Redirect.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Show Todos',
    component: ShowTodos
  },
  {
    path: '/addtodo',
    name: 'Add Todo',
    component: AddTodo
  },
  {
    path: '/redirect',
    name: 'redirect',
    component: Redirect
  },
]

Vue.router = new VueRouter({
  mode: "history",
  base: '/Trello-Sierra/',
  routes
})

export default Vue.router
