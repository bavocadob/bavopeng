<template>
  <div class="mb-8">
    <img
      v-if="actor.profile_path"
      class="profile-image"
      :src="`https://image.tmdb.org/t/p/original${actor.profile_path}`"
    />
    <img
      v-else
      src="@/assets/images/anonymous.png"
    >

    <div>
      <p v-if="actor.korean_name" class="profile-name">{{ actor.korean_name }}</p>
      <p v-else class="profile-name">{{ actor.name }}</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  actor: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.profile-image {
  border-radius: 8px;
  margin-bottom: 0.3rem;
  box-shadow: 1px 1px 2px 1px rgba(0, 0, 0, 0.1);
}

.profile-name {
  flex-grow: 1;
  min-width: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}


</style>