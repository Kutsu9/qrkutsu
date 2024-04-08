import qrcode as qr
from flask import Flask, request

# Instalar 
# pip install qrcode[pil]
# pip install Flask

# http://127.0.0.1:5000/qrpyxl?key1=397485|W1|0

app = Flask(__name__)

from flask import send_file
import io

@app.route('/qrpyxl', methods=['POST'])
def handle_post():
    # Accede a los datos enviados en la URL

    # Accede a los datos enviados en la URL
    data = request.args.get('key1', '')
    print(data)
    # Generar el QR basado en los datos recibidos
    qr_img = qr.make(data)
    img_io = io.BytesIO()  # Creamos un buffer para la imagen
    qr_img.save(img_io, 'PNG')  # Guardamos la imagen en formato PNG en el buffer
    img_io.seek(0)  # Movemos al inicio del buffer

    return send_file(img_io, mimetype='image/png')  # Enviamos la imagen como respuesta


if __name__ == '__main__':
    app.run(debug=True)
