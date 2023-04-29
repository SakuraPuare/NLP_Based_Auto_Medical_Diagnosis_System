import {createRouter, createWebHistory} from "vue-router";
import ChatView from "../views/ChatView.vue";
import DiseaseView from "../views/DiseaseView.vue";
import DrugView from "../views/DrugView.vue";
import SymptomView from "../views/SymptomView.vue";

const routes = [
	{
		path: '/',
		name: 'home',
		component: ChatView,
	},
	{
		path: '/disease/:id',
		name: 'disease',
		component: DiseaseView,
	},
	{
		path: '/disease',
		redirect: {
			name: 'disease',
			params: {
				id: 'list'
			}
		}
	},
	{
		path: '/drug/:id',
		name: 'drug',
		component: DrugView,
	},
	{
		path: '/drug',
		redirect: {
			name: 'drug',
			params: {
				id: 'list'
			}
		}
	},
	{
		path: '/symptom/:id',
		name: 'symptom',
		component: SymptomView,
	},
	{
		path: '/symptom',
		redirect: {
			name: 'symptom',
			params: {
				id: 'list'
			}
		}
	},
	{
		path: '/404',
		name: '404',
		component: () => import('../views/error/404.vue'),
	}
]

const router = createRouter({
	history: createWebHistory(),
	routes
})

// router.beforeEach((to,from,next)=>{
// //需要授权且用户没有登录
// 	if(to.meta.requestAuth&&!store.state.user.is_login){
// 		next({name:"user_account_login"});
// 	}else{
// 		next();
// 	}
// })

export default router