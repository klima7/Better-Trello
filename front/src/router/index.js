import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Logout from "../views/Logout.vue";
import Boards from "../views/Boards.vue";
import NotFound from "../views/NotFound.vue";
import ListBoards from '../views/ListBoards.vue'
import BoardPlaceholder from '../views/BoardPlaceholder.vue'

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/login",
    name: "login",
    component: Login,
    meta: {
      auth: false,
    },
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
  {
    path: "/register",
    name: "register",
    component: Register,
    meta: {
      auth: false,
    },
  },
  {
    path: "/logout",
    name: "logout",
    component: Logout,
    meta: {
      auth: false,
    },
  },
  {
    path: "/boards",
    name: "boards",
    component: Boards,
    meta: {
      auth: true,
    },
  },
  {
    path: "*",
    name: "404",
    component: NotFound,
  },
];

Vue.router = new VueRouter({
  mode: "history",
  base: "/Trello-Sierra/",
  routes,
});

export default Vue.router;
