<template>
    <div>
      <my_head></my_head>
      
      <div>
        <label for="breed-select">Выберите породу:</label>
        <select id="breed-select" v-model="selectedBreed" @change="fetchCats">
          <option disabled value="">выберите породу</option>
          <option v-for="breed in breeds" :key="breed.id" :value="breed.name">
            {{ breed.name }}
          </option>
        </select>
      </div>
  
      <div v-if="cats.length">
        <h2>Коты породы: {{ selectedBreed }}</h2>
        <ul>
          <li v-for="cat in cats" :key="cat.id">{{ cat.color }} - {{ cat.age }} - {{ cat.description }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  const breeds = ref([]);
  const cats = ref([]);
  const selectedBreed = ref("");
  
  const getBreeds = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/v1/all-breeds");
      breeds.value = response.data;
    } catch (error) {
      console.error("Error:", error);
    }
  };
  
  const fetchCats = async () => {
    if (!selectedBreed.value) return;
  
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/v1/filter-cats/?filter_data=${selectedBreed.value}`);
      cats.value = response.data;
    } catch (error) {
      console.error("Error fetching cats:", error);
    }
  };
  
  onMounted(async () => {
    await getBreeds();
  });
  </script>
  
  <style>
  </style>
  