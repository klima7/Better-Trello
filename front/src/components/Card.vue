<template>
  <v-card v-bind:key="card.title" @click="showDetails">
    <v-card-text v-if="card.labels.length != 0">
        <v-row>
      <Label
        v-for="label in card.labels"
        :key="label.id"
        :label="label"
        :card="card"
        :closeable="false"
        />
    </v-row>
    </v-card-text>
    <v-card-title>{{ card.title }}</v-card-title>
    <v-card-subtitle>
      {{ card.description }}
      </v-card-subtitle>
  </v-card>
</template>

<script>
import Label from "./Label.vue";

export default {
  props: {
    card: Object,
  },
  components: {
    Label,
  },
  methods: {
    showDetails: function(event) {
      this.$emit('show-card-details', this.card.id);
    }
  }
};
</script>
