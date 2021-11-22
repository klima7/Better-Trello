<template>
	<v-container>

        <v-row>
            <v-col>
                <h1>Lista tablic</h1>
            </v-col>
        </v-row>

        <v-row>
            <v-col>
                <v-card color="#89cff0">
                    <v-card-text>
                        <v-form ref="form">
                            <v-text-field :rules="rules" hide-details="auto" label="Nazwa nowej tablicy" color="primary" v-model="new_board_name" @keypress.enter="addBoard">
                                <template v-slot:append>
                                    <v-btn depressed tile color="primary" class="ma-0" @click="addBoard">
                                        Dodaj tablicę
                                    </v-btn>
                                </template>	
                            </v-text-field>
                        </v-form>				
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <v-row>
            <BoardTile v-for="board in boards" :key="board.id" :board="board" />
        </v-row>

	</v-container>
</template>

<script>

	const axios = require('axios').default;
	import BoardTile from "@/components/BoardTile.vue";

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
		components: {
			BoardTile
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