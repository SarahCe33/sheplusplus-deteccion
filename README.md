🧠 Detector de Rostros con Python, Flask y OpenCV

Este proyecto permite detectar rostros en imágenes usando un backend en Python (Flask + OpenCV) y un frontend simple en HTML + JavaScript.
El usuario sube una imagen, el backend procesa la detección y devuelve una nueva imagen con los rostros marcados.
_______________________________________________________________________________________________________________________________________________
🚀 Características

Detecta rostros usando Haar Cascades de OpenCV.

API backend en Flask lista para usar.

Compatible con cualquier frontend (HTML, React, Vue, etc.).

Incluye soporte CORS para evitar errores al conectar frontend ↔ backend.

Respuesta en formato imagen JPEG generada en tiempo real.
_______________________________________________________________________________________________________________________________________________
📁 Estructura del proyecto
tallerrostros/
│
├── backend/
│   ├── app.py
│   ├── resultado.jpg (se genera automáticamente)
│
└── frontend/
    ├── index.html
_______________________________________________________________________________________________________________________________________________
🛠️ Requisitos

Instala los paquetes necesarios:

py -m pip install flask
py -m pip install flask-cors
py -m pip install opencv-python
py -m pip install numpy

Opcional pero recomendado:

py -m pip install --upgrade pip
_______________________________________________________________________________________________________________________________________________
▶️ Cómo ejecutar el backend (Flask)

Abre la terminal (CMD).

Muévete a la carpeta del backend:

cd C:\Users\TU_USUARIO\pruebas\tallerrostros\backend


Ejecuta el servidor:

py app.py


Deberías ver:

Servidor Flask corriendo en http://127.0.0.1:5000
 * Debug mode: on


El backend ya está funcionando.
_______________________________________________________________________________________________________________________________________________
🖥️ Cómo usar el frontend

Abre el archivo:

tallerrostros/frontend/index.html


Selecciona una imagen.

Haz clic en Detectar rostros.

El frontend enviará la imagen al backend vía fetch().

Se mostrará la imagen procesada con los rostros detectados.

📡 Endpoint disponible
POST /rostros

Parámetros:

imagen: archivo enviado en multipart/form-data.

Respuesta:

JPEG con los rostros detectados.
