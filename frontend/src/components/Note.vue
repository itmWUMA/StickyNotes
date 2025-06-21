<template>
  <div class="note">
    <p>这是一个示例便签纸。</p>
    <button class="delete-button"><i class="fas fa-trash"></i></button>
  </div>
</template>

<script setup>
// JS logic will be added later
</script>

<style scoped>
.note {
    background-color: #e8f1f5; /* Light yellow */
    border: 1px solid;
    color: #303841;
    padding: 15px;
    border-radius: 4px;
    position: relative;
    word-wrap: break-word; /* Break long words */
}

.note p {
    margin-top: 0;
    margin-bottom: 25px; /* Space for delete button */
}

.delete-button {
    position: absolute;
    bottom: 10px;
    right: 10px;
    background: none;
    border: none;
    padding: 0;
    font-size: 1.2rem; /* Increase size for icon */
    color: #d9534f; /* Red color for the icon */
    cursor: pointer;
}

.delete-button:hover {
    color: #c9302c; /* Darker red on hover */
}
</style>