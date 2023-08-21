from flask import Flask, request, jsonify
from docx import Document
import magic

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/upload', methods=['POST'])
def upload_file():
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
    app.run(debug=True)
