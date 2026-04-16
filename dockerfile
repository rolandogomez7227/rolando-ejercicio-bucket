FROM python:3.9-slim
WORKDIR /app
COPY app.py datos.json.
# Ejecutar el script
CMD ["python", "app.py"]