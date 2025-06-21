import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all origins

DATA_FILE = 'notes.json'

def read_notes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def write_notes(notes):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(notes, f, indent=4, ensure_ascii=False)

@app.route('/notes', methods=['GET'])
def get_notes():
    notes = read_notes()
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
def add_note():
    new_note = request.json
    notes = read_notes()
    new_note['id'] = os.urandom(16).hex() # Generate a simple ID
    notes.append(new_note)
    write_notes(notes)
    return jsonify(new_note), 201

@app.route('/notes/<string:note_id>', methods=['DELETE'])
def delete_note(note_id):
    notes = read_notes()
    initial_len = len(notes)
    notes = [note for note in notes if note['id'] != note_id]
    if len(notes) < initial_len:
        write_notes(notes)
        return jsonify({'message': 'Note deleted'}), 200
    return jsonify({'message': 'Note not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)