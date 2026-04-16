FROM python:3.9-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos cada archivo de forma individual asegurando el destino
COPY app.py /app/app.py
COPY datos.json /app/datos.json

# Ejecutamos con la ruta absoluta
ENTRYPOINT ["python", "/app/app.py"] 