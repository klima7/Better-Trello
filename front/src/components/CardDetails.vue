<template>
  <v-dialog max-width="1000px" v-model="value" @click:outside="dialogClosed">
    <v-container fluid class="grey lighten-3">
    <v-card-text v-if="card.labels.length != 0">
        <v-row>
      <Label
        v-for="label in card.labels"
        :key="label.id"
        :label="label"
        :card="card"
        :closeable="true"
        />

      <!-- Add button -->
      <v-chip
        color="black"
        label
        text-color="white"
        v-on:click="showLabelsDialog"
      >
        <v-icon left>
          mdi-plus
        </v-icon>
        Add label
      </v-chip>

    </v-row>
    </v-card-text>

      <!-- title -->
      <v-row class="mb-0">
        <v-col v-if="!titleEdit" class="d-flex pb-2">
          <v-icon style="vertical-align: baseline" color="black"
            >mdi-card-text-outline</v-icon
          >
          <span class="ml-2 text-h6">{{ card.title }}</span>
          <v-btn icon class="ml-0" @click="titleEditClicked()">
            <v-icon color="black">mdi-pencil</v-icon>
          </v-btn>
          <!-- Archive button -->
          <v-btn icon class="ml-0" @click="archiveAddClicked()">
            <v-icon color="black">mdi-archive-plus</v-icon>
          </v-btn>
        </v-col>
        <v-col v-else class="d-flex">
          <v-icon style="vertical-align: baseline" color="black"
            >mdi-card-text-outline</v-icon
          >
          <v-form class="mb-3 ml-2 d-flex">
            <v-text-field
              dense
              hide-details
              outlined
              type="text"
              v-model="newTitle"
              style="background: white"
            />
            <v-btn icon class="ml-2" @click="titleEditAccepted">
              <v-icon color="black">mdi-check</v-icon>
            </v-btn>
            <v-btn icon @click="titleEditRejected">
              <v-icon color="black">mdi-close</v-icon>
            </v-btn>
          </v-form>
        </v-col>
      </v-row>

      <!-- Labels -->
      <!-- <v-row>
        <v-col class="py-0">
      <v-row>
      <Label
        v-for="label in card.labels"
        :key="label.id"
        :label="label"
        :closeable="false"
        />
        </v-row>
          <v-btn depressed>Add label</v-btn>
        </v-col>
      </v-row> -->

      <v-row>
        <v-col class="py-0">
          <v-icon
            style="vertical-align: top"
            class="d-inline-block"
            color="black"
            >mdi-text-long</v-icon
          >
          <span class="text-h6 ml-2">Description</span>
          <v-btn
            v-if="!descriptionEdit"
            small
            class="mx-2"
            @click="descriptionEditClicked()"
          >
            Edit
          </v-btn>
        </v-col>
      </v-row>
      <v-row class="mb-0">
        <v-col class="pt-0 my-2 ml-6">
          <div id="desc_edit" class="ml-2 mr-8">
            <div v-if="!descriptionEdit" style="white-space: pre">
              {{ card.description }}
            </div>
            <v-form v-else>
              <v-textarea
                hide-details
                outlined
                type="text"
                v-model="newDescription"
                style="background: white; width: 100%"
              />
              <v-btn icon class="ml-2" @click="descriptionEditAccepted">
                <v-icon color="black">mdi-check</v-icon>
              </v-btn>
              <v-btn icon @click="descriptionEditRejected">
                <v-icon color="black">mdi-close</v-icon>
              </v-btn>
            </v-form>
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-icon
            style="vertical-align: baseline"
            class="d-inline-block"
            color="black"
            >mdi-comment-outline</v-icon
          >
          <span class="text-h6 ml-2">Comments</span>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ml-8">
          <CardComment :card="card" />
        </v-col>
      </v-row>
      <v-btn @click="dialogClosed">Close</v-btn>
    </v-container>
  </v-dialog>
</template>

<script>
import CardComment from "@/components/CardComment.vue";
import Label from "./Label.vue";

export default {
  props: {
    value: Boolean,
    card: Object,
    board: Object,
  },
  data() {
    // temporary
    return {
      visibleA: this.visible,

      titleEdit: false,
      newTitle: this.card.title,

      descriptionEdit: false,
      newDescription: "",
    };
  },
  components: {
    CardComment,
    Label,
  },
  methods: {
    dialogClosed: function (event) {
      this.titleEdit = false;
      this.descriptionEdit = false;
      this.$emit("visibility-change", false);
    },

    titleEditClicked: function () {
      this.titleEdit = true;
      this.newTitle = this.card.title;
    },

    archiveAddClicked: function () {
      this.axios
        .post("/cards/" + this.card.id + "/archive", {state: true})
        .then((res) => {
          this.$emit("card-archive-change");
          this.dialogClosed();
      });
    },

    titleEditAccepted: function () {
      if (this.newTitle.length > 0) {
        this.axios
          .patch("/cards/" + this.card.id, { title: this.newTitle })
          .then((res) => {
            this.card.title = this.newTitle;
            this.titleEdit = false;
          });
      }
    },

    titleEditRejected: function () {
      this.titleEdit = false;
    },

    descriptionEditClicked: function () {
      this.descriptionEdit = true;
      this.newDescription = this.card.description;
    },

    descriptionEditAccepted: function () {
      if (this.newDescription.length > 0) {
        this.axios
          .patch("/cards/" + this.card.id, { description: this.newDescription })
          .then((res) => {
            this.card.description = this.newDescription;
            this.descriptionEdit = false;
          });
      }
    },

    descriptionEditRejected: function () {
      this.descriptionEdit = false;
    },

    showLabelsDialog: function() {
      console.log("Showting labels dialog")
      this.$emit('show-labels-dialog', this.card.id);
    }
  },
};
</script>