<template>
  <div class="container">
    <InputArea @add-note="addNote" />
    <DisplayArea :notes="notes" @delete-note="deleteNote" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import InputArea from './components/InputArea.vue';
import DisplayArea from './components/DisplayArea.vue';

const notes = ref([]);
const API_URL = 'http://127.0.0.1:5000/notes';

const fetchNotes = async () => {
  try {
    const response = await axios.get(API_URL);
    notes.value = response.data;
  } catch (error) {
    console.error('Error fetching notes:', error);
  }
};

const addNote = async (noteContent) => {
  if (noteContent.trim()) {
    try {
      const response = await axios.post(API_URL, { content: noteContent });
      notes.value.push(response.data);
    } catch (error) {
      console.error('Error adding note:', error);
    }
  }
};

const deleteNote = async (noteId) => {
  try {
    await axios.delete(`${API_URL}/${noteId}`);
    notes.value = notes.value.filter(note => note._id !== noteId);
  } catch (error) {
    console.error('Error deleting note:', error);
  }
};

onMounted(fetchNotes);
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
