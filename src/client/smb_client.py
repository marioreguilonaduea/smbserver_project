"""
smb_client.py

Este script actúa como cliente SMB.
Se conecta a un servidor SMB levantado previamente y accede
al recurso compartido C$.

El objetivo es verificar que el cliente puede conectarse
y ver el contenido del share.
"""

import logging
from impacket.smbconnection import SMBConnection
from src.shared.config import SERVER_IP, SERVER_PORT, SHARE_NAME


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def conectar_a_smb():
    """
    Función que establece conexión con el servidor SMB
    y lista el contenido del share.
    """

    # ------------------------------------------------------------------
    # 1. Configuración de conexión
    # ------------------------------------------------------------------

    servidor = SERVER_IP   # IP del servidor SMB
    puerto = SERVER_PORT   # Puerto SMB estándar
    share = SHARE_NAME     # Recurso compartido

    logging.info(f"Intentando conectar al servidor SMB {servidor}:{puerto}")

    # ------------------------------------------------------------------
    # 2. Crear conexión SMB
    # ------------------------------------------------------------------

    conexion = SMBConnection(servidor, servidor, sess_port=puerto)

    # ------------------------------------------------------------------
    # 3. Autenticación
    # ------------------------------------------------------------------
    # En este caso login anónimo porque el servidor lo permite

    conexion.login("", "")
    logging.info("Conexión SMB establecida correctamente")

    # ------------------------------------------------------------------
    # 4. Listar contenido del share
    # ------------------------------------------------------------------

    logging.info(f"Listando contenido del recurso compartido {share}")
    archivos = conexion.listPath(share, "*")

    for archivo in archivos:
        nombre = archivo.get_longname()
        tamanio = archivo.get_filesize()
        es_directorio = archivo.is_directory()
        fecha_mod = archivo.get_mtime_epoch()

        tipo = "DIRECTORIO" if es_directorio else "ARCHIVO"

        logging.info(f"{tipo} | {nombre} | {tamanio} bytes | mtime: {fecha_mod}")

    # ------------------------------------------------------------------
    # 5. Cerrar conexión
    # ------------------------------------------------------------------

    conexion.close()
    logging.info("Conexión SMB cerrada")


if __name__ == "__main__":
    conectar_a_smb()