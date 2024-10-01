<template>
  <div>
    <my_head></my_head>
    <h3>Обновить данные кота</h3>
    <form @submit.prevent="updateCat">
      <div>
        <label for="name">Возраст:</label>
        <input type="text" v-model="cat.age" id="name"/>
      </div>
      <div>
        <label for="color">Цвет:</label>
        <input type="text" v-model="cat.color" id="color"/>
      </div>
      <div>
        <label for="description">Описание:</label>
        <textarea v-model="cat.description" id="description"></textarea>
      </div>
      <button type="submit">Обновить</button>
    </form>
    
    <button @click="deleteCat" class="delete-button">Удалить кота</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const router = useRouter();
const catId = route.params.id;
console.log("catId - ", catId);

const cat = ref({
  age: '',
  color: '',
  description: '',
  breed: {
    id: '',
    name: '',
  }
});

const fetchCat = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/v1/get-cat/${catId}`);
    cat.value = response.data;
  } catch (error) {
    console.error("Ошибка при загрузке данных кота:", error);
  }
};

const updateCat = async () => {
  try {
    await axios.patch(`http://127.0.0.1:8000/api/v1/update-cat/${catId}`, cat.value);
  } catch (error) {
    console.error("Ошибка при обновлении данных кота:", error);
  }
};

const deleteCat = async () => {
  if (confirm('Вы уверены, что хотите удалить кота?')) {
    try {
      await axios.delete(`http://127.0.0.1:8000/api/v1/delete-cat/${catId}`);
      alert('Кот удалён!');
      router.push('/catList');
    } catch (error) {
      console.error("Ошибка при удалении кота:", error);
    }
  }
};

onMounted(fetchCat);
</script>

<style>
.delete-button {
  background-color: red;
  color: white;
  border: none;
  padding: 10px 15px;
  cursor: pointer;
  margin-top: 10px;
}
</style>
