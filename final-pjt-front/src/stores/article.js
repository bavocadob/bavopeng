import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const API_URL = 'http://127.0.0.1:8000/api/v1'
  const articles = ref([])

  const getArticles = function (page) {
    axios({
      method: 'get',
      url: `${API_URL}/article/pages/${page}/`,
    })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
}, {persist: true})
