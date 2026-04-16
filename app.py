import json
import os
from datetime import datetime

def procesar_datos(version_cambio):
    archivo_entrada = 'datos.json'
    archivo_salida = 'resultados.json'
    log_file = 'backup.log'
    
    # 1. Leer información
    with open(archivo_entrada, 'r') as f:
        datos = json.load(f)
    
    # 2. Procesar (Filtro: solo usuarios con status 'activo')
    filtrados = [d for d in datos if d.get('status') == 'activo']
    conteo = len(filtrados)
    
    # 3. Generar archivo de resultados
    with open(archivo_salida, 'w') as f:
        json.dump(filtrados, f, indent=4)
    
    # 4. Registrar en backup.log
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{fecha_hora}] Archivo: {archivo_entrada} | Procesados: {conteo} | Versión: {version_cambio}\n"
    
    with open(log_file, 'a') as f:
        f.write(log_entry)
    
    print(f"Se filtró {conteo} datos")

if __name__ == "__main__":
    # La versión se puede pasar como variable de entorno o input manual
    v = os.getenv('VERSION_ID', 'v1.0')
    procesar_datos(v)