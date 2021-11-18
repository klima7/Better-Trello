import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Logout from "../views/Logout.vue";
import Boards from "../views/Boards.vue";

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
  },
  {
    path: "/register",
    name: "register",
    component: Register,
  },
  {
    path: "/logout",
    name: "logout",
    component: Logout,
  },
  {
    path: "/boards",
    name: "boards",
    component: Boards,
    meta: {
      auth: true,
    },
  },
];

Vue.router = new VueRouter({
  mode: "history",
  base: "/Trello-Sierra/",
  routes,
});

export default Vue.router;
