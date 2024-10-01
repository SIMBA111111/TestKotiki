<template>
    <div>
      <my_head></my_head>
      <h1>Добавить кота</h1>
      <form @submit.prevent="addCat">
        <div>
          <label for="breed">Порода:</label>
          <select v-model="cat.breed" id="breed" required>
            <option value="" disabled>Выберите породу</option>
            <option v-for="breed in breeds" :key="breed" :value="breed">{{ breed.name }}</option>
          </select>
        </div>
        <div>
          <label for="color">Цвет:</label>
          <input type="text" v-model="cat.color" id="color" required />
        </div>
        <div>
          <label for="age">Возраст:</label>
          <input type="number" v-model="cat.age" id="age" required />
        </div>
        <div>
          <label for="description">Описание:</label>
          <textarea v-model="cat.description" id="description" required></textarea>
        </div>
        <button type="submit">Добавить кота</button>
      </form>
      <p v-if="message">{{ message }}</p>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
import { ref } from 'vue';
  
  const cat = ref({
    id: 2,
    color: '',
    age: '',
    description: '',
    breed: ''
  });
  console.log(cat);
  
  const message = ref('');
  const breeds = ref([]);

  const getBreeds = async () => {
    try {
        const response = await axios.get("http://127.0.0.1:8000/api/v1/all-breeds")
        breeds.value = response.data
    } catch (Error) {
        console.error("Error:", Error)
    }

  }

  onMounted( async () => {
    await getBreeds()
  });
  
  const addCat = async () => {
    try {
        console.log(cat);
        const response = await axios.post('http://127.0.0.1:8000/api/v1/create-cat', cat.value);
        message.value = response.data.Success; 
        cat.value = { breed: '', color: '', age: '', description: '' };
    } catch (error) {
      console.error("Error:", error);
    }
  };
  </script>
  
  <style scoped>
  form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
  }
  label {
    margin-top: 10px;
  }
  </style>
  