<template>
    <div :id="id" :style="style"></div>
</template>

<script setup>
import lottie from 'lottie-web'

import {onMounted, onUnmounted, ref} from 'vue'

//
const id = ref('lottie-' + Math.random().toString(36).substring(3, 13))


const props = defineProps({
	name: {
		type: String,
		required: true
	},
	autoplay: {
		type: Boolean,
		default: true
	},
	loop: {
		type: Boolean,
		default: true
	},
	height: {
		type: Number,
		default: 128
	},
	width: {
		type: Number,
		default: 0
	},
	center: {
		type: Boolean,
		default: true
	},
	style: {
		type: Object,
		default: () => {
			return {}
		}
	}
})


const container = ref(null)

const animation = ref(null)

let options = {}

const src = '/assets/lottie/' + props.name + '.json'

onMounted(() => {
	// get dom
	container.value = document.getElementById(id.value)

	// set height
	container.value.style.height = props.height + 'px'

	// if width
	if (props.width) {
		container.value.style.width = props.width + 'px'

	}

	// set center(text center)
	if (props.center) {
		container.value.style.textAlign = 'center'
	}

	options = {
		container: container.value,
		renderer: 'svg',
		loop: props.loop,
		autoplay: props.autoplay,
		path: src,
	}

	animation.value = lottie.loadAnimation(options)

})

onUnmounted(() => {
	if (animation.value !== null) {
		animation.value.destroy()
	}
})


</script>

<style scoped>

</style>