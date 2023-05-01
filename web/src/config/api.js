const config = {
	dev: {
		api: 'http://test.sakurapuare.com/'
	},
	prod: {
		api: 'https://medical.sakurapuare.com/api/'
	}
}

let current = config.prod;

console.log('api endpoint: ' + current.api);

export default current;