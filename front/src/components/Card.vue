<template>
<v-card
  class="mb-3"
  v-bind:key="card.title"
>
  <v-card-title>{{ card.title }}</v-card-title>
  <v-card-text>{{ card.description }}</v-card-text>
</v-card>
</template>

<script>
export default {
  props: {
    card: Object
  },
};
</script>
