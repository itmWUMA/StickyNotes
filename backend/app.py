import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app) # Enable CORS for all origins

# MongoDB connection
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client.notes_db # Database name
notes_collection = db.notes # Collection name

@app.route('/notes', methods=['GET'])
def get_notes():
    notes = []
    for note in notes_collection.find():
        note['_id'] = str(note['_id']) # Convert ObjectId to string
        notes.append(note)
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
def add_note():
    new_note = request.json
    if not new_note or 'content' not in new_note:
        return jsonify({'message': 'Invalid request body'}), 400

    inserted_note = notes_collection.insert_one({'content': new_note['content']})
    created_note = notes_collection.find_one({'_id': inserted_note.inserted_id})
    created_note['_id'] = str(created_note['_id']) # Convert ObjectId to string
    return jsonify(created_note), 201

@app.route('/notes/<string:note_id>', methods=['DELETE'])
def delete_note(note_id):
    try:
        print(note_id)
        result = notes_collection.delete_one({'_id': ObjectId(note_id)})
        if result.deleted_count == 1:
            return jsonify({'message': 'Note deleted'}), 200
        return jsonify({'message': 'Note not found'}), 404
    except Exception as e:
        return jsonify({'message': 'Invalid note ID', 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')