import axios from "axios";
import api from '../config/api.js'

const baseURL = api.api;
let instance = axios.create({
	baseURL: baseURL, timeout: 10000,
})

instance.interceptors.response.use((res) => {
	return Promise.resolve(res)
}, (error) => {

	console.error('axios error', error)
	// redirect to 404 page
	if (error.response.status === 404) {
		window.location.href = '/404'
	}
	let data = []
	if (error.response.data.data) {
		data = error.response.data.data
	}
	if (error.response.data.message) {
		data = error.response.data.message
	}

	if (error.response.data.error) {
		data = error.response.data.error.message
	}

	console.error('axios error', error)

	return Promise.reject(error)
})

export default instance
