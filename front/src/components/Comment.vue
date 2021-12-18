<template>
		<v-row>
			<v-col md="auto">
				<v-avatar
					color="primary"
					size="40">
				<span class="white--text text-h6">{{ comment.user.substring(0, 2) }}</span>
				</v-avatar>
			</v-col>
			<v-col>
				<v-row>
					<h4>{{comment.user}}</h4>
				</v-row>
				<v-row>
					<span v-if="!comment_edit">{{comment.content}}</span>
					<v-form class="mb-2" v-if="comment_edit" style="width: 100%">
						<v-textarea 
							class="mb-2" 
							v-model="comment_edit_value"
							rows="4"
							solo 
							hide-details
							outlined
							></v-textarea>

						<v-btn @click="confirmEdit" color="primary" small>Confirm</v-btn>
						<v-btn @click="abortEdit" small text class="ml-2">Discard</v-btn>
					</v-form>
				</v-row>
				<v-row v-if="!comment_edit && userowned">
					<v-btn text small color="primary" @click="edit">Edit</v-btn>
					<!-- <v-btn text small color="primary" @click="deleteComment">Delete</v-btn> -->
					<v-dialog
						v-model="delete_confirm"
						width="300"
						hide-overlay
						>
						<template v-slot:activator="{on, attrs}">
							<v-btn 
								v-on="on"
								v-bind="attrs"
								color="primary"
								class="ml-2"
								small 
								text>Delete</v-btn>
						</template>
						<v-card>
							<v-card-title>
								Delete comment?
							</v-card-title>
							<v-card-text>
								Deleting a comment is irreversible.
							</v-card-text>
							<v-card-actions>
								<v-btn color="red accent-4" @click="deleteComment">Delete</v-btn>
							</v-card-actions>
						</v-card>
					</v-dialog>
				</v-row>
			</v-col>
		</v-row>
</template>

<script>
export default {
	props: {
		comment: Object,
		card: Object,
		userowned: Boolean
	},
	data() {
		return {
			comment_input: "",
			comment_edit_value: "",
			comment_edit: false,
			user: this.$store.getters.user
		}
	},
	methods: {
		deleteComment: function() {
			this.axios
			.delete(`/cards/${this.card.id}/comment/${this.comment.id}`)
			.then((res) => {
			})
			.catch((err) => {
				console.log("Error when deleting comment");
			})
		},
		edit: function() {
			this.comment_edit = true;
			this.comment_edit_value = this.comment.content;
		},
		abortEdit: function() {
			this.comment_edit = false;
		},
		confirmEdit: function() {
			this.axios
			.patch(`/cards/${this.card.id}/comment/${this.comment.id}`, {content: this.comment_edit_value})
			.then((res) => {
				this.comment.content = this.comment_edit_value;
				this.comment_edit = false;
			})
			.catch((err) => {
				console.log("Error when updating comment");
			})
		}
	}
};
</script>