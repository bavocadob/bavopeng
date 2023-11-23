<template>
  <div class="fixed z-30 inset-28" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="flex items-center justify-center min-h-screen px-4 pt-6 pb-20 text-center sm:block sm:p-0">
      <div class="fixed inset-0 bg-gray-900 bg-opacity-75 transition-opacity"></div>

      <div class="fixed z-10 top-60 left-0 right-0 flex items-center justify-center" v-if="showAlert">
        <div class="bg-blue-900 text-white text-sm py-3 px-16 rounded">
          {{ alertMessage }}
        </div>
      </div>

      <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:align-middle sm:max-w-lg sm:w-full">
        <div class="bg-blue-900 px-4 py-2 flex justify-between items-center">
          <h3 class="text-lg leading-6 font-medium text-white" id="modal-title">
            리뷰 수정하기
          </h3>
          <button @click="closeModal" class="text-white text-lg">
            <i class="fas fa-times"></i>
          </button>
        </div>
        <div class="py-4 px-6">
          <div class="flex items-center mb-4">
            <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="Movie Poster" class="w-16 h-24 mr-4">
            
            <div>
              <p class="text-lg font-bold">{{ movie.title }}</p>
              <p class="text-gray-500">{{ movie.release_date }}</p>
            </div>
          </div>
          <div class="mb-4">
            <p class="text-lg font-bold mb-2">별점 평가</p>
            <div class="flex justify-center	">
              <StarRating 
                v-model="rating"
                :starSize="32"
                :starColor="'#4263EB'"
                :numberOfStars="5"
              />
            </div>
          </div>
          <div class="mb-4">
            <p class="text-lg font-bold mb-2">간단히 기록하기</p>
            <textarea
              v-model="content"
              class="w-full h-32 p-2 border border-gray-300 rounded focus:outline-none focus:ring-blue-500 focus:border-blue-500 resize-none"
              :maxlength="500"
            ></textarea>
            <p class="text-right text-gray-500 mt-1">{{ content.length }} / 500</p>
          </div>
          <div class="flex justify-end">
            <button @click="editReview" type="button" class="px-4 py-2 bg-blue-900 text-white rounded">
              수정
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import StarRating from '@/components/StarRating.vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useRoute } from 'vue-router'

const emit = defineEmits(['closeModal'])
const store = useUserStore()
const route = useRoute()


const props = defineProps({
  review : {
    type : Object,
  }
})


const rating = ref(0)
const content = ref('')
const showAlert = ref(false)
const alertMessage = ref('')
const movie = ref({})


onMounted(() => {
  rating.value = props.review.rating,
  content.value = props.review.content
  axios({
    method : 'GET',
    url : `http://127.0.0.1:8000/api/v1/movie/${route.params.movieId}/`
  })
  .then((res) => {
    movie.value = res.data 
  })
  .catch((err) => console.log(err))
})
 
const editReview = function() {
  if (rating.value === 0) {
    showAlert.value = true
    alertMessage.value = '아직 별점을 입력하지 않으셨어요!'
    setTimeout(() => { showAlert.value = false }, 2000)
    return
  }
  if (content.value === '') {
    showAlert.value = true
    alertMessage.value = '내용을 입력하지 않으셨어요!'
    setTimeout(() => { showAlert.value = false }, 2000)
    return
  }

  const data = {
    rating : rating.value,
    content : content.value,
  }

  axios({
    method : 'PUT',
    url : `${store.API_URL}/api/v1/review/${props.review.id}/`,
    data,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    location.reload() 
  })
  .catch((err) => {
    console.log(err)
  })

}

const closeModal = function() {
  emit('closeModal')
}

</script>
<style scoped>

</style>