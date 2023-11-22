import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const articles = ref([])
  const reloadComment = ref(false)

  const getArticles = function (page) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/article/pages/${page}/`,
    })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const toggleReloadComment = function() {
    reloadComment.value = !reloadComment.value
  }

  return { reloadComment, API_URL, toggleReloadComment }
  
}, {persist: true})
