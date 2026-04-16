# Usamos el repositorio público de AWS para evitar el bloqueo de Docker Hub
FROM public.ecr.aws/docker/library/python:3.9-slim

WORKDIR /app

# Copiamos los archivos (Asegúrate que existan en GitHub)
COPY app.py .
COPY datos.json .

CMD ["python", "app.py"]