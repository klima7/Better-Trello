<template>
  <v-col cols="12" sm="6" md="4">
    <v-card align-center justify-center color="#4275f5" class="white--text" :to="url">
      <div style="height: 100px">
        <v-container fill-height>
          <v-row class="text-center" justify="center" align="center">
            <v-col>
              {{ board.name }}
            </v-col>
          </v-row>
          <v-row>
            <v-col align="right">
              <v-btn small @click.prevent="share">udostępnij</v-btn>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </v-card>
  </v-col>
</template>

<script>
export default {
  props: {
    board: Object
  },
  methods: {
    share() {
      console.log("emitting sharing");
      this.$emit("share", this.board);
    }
  },
  computed: {
    url: function() {
      return `/board/${this.board.id}`
    }
  }
};
</script>
