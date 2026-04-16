FROM python:3.9-slim
WORKDIR /app

# Copiamos los archivos uno por uno para asegurar que entren
COPY app.py /app/app.py
COPY datos.json /app/datos.json

# Ejecutar el script apuntando a la ruta completa
CMD ["python", "/app/app.py"]