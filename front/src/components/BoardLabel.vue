<template>
  <div>

    <v-chip
      close
      :color="label.color"
      text-color="white"
      @click:close="delete_clicked"
      class="mb-1 mr-1"
      label
    >
      {{label.text}}
    </v-chip>

  </div>
</template>

<script>
export default {
  props: {
    board: Object,
    label: Object,
  },
  methods: {
    delete_clicked: function(event) {
      this.axios
            .delete(`/boards/${this.board.id}/labels/${this.label.id}`)
    },
  }
};
</script>
