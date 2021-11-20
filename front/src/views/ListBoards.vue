<template>
	<v-container
		class="py-8 px-6"
		fluid>
		<v-card>
			<v-subheader>Lista tablic</v-subheader>
			<v-container
					class="px-8">
				<v-btn> Nowa tablica idk?</v-btn>
				<v-list 
					two-line 
					v-for="board in boards" 
					:key="board.id">

					<v-list-item 
					:key="board.id"
					:to="'/board/' + board.id"
					link>
						<v-list-item-content>
							<v-list-item-title> {{ board.name }} </v-list-item-title>
							<!-- <v-list-item-subtitle>huh?</v-list-item-subtitle> -->
						</v-list-item-content>
					</v-list-item>
					<v-divider v-if="board.id != boards[boards.length-1].id" :key="`divider-${board.id}`"></v-divider>
				</v-list>
			</v-container>
		</v-card>
	</v-container>
</template>

<script>

	const axios = require('axios').default;

	export default {
		data() {
			return {
				boards: []
			}
		},
		methods: {
			boardSelected(id) {
				alert("nie wiem czy to będzie potrzebne tutaj: " + id);
			},
			fetchBoardList() {
				axios.get('/boards/1')
				.then((response) => {
					console.log(response);
					this.boards = response.data;
				})
				// eslint-disable-next-line no-unused-vars
				.catch((error) =>  {
					console.log(`Sorry sir no boards here. ${error}`);
					this.boards = [];
				})
			}
		},
		created() {
			console.log("anybody here");
			this.fetchBoardList();
		}
	}
</script>