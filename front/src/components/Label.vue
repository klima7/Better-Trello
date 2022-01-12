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
      Remove
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
      Remove
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
      this.delete_in_frontend();
    },
    delete_in_frontend: function() {
      var index = this.card.labels.indexOf(this.label);
      if (index !== -1) {
        this.card.labels.splice(index, 1);
      }
    }
  }
};
</script>
