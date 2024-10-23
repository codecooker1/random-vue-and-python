<template>
  <div class="post-list">
    <div v-for="post in posts" :key="post.id">
      <SinglePost :post="post" />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import SinglePost from './SinglePost.vue'

const props = defineProps(['posts'])

console.log(props)

onMounted(() => {
  console.log('mounted')
})
</script>

<style scoped></style>
