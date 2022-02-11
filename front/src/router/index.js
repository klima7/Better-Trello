import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Logout from "../views/Logout.vue";
import Boards from "../views/Boards.vue";
import NotFound from "../views/NotFound.vue";
import Board from '../views/Board.vue';

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
    path: '/boards',
    name: 'boards',
    component: Boards,
    meta: {
      auth: true,
    }
  },
  {
    path: '/board/:board_id',
    name: 'Board',
    component: Board,
    meta: {
      auth: true,
    }
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
    path: "*",
    name: "404",
    component: NotFound,
  },
];

Vue.router = new VueRouter({
  mode: "history",
  base: "/Better-Trello/",
  routes,
});

export default Vue.router;
