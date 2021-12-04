<template>
	<v-dialog v-model="value" @click:outside="dialogClosed">
		<!-- > -->
		<!-- <template v-slot:activator="{ on, attrs }">
			<v-btn
				color="red lighten-2"
				dark
				v-bind="attrs"
				v-on="on"
				>
			Click Me
			</v-btn>
		</template> -->

		<v-card>
			<v-card-title>
				{{ name }}
			</v-card-title>
			<v-card-text>
				{{ description }}
				{{ visibleA }}, {{value}}
				<v-btn @click="dialogClosed">close</v-btn>
			</v-card-text>
		</v-card>
	</v-dialog>
</template>

<script>
export default {
	props: {
		// detailsVisible: Boolean,
		value: Boolean
	},
	data() { // temporary
		return {
			visibleA: this.value,
			name: "not a priority",
			description: "it's a good car."
		}
	},
	methods: {
		dialogClosed: function (event) {
			// this.detailsVisible = false;
			console.log("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
			this.$emit('input', false);
		}
	}
}
</script>