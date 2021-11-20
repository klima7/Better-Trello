<template>
	<v-container>
		<v-card>
			<v-card-title>
				Board id {{ id }}
			</v-card-title>
			<v-card-text>
				Yoo mike, you want us to unpimp this thing let me hear you say what.
			</v-card-text>
		</v-card>
	</v-container>
</template>

<script>
export default {
	data() {
		return {
			id: this.$route.params.board_id
		}
	}
}
</script>