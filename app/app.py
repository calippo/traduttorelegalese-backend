from flask import Flask, request, jsonify
from docx import Document
import magic

from dotenv import load_dotenv, find_dotenv
import os
_ = load_dotenv(find_dotenv()) # read local .env file
TOKEN = os.environ['TOKEN']

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/upload', methods=['POST'])
def upload_file():
        # Extract token from the Authorization header
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify(error="Missing Authorization header"), 401

    # Extract the token from the Bearer format
    token = auth_header.split(" ")[1] if " " in auth_header else auth_header

    # Check the token
    if token != TOKEN:
        return jsonify(error="Invalid token"), 403

    # Check if a file was sent
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']

    # If no filename provided, return error
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # If file exists, process it
    if file:
        # Read the Word Document
        doc = Document(file)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return magic.simplify('\n'.join(fullText))

    return jsonify({'error': 'File processing failed'}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
