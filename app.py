import os
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Define o caminho da pasta para armazenar as imagens
UPLOAD_FOLDER = '/home/wendel-lucas/Imagens/teste'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No image file part', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400

    # Salva a imagem no caminho especificado
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Retornar uma mensagem de sucesso
    return f'Imagem salva com sucesso em: {file_path}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
