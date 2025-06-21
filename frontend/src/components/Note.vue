<template>
  <div class="note">
    <p>{{ note.content }}</p>
    <button class="delete-button" @click="deleteNote"><i class="fas fa-trash"></i></button>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  note: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['delete-note']);

const deleteNote = () => {
  emit('delete-note', props.note.id);
};
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