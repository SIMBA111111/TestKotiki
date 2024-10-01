<template>
    <div>
      <my_head></my_head>
      <hr>
      <div v-for="breed in breed_list" :key="breed.id">
        {{ breed.name }}
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  const breed_list = ref([]);
  
  const get_breeds = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/v1/all-breeds");
      breed_list.value = response.data; 
    } catch (error) {
      console.error('Error:', error);
    }
  };
  
  onMounted(async () => {
    await get_breeds();
  });
  </script>
  
  <style>
  </style>
  