<template>
  <div>

    <v-chip
      v-if="!closeable"
      :color="label.color"
      text-color="white"
      @click:close="delete_clicked"
      class="mb-1 mr-1"
      label
    >
      {{label.text}}
    </v-chip>

    <v-chip
      v-if="closeable"
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
    label: Object,
    card: Object,
    closeable: Boolean,
  },
  methods: {
    delete_clicked: function(event) {
      console.log("Delete clicked");
      this.deleteInFrontend()
      this.deleteInBackend(this.card.id, this.label.id);
    },
    deleteInFrontend: function() {
      var index = this.card.labels.indexOf(this.label);
      if (index !== -1) {
        this.card.labels.splice(index, 1);
      }
    },
    deleteInBackend: function(cardId, labelId) {
      this.axios
            .delete(`/cards/${cardId}/labels/${labelId}`)
    }
  }
};
</script>
