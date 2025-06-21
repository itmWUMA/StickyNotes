<template>
  <div class="container">
    <InputArea />
    <DisplayArea />
  </div>
</template>

<script setup>
import InputArea from './components/InputArea.vue';
import DisplayArea from './components/DisplayArea.vue';
</script>

<style>
body {
    font-family: sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 20px;
    background: linear-gradient(to right, 
        #2980b9,
        #6dd5fa,
        #ffffff);
    color: #eeeeee;
}

.container {
    display: flex;
    flex-direction: column;
    gap: 20px;
    max-width: 1200px;
    margin: 0 auto;
}
</style>
