<template>
  <v-card
    class="d-flex flex-column list"
  >
    <v-text-field
      v-if="adding"
      ref="nameField"
      v-model="cardTitle"
      dense
      hide-details
      outlined
      type="text"
      class="mx-2 mt-2"
      style="background: white;"
    />
    <v-btn
      v-if="!adding"
      @click="firstAddClicked"
      color="blue-grey"
      class="ma-2 white--text"
    >
      <v-icon
        left
        dark
      >
        mdi-plus-thick
      </v-icon>
      Add card
    </v-btn>
    <div v-if="adding">
      <v-btn
        @click="secondAddClicked"
        color="blue-grey"
        class="ma-2 white--text"
        width="200px"
      >
        <v-icon
          left
          dark
        >
          mdi-plus-thick
        </v-icon>
        Add card
      </v-btn>
      <v-btn 
        icon
        @click="cancelClicked"
      >
        <v-icon color="black">mdi-close-thick</v-icon>
      </v-btn>
    </div>
  </v-card>
</template>

<script>
export default {
    props: {
        column: null,
    },

    data() {
        return {
            adding: false,
            cardTitle: "",
        };
    },

    methods: {
        firstAddClicked() {
            this.cardTitle = "";
            this.adding = true;
            this.setFocusOnTextField();
        },

        cancelClicked() {
            this.adding = false;
        },

        secondAddClicked() {
            const cardTitle = this.cardTitle.trim();
            if(cardTitle.length == 0) return;

            console.log("Adding card: " + this.cardTitle);
            this.column.cards.push({title: cardTitle});
            this.addCard(cardTitle)
            this.cardTitle = "";
            this.setFocusOnTextField();
        },

        setFocusOnTextField() {
            setTimeout(() => {  this.$refs.nameField.focus(); }, 50);
        },

        addCard(cardTitle) {
            this.axios
                .post(`/boards/${this.column.board_id}/columns/${this.column.id}/cards`, {title: cardTitle})
                .then((res) => {
                console.log("Card added")
                });
            }
    },
};
</script>
