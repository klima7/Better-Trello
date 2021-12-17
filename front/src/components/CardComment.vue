<template>
	<div>
		<v-form>
			<v-container>
				<v-row>
					<!-- <v-col class="py-0"> -->
					<v-text-field
						label="Add comment"
						v-model="comment_input">
						</v-text-field>
					<v-btn>Submit</v-btn>
							<!-- <v-btn> aha!</v-btn> -->
					<!-- </v-col>
					<v-col md="auto" class="py-0"> -->
					<!-- </v-col> -->
				</v-row>
				<v-row>
					<v-col>
						<v-container>
							<Comment v-for="comment in comments" :key="comment.user" :comment="comment" :userowned="true" />
							<!-- <v-row v-for="comment in comments" :key="comment.user">
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
									</v-row>
									<v-row v-if="!comment_edit && email != comment.user">
										<v-btn text small color="primary" @click="edit()">Edit</v-btn>
										<v-btn text small color="primary">Delete</v-btn>
									</v-row>
									/// <v-list-item-content>
										<v-list-item-title v-text="comment.user"></v-list-item-title>
										<v-list-item-subtitle v-text="comment.content"></v-list-item-subtitle>
									</v-list-item-content> ///
								</v-col>
							</v-row>-->
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
			comments: [
				{user: "aba", content: "kici kici"},
				{user: "bab", content: "ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci ci "}],
			comment_input: "",
			comment_edit_value: "",
			comment_edit: false,
			user: this.$store.getters.user
		}
	}
};
</script>