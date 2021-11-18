<template>
    <v-container fluid>
    <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-4 mt-12">
            <v-toolbar dark color="primary">
            <v-toolbar-title>Register Form</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
            <v-form ref="form" v-model="isValid" validation>
                <v-text-field
                    prepend-icon="mdi-at"
                    name="email"
                    label="Email"
                    type="text"
                    v-model="email"
                    :rules="emailRules"
                    clearable
                    required
                ></v-text-field>
                <v-text-field
                    id="password"
                    prepend-icon="mdi-lock"
                    name="password"
                    label="Password"
                    type="password"
                    v-model="password"
                    :rules="passwordRules"
                    clearable
                    required
                ></v-text-field>
                <v-text-field
                    id="repeated"
                    prepend-icon="mdi-lock-check"
                    name="repeated"
                    label="Repeated Password"
                    type="password"
                    v-model="repeatedPassword"
                    :rules="repeatedPasswordRules"
                    clearable
                    required
                ></v-text-field>
            </v-form>
            </v-card-text>
            <v-card-actions class="pa-5">
            <v-spacer></v-spacer>
            <v-btn 
                color="primary" 
                @click="resetClicked"
                >Reset</v-btn>
            <v-btn 
                color="primary" 
                @click="registerClicked"
                :disabled="!isValid"
                >Register</v-btn>
            <v-btn 
                color="primary" 
                @click="test"
                >Test</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
        {{ $store.getters['user'] }}
    </v-layout>
    </v-container>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
      repeatedPassword: "",
      isValid: false,

      emailRules: [
        v => !!v || 'Email is required',
        v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
      ],
      passwordRules: [
        v => v.length >= 8 || 'Password must have at lest 8 characters'
      ],
      repeatedPasswordRules: [
        v => v == this.password || 'Passwords are not the same'
      ]
    }
  },

  methods: {

    registerClicked() {
      if(this.$refs.form.validate()) {
        this.register(this.email, this.password)
      }
    },

    register(email, password, remember) {
      let data = {
        email: email,
        password: password,
      };

      this.$store
        .dispatch('register', data)
        .then(() => {
          console.log('success')
        }, (res) => {
          console.log('failure')
        });
    },

    test() {
      this.register('ukasz43.klimkasdfiewiczsdfdfasdf24@gmail.com', 'KotAdosdflf')
    },

    resetClicked() {
      this.$refs.form.reset();
    }
  }
};
</script>

