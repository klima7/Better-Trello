import Vue from 'vue'
import VueRouter from 'vue-router'
import AddTodo from '../views/AddTodo.vue'
import ShowTodos from '../views/ShowTodos.vue'

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
]

const router = new VueRouter({
  routes
})

export default router
