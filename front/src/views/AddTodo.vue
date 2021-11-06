<template>
  <div class="about">
    <h1>This is test page</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  methods: {
    performRequest() {
      const path = 'https://pawtrello.herokuapp.com/';
      axios.get(path)
        .then((res) => {
          alert(res.data)
        })
        .catch((error) => {
          alert(error);
        });
    },
  },
  created() {
    // this.performRequest()
  }
}
</script>