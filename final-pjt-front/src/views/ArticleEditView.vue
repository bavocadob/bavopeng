<template>
  <div class="editor mx-auto my-10 p-5 bg-white shadow-md rounded-lg max-w-3xl">
    <input
      type="text"
      v-model="title"
      class="editor-title w-full p-3 mb-5 text-lg text-gray-900 placeholder-gray-500 border-b-2 border-gray-200 outline-none"
      placeholder="제목을 입력하세요."
    />
    <QuillEditor 
      v-model:content="content" contentType="html"
      :modules="modules"
      :toolbar="toolbar"
      class="h-96 border-gray-200 border rounded-lg"
    >
    </QuillEditor>

    <div class="relative mt-5 ">
      <input 
        class="w-full py-3 px-4 rounded-lg border-2 border-gray-200 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
        type="text"
        placeholder="영화를 검색하세요."
        @input="searchMovie"
        v-model="movieQuery"
      >
      
      <div v-if="searchedMovies.length > 0" class="absolute top-full w-full bg-white border border-gray-200 rounded-lg mt-1 z-10 overflow-y-auto max-h-48">
        <div 
          class="p-1.5 text-sm"
          v-for="(movie, index) in searchedMovies"
          :key="index"
          @click="selectMovie(movie)"
          >
          {{ movie.title }}
        </div>
      </div>
    </div>

    <!-- 태그된 영화 목록 -->
    <div v-if="selectedMovie != null" class="mb-5 mt-3">
      <div
        class="flex justify-between items-center p-3 mb-2 bg-gray-100 rounded-lg"
      >
        <div class="flex items-center">
          <img
            :src="`https://image.tmdb.org/t/p/original${selectedMovie.poster_path}`"
            alt="poster"
            class="w-12 mr-3"
          >
          <div>
            <div class="text-base">{{ selectedMovie.title }}</div>
            <div class="text-sm">{{ selectedMovie.release_date?.slice(0, 4) }}</div>
            <div class="flex">
              <StarRating
                v-model="selectedMovie.rating_avg"
                :disableClick="true"
                :starSize="14"
                :starColor="'#4263EB'"
                :numberOfStars="5"
              />
              <span class="text-sm ml-2">{{ Math.round(selectedMovie.rating_avg * 10) / 10 }}</span>
            </div>
          </div>
        </div>
        
        <!-- 삭제 버튼 -->
        <button @click="deleteMovie" class="text-gray-500 hover:text-red-500">
          <i class="fas fa-times"></i>
        </button>
      </div>
    </div> 

    <div class="mt-5 flex justify-end">
      <button class="bg-blue-900 hover:bg-blue-1000 hover:opacity-90 text-white py-2 px-5 rounded-lg text-sm transition duration-200 ease-in-out" @click="articleEdit">
        수정하기
      </button>
    </div>


  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { QuillEditor } from '@vueup/vue-quill'
import { useUserStore } from '@/stores/user'
import { useRoute, useRouter } from 'vue-router'
import { debounce } from 'lodash'
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import ImageUploader from 'quill-image-uploader'
import axios from 'axios'
import StarRating from '@/components/StarRating.vue'


const title = ref('')
const content = ref('')
const movieQuery = ref('')

const searchedMovies = ref([])
const selectedMovie = ref(null)
const store = useUserStore()
const router = useRouter()
const route = useRoute()
 

onMounted(() => {
  axios({
    method : 'GET',
    url : `${store.API_URL}/api/v1/article/${route.params.articleId}/`,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    console.log(res)
    title.value = res.data.title
    content.value = res.data.content
    selectedMovie.value = res.data.ref_movie
  })
  .catch((err) => {
    router.push({
      name : 'community'
    })
  })
})


const searchMovie = debounce(function(event) {
  if (movieQuery.value.trim()){
    axios({
      'method' : 'GET',
      'url' : `${store.API_URL}/api/v1/movie/search/${movieQuery.value}`,
    })
    .then((res) => {
      console.log(res)
      searchedMovies.value = res.data
    })
    .catch((err) => console.log(err))
  } else {
    searchedMovies.value = []
  }
}, 300)


const selectMovie = function(movie) {
  selectedMovie.value = movie
  movieQuery.value = ''
  searchedMovies.value = []
}

const deleteMovie = function() {
  selectedMovie.value = null
}


const modules = {
        name: 'imageUploader',
        module: ImageUploader,
        options: {
          upload: file => {
            return new Promise((resolve, reject) => {
              const formData = new FormData()
              formData.append("image", file)
              axios(
                {
                  method: "POST",
                  data: formData,
                  url: `${store.API_URL}/api/v1/article/image/`
                }
              )
                .then(response => response.data)
                .then(result => {
                  console.log(result);
                  resolve(result.url)
                })
                .catch(error => {
                  reject("Upload failed")
                  console.error("Error:", error)
                });
            });
            }
          }
  }


const toolbar = [
      ['bold', 'italic', 'underline', 'strike'],
      ['blockquote', 'code-block'],
      [{ 'list': 'ordered' }, { 'list': 'bullet' }],
      [{ 'color': [] }, { 'background': [] }],
      ['image']
    ]

const articleEdit = function() {
  const data = {
    title : title.value,
    content : content.value,
  }

  if (selectedMovie.value !== null) {
    data.ref_movie = selectedMovie.value.id;
  }
  
  axios({
    method : 'PUT',
    url : `${store.API_URL}/api/v1/article/${route.params.articleId}/`,
    data,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    router.push({
      name: 'articleDetail',
      params: {
        articleId: res.data.id,
      },
    })
  })
  .catch((err) => {
    console.log(err)
    router.push({
      name : 'community'
    })
  })

}


</script>

<style scoped>

</style>

