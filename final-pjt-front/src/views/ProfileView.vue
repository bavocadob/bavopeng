<template>
    <div class="w-full h-screen bg-slate-400">
      <div>
        <div class="flex">
          <div class="w-40">
            <img :src="`http://127.0.0.1:8000${profileInfo.profile_img}`" alt="">
          </div>
        </div>
      </div>
        <input type="file" ref="fileInput">
        <button @click="upload">dd</button>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useUserStore } from '../stores/user'
import UserProfile from '@/components/UserProfile.vue'
import UserPreference from '@/components/UserPreference.vue'
import UserRecord from '@/components/UserRecord.vue'
import axios from 'axios'

const route = useRoute()
const store = useUserStore()

const username = route.params.username
const profileInfo = ref({})
const preferenceInfos = ref({})
const records = ref({})

axios({
  method: 'get',
  url: `http://127.0.0.1:8000/api/v1/profile/${username}/`,
})
  .then((res) => {
    // console.log(res.data)
    const data = res.data
    profileInfo.value = {
      id: data.user.id,
      nickname: data.nickname,
      profile_img: data.profile_img,
      introduce: data.introduce
    }
    console.log(profileInfo.value)
  })
  .catch((err) => {
    console.log(err)
  })

  const fileInput = ref(null) 

  const upload = function () {
    console.log(fileInput.value)
    const file = fileInput.value.files[0]
    const formData = new FormData()
    formData.append('profile_img', file)
    formData.append('nicname', '되냐')
    axios({
      method: 'put',
      url: `http://127.0.0.1:8000/api/v1/profile/${username}/`,
      headers: {
        Authorization: `Token ${store.token}`,
        "Content-Type": 'multipart/form-data'
      },
      data: formData
    })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
  }
</script>

<style scoped>

</style>