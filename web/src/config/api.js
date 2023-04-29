const config = {
	dev: {
		api: 'http://192.168.31.49:8000/'
	},
	prod: {
		api: ''
	}
}

let current = config.dev;

if (process.env.NODE_ENV === 'production') {
	current = config.prod;
}

console.log('api endpoint: ' + current.api);

export default current;