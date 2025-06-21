<template>
  <div class="display-area">
    <h2>展示区</h2>
    <div class="notes-container">
      <!-- 示例便签纸 -->
      <Note />
      <Note />
    </div>
  </div>
</template>

<script setup>
import Note from './Note.vue';
// JS logic will be added later
</script>

<style scoped>
.display-area {
    flex: 1;
    background-color: #303841;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.display-area h2 {
    margin-top: 0;
    color: #eeeeee;
}

.notes-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
}
</style>