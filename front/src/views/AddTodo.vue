<template>
  <div class="about pa-8">
    <v-row align="center" justify="center">
      <h1 class="mb-4">Add todo</h1>
    </v-row>
    <v-row>
      <v-text-field
        label="Content"
        v-model="content"
        outlined>Add</v-text-field>
    </v-row>
    <v-row align="center" justify="center">
      <v-btn
        color="primary"
        elevation="2"
        class="px-12"
        @click="addPressed"
        outlined
      >Add</v-btn>
    </v-row>
    <v-row>
      <v-btn color="primary" class="mr-2" @click="oauth2Default('google')">Google</v-btn>
      <v-btn color="primary" class="mr-2" @click="login()">Login</v-btn>
      <v-btn color="primary" class="mr-2" @click="logout()">Logout</v-btn>
      <v-btn color="primary" class="mr-2" @click="getUser()">Get user</v-btn>
      <v-btn color="primary" class="mr-2" @click="setUser()">Set user</v-btn>
      <v-btn color="primary" class="mr-2" @click="fetch()">Fetch</v-btn>
      <v-btn color="primary" class="mr-2" @click="token()">Token</v-btn>
      <v-btn color="primary" class="mr-2" @click="refresh()">Refresh</v-btn>
      <v-btn color="primary" class="mr-2" @click="register()">Register</v-btn>
    </v-row>
    <v-row>
      <span>Ready: {{$auth.ready()}} Check: {{$auth.check()}}</span>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      content: "",
      form: {
        body: {},
        code: false,
        params: {
          state: {
            remember: false,
            staySignedIn: true,
            fetchUser: true,
          }
        }
      }
    }
  },
  methods: {
    addPressed() {
      const todo = {content: this.content};
      this.addTodo(todo);
    },
    addTodo(todo) {
      const path = '/todos';
      axios.post(path, todo)
      // eslint-disable-next-line no-unused-vars
      .then((_res) => {
        this.content = "";
        alert("Todo added")
      })
        .catch((error) => {
          alert('ERror occurred');
          console.log(error);
        });
    },
    oauth2Default(type) {
      this.$auth.oauth2(type, this.form);
    },

    login() {
      this.$auth.login({
        data: {login: 'ukasz.klimkiewicz@gmail.com', password: '12345678'},
        redirect: {name: 'redirect'},
        remember: 'Rob',
        staySignedIn: true,
        fetchUser: true
      })
      .then((res) => {
        console.log("Login success")
        console.log(res)
      })
      .catch((error) => {
        console.log(error)
      });
    },

    logout() {
      this.$auth.logout({
        redirect: {name: 'redirect'},
      })
      .then((res) => {
        console.log("Logout success")
      })
      .catch((error) => {
        console.log(error)
      });
    },

    getUser() {
      const user = this.$auth.user()
      console.log(user.nick)
    },

    setUser() {
      this.$auth.user({nick: 'unknown'})
    },

    fetch() {
      this.$auth.fetch()
      .then((res) => {
        console.log(res)
      })
      .catch((error) => {
        console.log(error)
      });
    },

    token() {
      console.log(this.$auth.token())
    },

    refresh() {
      this.$auth.refresh()
      .then((res) => {
        console.log(res)
      })
      .catch((error) => {
        console.log(error)
      });
    },

    register() {
      this.$auth .register({
        data: {
            email: 'hello@example.com',
            password: 'abcd1234'
        },
        redirect: {name: 'redirect'},
        remember: 'Rob',
        staySignedIn: true,
        autoLogin: false,
        fetchUser: false
      });
    }

  },
  created() {
    // this.performRequest()
  }
}
</script>