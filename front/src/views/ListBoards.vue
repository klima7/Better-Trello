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
					v-on:click="boardSelected(board.id)"
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
	export default {
		data() {
			return {
				boards: [
					{id: 0, name: "Jacek"},
					{id: 73, name: "Stasiak"},
					{id: 72, name: "baby a triple"}
				]
			}
		},
		methods: {
			boardSelected(id) {
				alert("nie wiem czy to będzie potrzebne tutaj: " + id);
			}
		}
	}
</script>