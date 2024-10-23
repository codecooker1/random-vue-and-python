<template>
  <div>
    <router-link to="{name:'PostDetails', params:{id:post.id}}">
      <h3>{{ post.title }}</h3>
      <p>{{ snippet }}</p>
      <span v-for="tag in post" :key="tag"> #{{ tag }} </span>
    </router-link>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps(['post'])

const snippet = computed(() => {
  return props.post.body.substring(0, 100) + '.....'
})
</script>

<style scoped></style>
