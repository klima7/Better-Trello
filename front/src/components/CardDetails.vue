<template>
	<v-dialog 
		max-width="1000px"
		v-model="value" 
		@click:outside="dialogClosed">
			<v-card>
				<v-card-title>
					<v-container fluid>
						<v-row align="center">
								<v-row v-if="!titleEdit">
									<v-icon style="vertical-align: top" color="black">mdi-card-text-outline</v-icon>
								<!-- <div > -->
									<span class="ml-2">{{ card.title }}</span>
									<v-btn icon class="ml-4" @click="titleEditClicked()">
										<v-icon color="black">mdi-pencil</v-icon>
									</v-btn>
								<!-- </div> -->
								</v-row>
								<v-row v-else>
								<v-form>
									<v-text-field
										dense
										hide-details
										outlined
										type="text"
										v-model="newTitle"
										style="background: white; width: 250pt;"
										/>
										<v-btn icon class="ml-2" @click="titleEditAccepted">
										<v-icon color="black">mdi-check</v-icon>
										</v-btn>
										<v-btn icon @click="titleEditRejected">
										<v-icon color="black">mdi-close</v-icon>
										</v-btn>
								</v-form>
								</v-row>
						</v-row>
					</v-container>
				</v-card-title>
				<v-card-subtitle class="ml-8">
					on board <a href="http://www.google.com">{{ board }}</a>
				</v-card-subtitle>
				<v-card-text>
					<v-icon style="vertical-align: top" class="d-inline-block" color="black">mdi-text-long</v-icon>
					<!-- class="d-inline-block"  -->
					<div id="desc_edit" class="d-inline-block ml-2">
						<div v-if="!descriptionEdit">
							{{ card.description }}
							<v-btn icon class="ml-4" @click="descriptionEditClicked()">
								<v-icon color="black">mdi-pencil</v-icon>
							</v-btn>
						</div>
						<v-form v-else>
							<v-textarea
								hide-details
								outlined
								type="text"
								v-model="newDescription"
								style="background: white; width: 250pt;"
								/>
								<v-btn icon class="ml-2" @click="descriptionEditAccepted">
								<v-icon color="black">mdi-check</v-icon>
								</v-btn>
								<v-btn icon @click="descriptionEditRejected">
								<v-icon color="black">mdi-close</v-icon>
								</v-btn>
						</v-form>
					</div>
				</v-card-text>
			<v-card-text>
				<v-btn @click="dialogClosed">Close</v-btn>
			</v-card-text>
			</v-card>
	</v-dialog>
</template>

<script>
export default {
	props: {
		// detailsVisible: Boolean,
		value: Boolean,
		card: Object
	},
	data() { // temporary
		return {
			visibleA: this.visible,
			name: "not a priority",
			description: "it's a good car.",
			board: "idk",
			titleEdit: false,
			newTitle: this.card.title,

			descriptionEdit: false,
			newDescription: ""
		}
	},
	methods: {
		dialogClosed: function (event) {
			// this.detailsVisible = false;
			console.log("closing dialog");
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
					console.log("WORKED");
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
					console.log("WORKED");
				});
			}
		},

		descriptionEditRejected: function() {
			this.descriptionEdit = false;
		},
	}
}
</script>