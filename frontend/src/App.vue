<template>
  <div class="container">
    <InputArea @add-note="addNote" />
    <DisplayArea :notes="notes" @delete-note="deleteNote" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import InputArea from './components/InputArea.vue';
import DisplayArea from './components/DisplayArea.vue';

const notes = ref([]);

const addNote = (noteContent) => {
  if (noteContent.trim()) {
    notes.value.push({
      id: Date.now(), // Simple unique ID
      content: noteContent
    });
  }
};

const deleteNote = (noteId) => {
  notes.value = notes.value.filter(note => note.id !== noteId);
};
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
    max-width: 1600px; /* Increased max-width */
    margin: 0 auto;
}
</style>
