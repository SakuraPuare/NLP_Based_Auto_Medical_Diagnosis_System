<template>
    <header>
        <el-menu :default-active="activeIndex" :ellipsis="false" mode="horizontal" router>
            <el-menu-item index="1" route="/">
                智能医疗系统
            </el-menu-item>
            <el-menu-item class="hidden-sm-and-down" index="home" route="/">首页</el-menu-item>
            <el-menu-item class="hidden-sm-and-down" index="disease" route="/disease">疾病信息</el-menu-item>
            <el-menu-item class="hidden-sm-and-down" index="symptom" route="/symptom">症状信息</el-menu-item>
            <el-menu-item class="hidden-sm-and-down" index="drug" route="/drug">药品信息</el-menu-item>
        </el-menu>
    </header>
</template>

<script setup>
import 'element-plus/theme-chalk/display.css'
import {useRoute} from "vue-router"

const route = useRoute();
const activeIndex = route.name;

</script>

<style scoped>
</style>