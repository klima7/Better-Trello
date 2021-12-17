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
					<v-form v-if="comment_edit" style="width: 100%">
						<v-textarea 
							v-model="comment_edit_value"
							solo 
							hide-details
							outlined
							></v-textarea>

						<v-btn @click="confirmEdit" small text>Yes</v-btn>
						<v-btn @click="abortEdit" small text class="ml-2">No</v-btn>
					</v-form>
				</v-row>
				<v-row v-if="!comment_edit && userowned">
					<v-btn text small color="primary" @click="edit()">Edit</v-btn>
					<v-btn text small color="primary">Delete</v-btn>
				</v-row>
				<!-- <v-list-item-content>
					<v-list-item-title v-text="comment.user"></v-list-item-title>
					<v-list-item-subtitle v-text="comment.content"></v-list-item-subtitle>
				</v-list-item-content> -->
			</v-col>
		</v-row>
</template>

<script>
export default {
	props: {
		comment: Object,
		userowned: Boolean
	},
	data() {
		return {
			// comments: [
			// 	{user: "aba", content: "kici kici"},
			// 	{user: "bab", content: "ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci "}],
			comment_input: "",
			comment_edit_value: "",
			comment_edit: false,
			user: this.$store.getters.user
		}
	},
	methods: {
		edit: function() {
			this.comment_edit = true;
			this.comment_edit_value = this.comment.content;
		},
		abortEdit: function() {
			this.comment_edit = false;
		},
		confirmEdit: function() {
			this.comment_edit = false;
			this.comment.content = this.comment_edit_value;
		}
	}
};
</script>