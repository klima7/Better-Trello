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

    refresh(data) {
      return Vue.auth.refresh(data);
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
        .then((res) => {
          if (data.remember) {
            Vue.auth.remember(JSON.stringify({
              name: ctx.getters.user.first_name
            }));
          }
          resolve(res);
        }, reject);
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

    impersonate(ctx, data) {
      var props = this.getters['properties/data'];

      Vue.auth.impersonate({
        url: 'auth/' + data.user.id + '/impersonate',
        redirect: 'user-account'
      });
    },

    unimpersonate(ctx) {
      Vue.auth.unimpersonate({
        redirect: 'admin-users'
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