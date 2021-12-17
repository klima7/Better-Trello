<template>
	<v-dialog 
		max-width="1000px"
		v-model="value" 
		@click:outside="dialogClosed">
			<!-- <v-card>
				<v-card-title> -->
					<v-container fluid class="grey lighten-3">
						<!-- title -->
						<v-row class="mb-0"> 
							<!-- <v-col> -->
							<v-col v-if="!titleEdit" class="d-flex pb-2">
								<v-icon style="vertical-align: baseline" color="black">mdi-card-text-outline</v-icon>
							<!-- </v-col> -->
							<!-- <div > -->
								<span class="ml-2 text-h6">{{ card.title }}</span>
								<v-btn icon class="ml-0" @click="titleEditClicked()">
									<v-icon color="black">mdi-pencil</v-icon>
								</v-btn>
							<!-- </div> -->
							</v-col>
							<v-col v-else class="d-flex">
								<v-icon style="vertical-align: baseline" color="black">mdi-card-text-outline</v-icon>
								<v-form class="mb-3 ml-2 d-flex" >
										<!-- <v-row>
									<v-col> -->
											<v-text-field
												dense
												hide-details
												outlined
												type="text"
												v-model="newTitle"
												style="background: white; "
												/>
												<v-btn icon class="ml-2" @click="titleEditAccepted">
												<v-icon color="black">mdi-check</v-icon>
												</v-btn>
												<v-btn icon @click="titleEditRejected">
												<v-icon color="black">mdi-close</v-icon>
												</v-btn>
										<!-- </v-col>
											</v-row> -->
								</v-form>
						</v-col>
						</v-row>
						<!-- <v-row class="my-0 ml-5">
							<v-col class="py-0 subtitle-1 light-gray">
								on column <a href="http://www.google.com">{{ card.column.name }}</a>
							</v-col>
						</v-row> -->
				<!-- </v-card-title> -->
				<!-- <v-card-subtitle class="ml-8"> -->
				<!-- </v-card-subtitle> -->
				<!-- <v-card-text> -->
						<v-row>
							<v-col class="py-0">
								<!-- <v-row> -->
									<v-icon style="vertical-align: top" class="d-inline-block" color="black">mdi-text-long</v-icon>
									<span class="text-h6 ml-2">Description</span>
									<v-btn v-if="!descriptionEdit" small class="mx-2" @click="descriptionEditClicked()">
										Edit
										<!-- <v-icon color="black">mdi-pencil</v-icon> -->
									</v-btn>
							<!-- </v-row> -->
							</v-col>
						</v-row>
						<v-row class="mb-0">
							<v-col  class="pt-0 my-2 ml-6">
						<!-- class="d-inline-block"  -->
						<div id="desc_edit" class="ml-2 mr-8">
							<div v-if="!descriptionEdit" style="white-space: pre;">{{card.description}}</div>
							<v-form v-else>
								<v-textarea
									hide-details
									outlined
									type="text"
									v-model="newDescription"
									style="background: white; width: 100%;"
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
								<v-icon style="vertical-align: baseline" class="d-inline-block" color="black">mdi-comment-outline</v-icon>
								<span class="text-h6 ml-2">Comments</span>
								<!-- <h3>Aktywność</h3> -->
							</v-col>
						</v-row>
						<v-row>
							<v-col class="ml-8">
								<CardComment
									:card="card"
								/>
							</v-col>
						</v-row>
						<v-btn @click="dialogClosed">Close</v-btn>
					</v-container>
				<!-- </v-card-text> -->
			<!-- <v-card-text> -->
			<!-- </v-card-text>
			</v-card> -->
	</v-dialog>
</template>

<script>

import CardComment from "@/components/CardComment.vue";

export default {
	props: {
		// detailsVisible: Boolean,
		value: Boolean,
		card: Object
	},
	data() { // temporary
		return {
			visibleA: this.visible,

			titleEdit: false,
			newTitle: this.card.title,

			descriptionEdit: false,
			newDescription: "",
		}
	},
	components: {
		CardComment	
	},
	methods: {
		dialogClosed: function (event) {
			this.titleEdit = false;
			this.descriptionEdit = false;
			this.$emit('visibility-change', false);
		},
		
		titleEditClicked: function() {
			this.titleEdit = true;
			this.newTitle = this.card.title;
		},

		titleEditAccepted: function() {
			if (this.newTitle.length > 0) {
				this.axios
				.patch('/cards/' + this.card.id, {title: this.newTitle})
				.then((res) => {
					this.card.title = this.newTitle;
					this.titleEdit = false;
				});
			}
		},

		titleEditRejected: function() {
			this.titleEdit = false;
		},

		descriptionEditClicked: function() {
			this.descriptionEdit = true;
			this.newDescription = this.card.description;
		},

		descriptionEditAccepted: function() {
			if (this.newDescription.length > 0) {
				this.axios
				.patch('/cards/' + this.card.id, {description: this.newDescription})
				.then((res) => {
					this.card.description = this.newDescription;
					this.descriptionEdit = false;
				});
			}
		},

		descriptionEditRejected: function() {
			this.descriptionEdit = false;
		},
	}
}
</script>