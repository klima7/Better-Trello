import Vue from 'vue'
import VueRouter from 'vue-router'
import AddTodo from '../views/AddTodo.vue'
import ShowTodos from '../views/ShowTodos.vue'
import ListBoards from '../views/ListBoards.vue'
import BoardPlaceholder from '../views/BoardPlaceholder.vue'

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
    path: '/listboards',
    name: 'List boards',
    component: ListBoards
  },
  {
    path: '/board/:board_id',
    name: 'Board',
    component: BoardPlaceholder
  },
]

const router = new VueRouter({
  mode: "history",
  base: '/Trello-Sierra/',
  routes
})

export default router
