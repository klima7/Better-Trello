import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import http from './http'
import config from './config'
import './assets/css/main.css'; // global styles

Vue.config.productionTip = false

new Vue({
  el: '#app',
  http: http,
  router: router,
  store: store,
  vuetify: vuetify,
  config: config,
  render: h => h(App),

  created () {
    if (sessionStorage.redirect) {
        const redirect = sessionStorage.redirect
        delete sessionStorage.redirect
        this.$router.push(redirect)
    }
}
});
