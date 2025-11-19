from flask import Flask, request, send_file
from flask_cors import CORS
import cv2
import numpy as np
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # <- Esto sí habilita CORS correctamente


# Cargar clasificador Haarcascade
rostro = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

@app.route("/rostros", methods=["POST"])
def detectar_rostros():
    if 'imagen' not in request.files:
        return {"error": "Debes enviar una imagen"}, 400
    
    file = request.files['imagen']
    
    # Leer imagen en OpenCV
    npimg = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detectar rostros
    cara = rostro.detectMultiScale(img_gris, 1.3, 8)
    
    # Dibujar rectángulos
    for (x, y, ancho, alto) in cara:
        cv2.rectangle(img, (x, y), (x+ancho, y+alto), (255,0,150), 5)
    
    # Guardar resultado temporal
    output_path = os.path.join(os.path.dirname(__file__), "resultado.jpg")
    cv2.imwrite(output_path, img)
    
    # Retornar imagen
    return send_file(output_path, mimetype="image/jpeg")

if __name__ == "__main__":
    print("Servidor Flask corriendo en http://127.0.0.1:5000")
    app.run(debug=True)
