<template>
    <div class="text-center">
        <el-header>
            <TopMenu/>
        </el-header>


        <div class="pt-20">
            <Lottie :height="250" name="Thinking-face"/>
        </div>
        <div class="py-5">
            <h1>找不到你想要的东西</h1>
        </div>
        <div class="text-base">
            <router-link to="/">回到首页</router-link>
        </div>

    </div>
</template>
<script setup>
import TopMenu from "../../components/Menu/TopMenu.vue";
import Lottie from "../../components/Lottie.vue";
</script>