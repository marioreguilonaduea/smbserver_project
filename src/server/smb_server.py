"""
smb_server.py

Este script levanta un servidor SMB usando la librería Impacket.
El servidor compartirá una carpeta local como si fuera el disco C$
de un equipo Windows.

Otros equipos o scripts podrán conectarse usando SMB al puerto 445
y acceder al recurso compartido.

Ejemplo de acceso desde Windows:
net use Z: \\\\IP_DEL_SERVIDOR\\C$
"""

import os
import logging
from impacket.smbserver import SimpleSMBServer
from src.shared.config import SERVER_PORT, SHARE_NAME, SHARE_PATH


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def iniciar_smb_funcional():
    """
    Función que configura y arranca el servidor SMB.
    """

    # 1. Crear carpeta que actuará como disco compartido
    ruta_compartida = str(SHARE_PATH)
    os.makedirs(ruta_compartida, exist_ok=True)

    logging.info("Carpeta compartida creada o ya existente.")
    logging.info(f"Ruta local compartida: {ruta_compartida}")

    # 2. Crear servidor SMB
    # listenAddress = 0.0.0.0 significa que escuchará en todas las interfaces
    # listenPort = 445 es el puerto estándar de SMB
    server = SimpleSMBServer(listenAddress="0.0.0.0", listenPort=SERVER_PORT)
    logging.info(f"Servidor SMB configurado para escuchar en el puerto {SERVER_PORT}")

    # 3. Añadir recurso compartido
    # Creamos un share llamado "C$"
    # Esto simula el disco administrativo típico de Windows
    server.addShare(
        SHARE_NAME,        # Nombre del recurso compartido
        ruta_compartida,   # Carpeta local
        "Disco C Simulado" # Descripción
    )
    logging.info(f"Recurso compartido SMB creado: {SHARE_NAME}")

    # 4. Activar soporte SMB2 / SMB3
    # Muy importante para que funcione con sistemas modernos
    server.setSMB2Support(True)
    logging.info("Soporte SMB2 activado")

    # 5. Autenticación (OPCIONAL)
    # Si se comenta esta línea el servidor acepta conexiones anónimas
    # server.addCredential("administrador", "Simulacro2026", "DOMINIO_SIMULADO", "")

    # 6. Iniciar servidor
    # El servidor entra en un bucle infinito esperando conexiones SMB
    try:
        logging.info("Servidor SMB iniciado correctamente.")
        logging.info("Esperando conexiones...")

        server.start()

    except Exception as e:
        logging.error(f"Error al iniciar el servidor SMB: {e}")
        logging.error("Puede que necesites ejecutar el script como administrador/root.")


if __name__ == "__main__":
    iniciar_smb_funcional()


