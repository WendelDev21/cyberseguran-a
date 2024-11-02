import os
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# Configurações do Telegram
TELEGRAM_BOT_TOKEN = '7203276521:AAFV3BfQkszoQGtY1as_IKy1tVOxYFNikck'
CHAT_ID = '6540052628'

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

    # Salvar imagem em uma pasta temporária
    file_path = f'/tmp/{file.filename}'  # ou qualquer caminho temporário
    file.save(file_path)

    # Enviar imagem para o Telegram
    with open(file_path, 'rb') as photo:
        requests.post(f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto',
                      data={'chat_id': CHAT_ID},
                      files={'photo': photo})

    return 'Imagem enviada para o Telegram com sucesso!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
