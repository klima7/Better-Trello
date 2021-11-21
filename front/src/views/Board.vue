<template>
	<v-container>
			<h1>{{ board_info.board_name }}</h1>
			<v-container class="d-flex flex-row pr-6 pt-3" >
				<v-card
					v-for="column in board_info.columns"
					class="d-flex flex-column pt-3 mr-6 list"
					v-bind:key="column.name">
					<h2 class="ms-3">{{column.name}}</h2>
					<v-container>
						<v-card
							v-for="card in column.cards"
							class="mb-3"
							v-bind:key="card.title">
							<v-card-title>{{card.title}}</v-card-title>
							<v-card-text>{{card.description}}</v-card-text>
						</v-card>
					</v-container>
				</v-card>
			</v-container>
	</v-container>
</template>

<script>
	const axios = require('axios').default;
	export default {
		data() {
			return {
				id: this.$route.params.board_id,
				board_info: []
			}
		},
		methods: {
			fetchBoardInfo() {
				if (this.id == null) {
					return
				}
				let data = {
					id: this.id
				};
				axios.post('/info', data)
				.then((response) => {
					console.log('Successfully fetched board with id: ' + this.id)
					this.board_info = response.data
				})
				.catch((error) => {
					console.log('Error occurred while fetching board with id: ' + this.id);
				});
			}
		},
		created() {
			this.fetchBoardInfo();
		}
	}
</script>