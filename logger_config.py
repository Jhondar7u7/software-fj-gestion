# logger_config.py
# Configura el archivo de logs donde se guardan eventos y errores.

import logging
import os

# Crea la carpeta "logs" si no existe
os.makedirs("logs", exist_ok=True)

# Crea el logger con un nombre y le dice que guarde desde nivel INFO
logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.INFO)

# Solo configuramos el archivo una vez (evita mensajes repetidos)
if not logger.handlers:
    # Archivo donde se escriben los mensajes
    archivo = logging.FileHandler("logs/eventos.log", encoding="utf-8")

    # Formato: fecha y hora - tipo de mensaje - texto
    formato = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    archivo.setFormatter(formato)

    # Conecta el archivo con el logger
    logger.addHandler(archivo)