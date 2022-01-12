<template>
	<div>
		<v-form>
			<v-container>
				<v-row>
					<v-textarea
						label="Add comment"
						v-model="comment_input"
						class="mr-2"
						rows="2"
						solo 
						hide-details
						outlined
						>
						</v-textarea>
					<v-btn @click="addComment">Submit</v-btn>
				</v-row>
				<v-row>
					<v-col class="px-0">
						<v-container>
							<Comment v-for="comment in this.card.comments" :key="comment.id" :comment="comment" :card="card" :userowned="comment.user == user.email" />
						</v-container>
					</v-col>
				</v-row> 
			</v-container>
		</v-form>
	</div>
</template>

<script>

import Comment from "@/components/Comment.vue";

export default {
	props: {
		card: Object
	},
	components: {
		Comment
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
		addComment: function() {
			this.axios.post(`/cards/${this.card.id}/comment`, {content: this.comment_input})
				.then((response) => {
					console.log('Added comment: ' + this.comment_input);
					this.comment_input = "";
				})
				.catch((error) => {
					console.log('Error occurred while adding comment');
				});	
		}
	}
};
</script>