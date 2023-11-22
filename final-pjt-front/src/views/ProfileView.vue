<template>
    <div class="w-11/12 mx-auto">
      <h1 class="text-4xl font-semibold text-white">프로필</h1>
      <div class="my-8 h-full bg-gray-200 flex justify-center items-center rounded-lg">
        <div class="w-[800px] my-20 bg-white shadow-md">
          <UserProfile :profileInfo="profileInfo" />
        </div>
      </div>
      <div class="my-14 h-full bg-gray-200 flex flex-col items-center rounded-lg">
        <div class="my-8">
          <h2 class="text-2xl my-4">좋아하는 영화</h2>
          <div class="w-[1000px] my-18 bg-gray-100 p-8 rounded-lg shadow-md">
            <MovieSwiper :movies="likeMovies" />
          </div>
        </div>
        <div class="my-8">
          <h2 class="text-2xl m-4">보고싶은 영화</h2>
          <div class="w-[1000px] my-18 bg-gray-100 p-8 rounded-lg shadow-md">
            <MovieSwiper :movies="wishMovies" />
          </div>
        </div>
      </div>
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
import MovieSwiper from '../components/MovieSwiper.vue'

const route = useRoute()
const store = useUserStore()

const username = route.params.username
const profileInfo = ref({})
const preferenceInfos = ref({})
const likeMovies = ref([])
const wishMovies = ref([])
const records = ref({})

axios({
  method: 'get',
  url: `http://127.0.0.1:8000/api/v1/profile/${username}/`,
})
  .then((res) => {
    // console.log(res.data)
    const data = res.data
    profileInfo.value = {
      username,
      id: data.user.id,
      nickname: data.nickname,
      profile_img: data.profile_img,
      introduce: data.introduce,
      followings: data.user.followings_cnt,
      followers: data.user.followers_cnt,
    }
    likeMovies.value = data.user.liked_movies
    wishMovies.value = data.user.wished_movies
  })
  .catch((err) => {
    console.log(err)
  })

  
</script>

<style scoped>

</style>