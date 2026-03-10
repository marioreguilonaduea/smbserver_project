"""
smb_client.py

Este script actúa como cliente SMB.
Se conecta a un servidor SMB levantado previamente y accede
al recurso compartido C$.

El objetivo es verificar que el cliente puede conectarse, subir un archivo
y ver el contenido del share.
"""

import logging
from src.shared.config import SHARE_NAME, DATA_DIR
from src.client.connection import crear_conexion, cerrar_conexion
from src.client.file_ops import listar_archivos, subir_archivo


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def main():

    conexion = crear_conexion()

    listar_archivos(conexion, SHARE_NAME)

    archivo_local = DATA_DIR / "upload_test.txt"
    archivo_remoto = "malware_copy.txt"

    subir_archivo(conexion, SHARE_NAME, archivo_local, archivo_remoto)

    listar_archivos(conexion, SHARE_NAME)

    cerrar_conexion(conexion)


if __name__ == "__main__":
    main()