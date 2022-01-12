<template>
	<v-dialog 
		max-width="1000px"
		v-model="value"
		@click:outside="closeDialog"
		v-if="board">
		<v-container fluid class="white">
			<v-row>
				<v-col>
					<h1>Udostępnianie tablicy <i>{{board['name']}}</i></h1>
				</v-col>
			</v-row>
			<v-row>
				<v-col>
					<v-form class="d-flex" >
								<v-text-field
									dense
									hide-details
									outlined
									type="text"
									v-model="newUser"
									style="background: white; "
									/>
									<v-btn class="ml-2" @click="addUser">
										Dodaj użytkownika
									</v-btn>
					</v-form>
					<v-alert
						class="mt-3"
						v-model="error_visible" 
						color="red"
						border="left"
						dismissible
						>
						{{ error_msg }}</v-alert>
				</v-col>
			</v-row>
			<v-row>
				<v-col class="pb-0">
					<h3>Użytkownicy posiadający dostęp</h3>
				</v-col>
			</v-row>
			<v-row>
				<v-col class="pt-0">
					<v-list>
						<v-list-item v-for="user in board.shared_users" :key="user">
							<v-list-item-content>
								{{ user }}
							</v-list-item-content>
							<v-list-item-action>
								<v-tooltip left>
									<template v-slot:activator="{on, attrs}">
										<v-btn 
											v-bind="attrs"
											v-on="on"
											@click="removeUser(user)"
											icon>
											<v-icon>mdi-account-remove</v-icon>
										</v-btn>
									</template>
									<span>Usuń użytkownika z listy</span>
								</v-tooltip>
							</v-list-item-action>
						</v-list-item>
					</v-list>
				</v-col>
			</v-row>
			<v-btn @click="closeDialog">Zamknij</v-btn>
		</v-container>
	</v-dialog>
</template>

<script>
export default {
	props: {
		value: Boolean,
		board: Object
	},
	data() {
		return {
			error_visible: false,
			error_msg: "",
			mboard: this.board,
			sharing_dialog_opened: true,
			newUser: ""
		};
	},
	methods: {
		closeDialog: function(event) {
			this.$emit('hide', false);
		},
		addUser: function() {
			this.axios.post(`/boards/${this.board.id}/share`, {email: this.newUser})
			.then((res) => {
				console.log("Sharing succeded");
			})
			.catch((err) => {
				console.log(err);
				this.error_visible = true;
				this.error_msg = "Błąd podczas dodwania użytkownika. Upewnij się, że wpisany email jest poprawny."
			});
		},
		removeUser: function(u) {
			console.log("removing " + u);
			this.axios.post(`/boards/${this.board.id}/sharestop`, {email: u})
			.then((res) => {
				console.log("deleting succeded");
			})
			.catch((err) => {
				console.log(err);
				this.error_visible = true;
				this.error_msg = "Błąd podczas usuwania użytkownika."
			});
		}
	}
}
</script>