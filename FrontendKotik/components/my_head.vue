<template>
    <div class="container">
      <div><NuxtLink to="/breed_list" exact-active-class="active" class="el">список пород</NuxtLink></div>
      <div><NuxtLink to="/catList" exact-active-class="active" class="el">список котов</NuxtLink></div>
      <div><NuxtLink to="/catList/create" target="_blank">добавить кота</NuxtLink></div>
      <div><NuxtLink to="/filter" target="_blank">Поиск котов по породе</NuxtLink></div>
    </div>
  </template>
  
  <style>
  .container{
    margin-bottom: 40px;
  }
  </style>
  