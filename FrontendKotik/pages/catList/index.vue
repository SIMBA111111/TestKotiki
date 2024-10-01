<template>
    <div>
      <my_head></my_head>
      <hr>
      <div v-for="cat in cat_list" :key="cat.id">
        {{ cat.id }} - 
        {{ cat.color }}
        {{ cat.age }}
        {{ cat.description }}
        {{ cat.breed.name }}
        <div><NuxtLink :to="`/catList/${cat.id}`" target="_blank">подробнее</NuxtLink></div>
        <hr>
      </div>    
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  const cat_list = ref([]);
  
  const get_cats = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/v1/all-cats");
      cat_list.value = response.data; 
      console.log("cat_list.value - ", cat_list.value);
      
    } catch (error) {
      console.error('Error:', error);
    }
  };
  
  onMounted(async () => {
    await get_cats();
  });
  </script>
  
  <style>
  </style>
  