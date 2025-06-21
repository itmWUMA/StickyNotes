<template>
  <div class="display-area">
    <h2>展示区</h2>
    <div class="notes-container">
      <Note v-for="note in notes" :key="note.id" :note="note" @delete-note="handleDeleteNote" />
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';
import Note from './Note.vue';

const props = defineProps({
  notes: {
    type: Array,
    default: () => []
  }
});

const emit = defineEmits(['delete-note']);

const handleDeleteNote = (noteId) => {
  emit('delete-note', noteId);
};
</script>

<style scoped>
.display-area {
    flex: 1;
    min-width: 400px; /* Added min-width */
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