<template>
    <div>
      <img :src="`http://127.0.0.1:8000${profile_img}`" alt="">
      {{ profileInfo }}
    </div>
</template>

<script setup>
import { ref } from 'vue'


const props = defineProps({
  profileInfo: Object,
})

const { profileInfo } = props

const nickname = ref(profileInfo.nickname)
const profile_img = ref(profileInfo.profile_img)
const introduce = ref(profileInfo.introduce)

</script>

<style scoped>

</style>