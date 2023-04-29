<template>
    <div class="text-justify">
        <el-header>
            <TopMenu/>
        </el-header>
        <div class="grid grid-cols-12 text-justify ">
            <div class="col-start-5 col-span-4 text-center mb-5 p-8">
                <h1>智能医疗诊断系统</h1>
            </div>

            <div class="col-start-4 col-span-6">
                <el-input v-model="question" clearable placeholder="请输入症状！"/>
            </div>

            <div class="col-start-4 col-span-6 pt-10 pb-10 text-center">
                <el-button :icon="Promotion" :loading="loading" bg plain type="primary" @click="send">
                    发送
                </el-button>
                <el-button :icon="Refresh" bg plain type="success" @click="refresh">
                    看看
                </el-button>
                <el-button :icon="CloseBold" bg plain type="danger" @click="remove">
                    清除
                </el-button>
            </div>

            <div class="col-start-4 col-span-6 p-5 mb-10 rounded indent-8 shadow-lg leading-relaxed text-base text-justify">
                {{ answer }}
            </div>

        </div>
    </div>

</template>
<script setup>
import TopMenu from "../components/Menu/TopMenu.vue";
import {ref} from "vue";
import api from "../config/api.js";
import http from "../plugin/http.js";
import {CloseBold, Promotion, Refresh} from "@element-plus/icons-vue";
import get_question from "../data/question.js";

const baseURL = api.api

const question = ref(get_question());
const answer = ref("请向我提问吧！");
const loading = ref(false);
let last = "";
const send = () => {
	// add attribute loading on button
	loading.value = true;

	if (question.value === last) {
		loading.value = false;
		return;
	} else if (question.value === "") {
		loading.value = false;
		return;
	}

	http.get(baseURL + 'query', {
		params: {
			message: question.value
		}
	})
		.then((res) => {
			last = question.value;
			answer.value = res.data.data;
			loading.value = false;
		})
		.catch((err) => {
			console.log(err)
		})
}
const refresh = () => {
	question.value = get_question()
	send()
}
const remove = () => {
	answer.value = "请向我提问吧！";
	question.value = "";
}


// listen to enter key
document.onkeydown = function (e) {
	if (e.key === 'Enter') {
		send();
	}
}

</script>
<style scoped>

</style>