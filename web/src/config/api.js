const config = {
	dev: {
		api: 'http://localhost:8000/'
	},
	prod: {
		api: 'https://medical.sakurapuare.com/api/'
	}
}

let current = config.prod;

if (process.env.NODE_ENV === 'production') {
	current = config.prod;
}

console.log('api endpoint: ' + current.api);

export default current;