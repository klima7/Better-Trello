import Vue from 'vue';

export default {

  state() {
    return {
        
    };
  },

  actions: {
    fetch(data) {
      return Vue.auth.fetch(data);
    },

    login(ctx, data) {
      return new Promise((resolve, reject) => {
        Vue.auth.login({
          data: {
            email: data.email,
            password: data.password,
          },
          redirect: null,
          staySignedIn: data.rememberMe,
        })
        .then(resolve, reject);
      });
    },

    register(ctx, data) {
      data = data || {};

      return new Promise((resolve, reject) => {
        Vue.auth.register({
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
          data.rememberMe = false,
          ctx.dispatch('login', data).then(resolve, reject);
        }, reject);
      });
    },

    logout(ctx) {
      return Vue.auth.logout();
    },
},

  getters: {
    user() {
      return Vue.auth.user();
    },
  }

}