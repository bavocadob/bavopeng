import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useUserStore = defineStore('user', () => {
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const userInfo = ref({})
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const login = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/dj-rest-auth/login/`,
      data: {
        username,
        password
      }
    })
      .then((res) => {
        // console.log(res)
        token.value = res.data.key
        return res.data.key
      })
      .then((token) => {
        getUserInfo(token)
      })
      .then(() => {
        router.replace({name: 'main'})
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getUserInfo = function (token) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/userinfo/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then((res) => {
        userInfo.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/dj-rest-auth/registration/`,
      data: {
        username,
        password1,
        password2
      }
    })
      .then((res) => {
        // console.log(payload)
        return payload
      })
      .then((payload) => {
        const data = {
          username: payload.username,
          password: payload.password1
        }
        login(data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logout = function () {
    axios({
      method: 'post',
      url: `${API_URL}/dj-rest-auth/logout/`
    })
      .then((res) => {
        console.log(res)
        token.value = null
        userInfo.value = {}
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  return { API_URL, signUp, login, logout, token, isLogin, userInfo, getUserInfo}
}, {persist: true})
