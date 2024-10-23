<template>
  <div class="home">
    <h1>Home</h1>
    <PostList :posts="posts" />
    <div v-if="error" class="text-center">
      <div class="spinner-border" style="width: 5rem; height: 5rem" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import PostList from '@/components/PostList.vue'
import getPosts from '@/composables/getPosts'

const { posts, error, load } = getPosts()

load()
</script>

<style></style>
