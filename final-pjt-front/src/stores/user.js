import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000/dj-rest-auth'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value = null) {
      return false
    } else {
      return true
    }
  })

  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/registration/`,
      data: {
        username,
        password1,
        password2
      }
    })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
}, {persist: true})
