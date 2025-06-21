<template>
  <div class="input-area">
    <h2>输入区</h2>
    <textarea id="note-input" placeholder="请输入便签内容..."></textarea>
    <button id="add-button">添加便签</button>
  </div>
</template>

<script setup>
// JS logic will be added later
</script>

<style scoped>
.input-area {
    flex: 1;
    background-color: #303841;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.input-area h2 {
    margin-top: 0;
    color: #eeeeee;
}

textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
    font-family: sans-serif;
}

button {
    display: block;
    background: #ff5722;
    color: #fff;
    border: none;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
}

button:hover {
    background: #005691;
}
</style>