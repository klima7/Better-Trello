<template>
	<!-- <v-container
		class="py-8 px-6"
		fluid> -->
	<v-container>
		<v-card>
			<v-card-title>Lista tablic</v-card-title>
			<v-card-text>
				<!-- Add button and field -->
				<v-form ref="form">
					<v-text-field :rules="rules" hide-details="auto" label="Nazwa nowej tablicy" color="primary" v-model="new_board_name" @keypress.enter="addBoard">
						<template v-slot:append>
							<v-btn depressed tile color="primary" class="ma-0" @click="addBoard">
								Dodaj tablicę
							</v-btn>
						</template>	
					</v-text-field>
				</v-form>				
				<!-- <v-container> -->
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
			</v-card-text>
			<!-- </v-container> -->
		</v-card>
	</v-container>
</template>

<script>

	const axios = require('axios').default;

	export default {
		data() {
			return {
				new_board_name: "",
				boards: [],
				rules: [
					(value) => !!value || "Pole wymagane!",
					(value) => (value || "").length <= 40 || "Maksymalna długość nazwy tablicy: 40 znaków!",
				],
			}
		},
		methods: {
			boardSelected(id) {
				alert("nie wiem czy to będzie potrzebne tutaj: " + id);
			},
			fetchBoardList() {
				axios.get('/boards')
				.then((response) => {
					console.log(response);
					this.boards = response.data;
				})
				// eslint-disable-next-line no-unused-vars
				.catch((error) =>  {
					console.log(`Sorry sir no boards here. ${error}`);
					this.boards = [];
				})
			},
			addBoard() {
				if (this.new_board_name == '') {
					return
				}
				let data = {
					name: this.new_board_name
				};
				axios.post('/boards', data)
				.then((response) => {
					console.log('Added: ' + this.new_board_name);
					this.fetchBoardList();
					this.$refs.form.reset();
				})
				.catch((error) => {
					console.log('Error occurred while adding' + this.new_board_name);
				});	
			}
		},
		created() {
			console.log("anybody here");
			this.fetchBoardList();
		}
	}
</script>