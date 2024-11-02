from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'pasta_para_salvar'  # Certifique-se de que esse caminho exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')  # Certifique-se de que main.html exista

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No image file part', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return 'Upload successful', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
