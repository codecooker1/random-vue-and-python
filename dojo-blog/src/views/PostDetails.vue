<template>
  <div class="error" v-if="{ error }">{{ error }}</div>
  <div class="post" v-if="post">
    <h3>{{ post.title }}</h3>
    <p class="pre">{{ post.body }}</p>
  </div>
</template>

<script setup>
import getPost from '@/composables/getPost'

const props = defineProps(['id'])

const { post, error, load } = getPost(props.id)
load()
</script>

<style scoped>
.post {
  max-width: 1200px;
  margin: 0 auto;
}
.post p {
  margin-top: 40px;
  color: #444;
  line-height: 1.4em;
}
.pre {
  white-space: pre-wrap;
}
</style>
