<template>
  <v-dialog max-width="600px" v-model="value" @click:outside="closeDialog">
    <v-container fluid class="grey lighten-3">
      <h2>Add Label</h2>
      <p>Content</p>
      <h2>Existing Labels</h2>
      <p>Content</p>
    </v-container>
  </v-dialog>
</template>

<script>

export default {
  props: {
    value: Boolean,
  },
  data() {
    return {

    };
  },
  methods: {
    closeDialog: function (event) {
      this.$emit("visibility-change", false);
    },
  },
};
</script>