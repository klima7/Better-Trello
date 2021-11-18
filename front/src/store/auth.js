import Vue from "vue";

export default {
  state() {
    return {};
  },

  actions: {
    fetch(data) {
      return Vue.auth.fetch(data);
    },

    login(ctx, data) {
      var redirect = Vue.auth.redirect();
      return new Promise((resolve, reject) => {
        Vue.auth
          .login({
            data: {
              email: data.email,
              password: data.password,
            },
            redirect: {
              name: redirect ? redirect.from.name : "boards",
            },
            staySignedIn: data.rememberMe,
          })
          .then(resolve, reject);
      });
    },

    register(ctx, data) {
      data = data || {};

      return new Promise((resolve, reject) => {
        Vue.auth
          .register({
            data: {
              email: data.email,
              password: data.password,
            },
            redirect: null,
            staySignedIn: true,
            autoLogin: false,
            fetchUser: true,
          })
          .then((res) => {
            (data.rememberMe = false),
              ctx.dispatch("login", data).then(resolve, reject);
          }, reject);
      });
    },

    logout(ctx) {
      return Vue.auth.logout({
        redirect: "logout",
      });
    },
  },

  getters: {
    user() {
      return Vue.auth.user();
    },
    isLogged() {
      return Vue.auth.user() != null;
    },
  },
};
