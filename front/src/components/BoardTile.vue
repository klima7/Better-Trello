<template>
  <v-col cols="12" sm="6" md="4">
    <v-card align-center justify-center color="#4275f5" class="white--text" :to="url">
      <div style="height: 100px" class="text-center">
        <v-container fill-height>
          <v-row justify="center" align="center">
            <v-col>
              {{ board.name }}
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
  computed: {
    url: function() {
      return `/board/${this.board.id}`
    }
  }
};
</script>
