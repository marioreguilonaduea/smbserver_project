import logging
from impacket.smbconnection import SMBConnection
from src.shared.config import SERVER_IP, SERVER_PORT

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def crear_conexion():
    """
    Crea la conexión SMB y realiza login.
    """
    logging.info(f"Intentando conectar al servidor SMB {SERVER_IP}:{SERVER_PORT}")

    conexion = SMBConnection(SERVER_IP, SERVER_IP, sess_port=SERVER_PORT)

    conexion.login("", "")

    logging.info("Conexión SMB establecida correctamente")

    return conexion