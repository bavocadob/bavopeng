<template>
    <div class="w-screen h-screen bg-[url('@/assets/images/loginbg.jpg')] bg-cover">
      <div class="w-screen h-screen bg-blue-950 bg-opacity-80 grid place-content-center">
        <div v-if="route.name === 'signin'">
          <SigninForm />
        </div>
        <div v-if="route.name === 'signup'">
          <SignupForm />
        </div>
      </div>
    </div>
</template>

<script setup>
import { useUserStore } from '../stores/user'
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import SigninForm from '@/components/SigninForm.vue'
import SignupForm from '@/components/SignupForm.vue'

const store = useUserStore()
const router = useRouter()
const route = useRoute()

const username = ref(null)
const password = ref(null)

const login = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.login(payload)
}

const goMain = function () {
  router.push({ name: 'main' })
}

</script>

<style scoped>

</style>