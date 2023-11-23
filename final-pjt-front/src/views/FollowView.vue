<template>
  <div class="text-center text-white text-4xl font-semibold my-8">
    <h1
      class="my-8 cursor-pointer"
    >{{ route.name }} list</h1>
    <div class="w-1/2 h-[640px] text-slate-900 overflow-y-auto mx-auto hover:cursor-pointer">
      <UserFollowProfile
      v-for="user in followList"
      :key="user.id"
      :user="user"
      @click="goProfile(user.username)"
      />
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'
import { ref } from 'vue'
import { routerKey, useRoute, useRouter } from 'vue-router'
import UserFollowProfile from '@/components/UserFollowProfile.vue'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const store = useUserStore()

const followList = ref([])

axios({
  method: 'get',
  url: `${store.API_URL}/api/v1/${route.name}/${route.params.id}/` 
})
  .then((res) => {
    console.log(res)
    followList.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })

const goProfile = function (username) {
  router.push({name: 'profile', params: {username}})
}

</script>

<style scoped>

</style>