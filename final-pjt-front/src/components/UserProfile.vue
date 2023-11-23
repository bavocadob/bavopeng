<template>
    <div class="bg-white flex flex-col p-4">
      <div class="basis-4/5 flex">
        <div class="basis-4/12 m-4 flex flex-col justify-center items-center gap-4">
          <div v-if="profileUrl" class="w-32 h-32 border rounded-full bg-slate-50">
            <img 
              v-if="route.name!=='profile'" :src="previewImg" alt="previewImg"  
              class="w-full h-full rounded-full outline outline-offset-4 outline-2 outline-indigo-600"
            >
            <img 
              v-else :src="profileUrl" alt="profileImg" 
              class="w-full h-full rounded-full outline outline-offset-4 outline-2 outline-indigo-600"
            >
          </div>
          <div v-else class="w-32 h-32 border rounded-full bg-slate-50">
            <img 
              src="@/assets/images/anonymous_square.png" alt="anonymous"
              class="w-full h-full rounded-full outline outline-offset-4 outline-2 outline-indigo-600"
            >
          </div>
          <input 
            v-if="route.name!=='profile'" @change="changeImage"
            type="file" accept=".png, .jpg" ref="fileInput" 
            class="w-full text-sm ps-5"
          /> 
        </div>
        <div class="basis-7/12 mt-6 flex flex-col justify-between">
          <div class="flex max-md:flex-col items-start">
            <div class="basis-3/4">
              <h2 v-if="route.name === 'profile'" class="text-4xl font-bold">{{ nickname }}</h2>
              <div v-else>
                <input v-model="nickname" @input="ExistsNickname"
                  class="w-64 text-xl border-2 text-black border-slate-400 rounded-md px-4 py-2 focus:outline-indigo-500"
                  :class="{'border-pink-500 text-pink-600 focus:outline-pink-500 focus:ring-pink-500':!isValidNickname}"
                >
                <p>{{ checkNicknameMessage }}</p>
              </div>
            </div>
            <div class="basis-1/4">
              <button @click="follow"
                v-if="store.userInfo.username !== route.params.username"
                class="bg-slate-200 text-sm px-2 py-1.5 rounded-md"
              >&nbsp&nbsp팔로우&nbsp&nbsp</button>
              <div v-else>
                <button 
                  v-if="route.name === 'profile'" @click="goModify"
                  class="bg-slate-200 text-sm px-2 py-1.5 rounded-md"
                >프로필 수정</button>
                <button v-else @click="goProfile"
                  class="bg-slate-200 text-sm px-2 py-1.5 rounded-md"
                >프로필 저장</button>
              </div>
            </div>
          </div>
          <div>
            <span 
              v-for="genre in profileInfo.genresLike"
              class="me-4 p-2 rounded-md bg-blue-200 font-semibold shadow-md"
            >{{ genre[0] }}</span>
          </div>
          <div class="text-xl flex gap-4">
            <p @click="followerList" class="shadow-md py-1 px-1.5 rounded-md hover:cursor-pointer">
              팔로워&nbsp
              <span class="">{{ followersCnt }}</span>
            </p>
            <p @click="followingList" class="shadow-md py-1 px-1.5 rounded-md hover:cursor-pointer">
              팔로우&nbsp
              <span class="">{{ followingsCnt }}</span>
            </p>
          </div>
        </div>
      </div>
      <div class="basis-1/2 m-2">
        <div class="flex justify-between">
          <p class="text-lg">About Me</p>
          <div v-if="route.name === 'profileModify'" class="mt-auto">
            <span>{{ introduceLength }}</span>
            <span>/250자</span>
          </div>
        </div>
        <div v-if="route.name === 'profile'" class="p-4 border shadow-sm ">
          <p>{{ introduce }}</p>
          <p v-if="!introduce" class="text-gray-400">
            아직 소개가 없습니다.
          </p>
        </div>
        <div v-else>
          <textarea rows="5" maxlength="250" v-model="introduce"
            class="p-4 block w-full border border-gray-300 shadow-sm resize-none focus:outline-none
            focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" 
          ></textarea>
      </div>
      </div>
    </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute, useRouter, onBeforeRouteLeave } from 'vue-router'
import { useUserStore } from '../stores/user'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const store = useUserStore()
const props = defineProps({
  profileInfo: Object,
})

const username = route.params.username
const nickname = ref(props.profileInfo.nickname)
const profileUrl = ref(store.API_URL+props.profileInfo.profile_img)
const introduce = ref(props.profileInfo.introduce)
const followingsCnt = ref(props.profileInfo.followingsCnt)
const followersCnt = ref(props.profileInfo.followersCnt)
const checkNicknameMessage = ref('')
const isValidNickname = ref(true)
const introduceLength = ref(introduce.value?.length)

watch(() => props.profileInfo, (newProfile) => {
  if (newProfile.profile_img !== null) {
    profileUrl.value = store.API_URL+newProfile.profile_img
  } else {
    profileUrl.value = null
  }
  nickname.value = newProfile.nickname
  introduce.value = newProfile.introduce
  followingsCnt.value = newProfile.followingsCnt
  followersCnt.value = newProfile.followersCnt
})

watch(introduce, (newValue) => {
  introduceLength.value = newValue.length
})

// 프로필 사진 프리뷰
const previewImg = ref(profileUrl)
const changeImage = (event) => { 
  const files = event.target?.files
  // console.log(files)
  if (files.length > 0){
      const file = files[0]
      const reader = new FileReader() 
      reader.onload = (read) => {
      previewImg.value = read.target.result }
      reader.readAsDataURL(file)
  }
}

// 이미지 포함한 요청
const fileInput = ref(null) 
const upload = function () {
  const file = fileInput.value.files[0]
  const formData = new FormData()
  if (file) {
    formData.append('profile_img', file)
  }
  formData.append('nickname', nickname.value)
  formData.append('introduce', introduce.value)
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
      store.getUserInfo(store.token)
    })
    .catch((err) => {
      console.log(err)
    })
}

const ExistsNickname = function () {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/nickname/',
    params: {
      nickname: nickname.value
    }
  })
    .then((res) => {
    if (!nickname.value) {
      checkNicknameMessage.value = '닉네임을 입력해주세요.'
      isValidNickname.value = false
    } else if (res.data.result && (nickname.value !== store.userInfo.profile.nickname)) {
        checkNicknameMessage.value = '이미 존재하는 닉네임입니다.'
        isValidNickname.value = false
    } else {
        checkNicknameMessage.value = ''
        isValidNickname.value = true
    }
    })
    .catch((err) => {
      console.log(err)
    })
}

const goModify = function () {
  router.push({name: 'profileModify', params: {username: username}})
}

const goProfile = function () {
  if (isValidNickname.value) {
    router.push({name: 'profile', params: {username: username}})
  }
}

onBeforeRouteLeave((to, from) =>  {
  console.log(from)
  if (from.name === 'profileModify') {
    const answer = window.confirm('저장하시겠습니까?')
    if (answer === false) {
      return false
    } else {
      upload()
    }
  }
})
// console.log(profileUrl)

// 팔로우 & 언팔로우
const follow = function () {
  console.log(props.profileInfo.followers)
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/following/${props.profileInfo.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
      if (props.profileInfo.followers.includes(store.userInfo.id)) {
        props.profileInfo.followers.pop(store.userInfo.id)
        followersCnt.value -= 1
      } else {
        props.profileInfo.followers.push(store.userInfo.id)
        followersCnt.value += 1
      }
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>