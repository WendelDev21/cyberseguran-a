import os
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

UPLOAD_FOLDER = 'pasta_para_salvar'
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

    # Salva a imagem
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # URL da imagem que você pode enviar via WhatsApp
    image_url = f"http://192.168.3.19:5000/{UPLOAD_FOLDER}/{file.filename}"

    # Substitua pelo seu número
    whatsapp_number = "5579999801810"
    whatsapp_message = f"Nova foto recebida: {image_url}"

    # Redirecionar para o WhatsApp
    return redirect(f"https://wa.me/{whatsapp_number}?text={whatsapp_message}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
