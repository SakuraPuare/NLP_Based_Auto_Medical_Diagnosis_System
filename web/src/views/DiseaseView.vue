<template>

    <div>
        <el-header>
            <TopMenu/>
        </el-header>
        <div v-if="id !== 'list'" class="grid grid-cols-12 text-justify mb-10">
            <div class="col-start-5 col-span-4 text-center mb-5 p-8">
                <h1>{{ data.name }}</h1>
            </div>
            <div class="col-start-4 col-span-6 rounded-lg border shadow indent-4">
                <el-collapse>
                    <el-collapse-item title="疾病概述">
                        <div class="indent-4 text-base m-4">
                            {{ data.overview }}
                        </div>
                    </el-collapse-item>
                </el-collapse>
            </div>
            <div class="col-start-4 col-span-6 rounded-lg border shadow indent-4">
                <el-collapse>
                    <el-collapse-item title="疾病病因">
                        <div class="indent-4 text-base m-4">
                            {{ data.reason }}
                        </div>
                    </el-collapse-item>
                </el-collapse>
            </div>
            <div class="col-start-4 col-span-6 rounded-lg border shadow indent-4">
                <el-collapse>
                    <el-collapse-item title="疾病预防">
                        <div class="indent-4 text-base m-4">
                            {{ data.prevention }}
                        </div>
                    </el-collapse-item>
                </el-collapse>
            </div>
            <div class="col-start-4 col-span-6 rounded-lg border shadow indent-4">
                <el-collapse>
                    <el-collapse-item title="疾病治疗">
                        <div class="indent-4 text-base m-4">
                            {{ data.treatment }}
                        </div>
                    </el-collapse-item>
                </el-collapse>
            </div>
            <div class="col-start-4 col-span-6 rounded-lg border shadow indent-4">
                <el-collapse>
                    <el-collapse-item title="疾病并发症">
                        <div class="indent-4 text-base m-4">
                            {{ data.complication }}
                        </div>
                    </el-collapse-item>
                </el-collapse>
            </div>
        </div>
        <div v-else class="grid grid-cols-12 text-justify mb-10">
            <div class="col-start-5 col-span-4 text-center mb-5 p-8">
                <h1>疾病列表</h1>
            </div>
            <div class="col-start-4 col-span-6 rounded-lg border shadow indent-4">
                <div class="overflow-auto max-h-max">
                    <ul>
                        <li v-for="item in data" class="text-base p-2 shadow">
                            <el-link :href="'/disease/' + item.id">{{ item.id }}: {{ item.name }}</el-link>
                            <!--                        <router-link :to="'/disease/' + item.id"></router-link>-->
                        </li>

                    </ul>
                </div>
            </div>

            <div class="col-start-4 col-span-6 rounded-lg border shadow my-5 py-2">
                <el-pagination
                        v-model:current-page="current_page"
                        v-model:page-size="current_size"
                        :page-sizes="[10,20,30,40,50]"
                        :total="7825"
                        class="justify-center"
                        layout="total, sizes, prev, pager, next, jumper"
                        @current-change="reload"
                        @size-change="reload"
                />
            </div>
        </div>
    </div>


</template>

<script setup>

import TopMenu from "../components/Menu/TopMenu.vue";
import api from "../config/api.js";
import {computed, ref} from "vue";
import {useRoute} from 'vue-router'
import http from "../plugin/http.js";

const baseURL = api.api
const id = computed(() => useRoute().params.id)
const data = ref()
const current_page = ref(1)
const current_size = ref(10)

const reload = () => {
	get_list(current_size.value, (current_page.value - 1) * current_size.value)
}

// const load_more = () => {
// 	get_list(10, data.value.length)
// }

function get_list(limit, offset) {
	http.get(baseURL + 'disease/list/', {
		params: {
			limit: limit,
			offset: offset
		}
	})
		.then((res) => {
			let x = []
			for (let i = 0; i < res.data.data.length; i++) {
				let t = {
					id: res.data.data[i][0],
					name: res.data.data[i][1]
				}
				x.push(t)
			}
			data.value = x
		})
		.catch((err) => {
			console.log(err)
		})
}

if (id.value === 'list') {
	data.value = []
	reload()
} else {
	data.value = ''
	http.get(baseURL + 'disease/' + id.value + '/')
		.then((res) => {
			data.value = res.data.data;
			console.log(data)
		})
		.catch((err) => {
			console.log(err)
		})
}


</script>

<style scoped>

</style>