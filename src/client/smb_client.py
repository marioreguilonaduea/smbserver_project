"""
smb_client.py

Este script actúa como cliente SMB.
Se conecta a un servidor SMB levantado previamente y accede
al recurso compartido C$.

El objetivo es verificar que el cliente puede conectarse, subir un archivo
y ver el contenido del share.
"""

from src.shared.config import SHARE_NAME, DATA_DIR
from src.client.connection import crear_conexion, cerrar_conexion
from src.client.file_ops import (
    listar_archivos,
    listar_archivos_recursivo,
    subir_archivo,
    descargar_archivo,
    renombrar_archivo,
    eliminar_archivo
)


def main():

    conexion = crear_conexion()

    print("\nCliente SMB interactivo conectado.")
    print("Comandos disponibles:")
    print("  ls")
    print("  lsrec")
    print("  upload <archivo_local> <archivo_remoto>")
    print("  download <archivo_remoto> <archivo_local>")
    print("  rename <archivo_actual> <archivo_nuevo>")
    print("  delete <archivo>")
    print("  exit\n")

    while True:

        comando = input("smb-client> ").strip()

        if not comando:
            continue

        partes = comando.split()

        cmd = partes[0]

        try:

            if cmd == "ls":
                listar_archivos(conexion, SHARE_NAME)

            elif cmd == "lsrec":
                listar_archivos_recursivo(conexion, SHARE_NAME)

            elif cmd == "upload":
                archivo_local = DATA_DIR / partes[1]
                archivo_remoto = partes[2]

                subir_archivo(conexion, SHARE_NAME, archivo_local, archivo_remoto)

            elif cmd == "download":
                archivo_remoto = partes[1]
                archivo_local = DATA_DIR / partes[2]

                descargar_archivo(conexion, SHARE_NAME, archivo_remoto, archivo_local)

            elif cmd == "rename":
                archivo_actual = partes[1]
                archivo_nuevo = partes[2]

                renombrar_archivo(conexion, SHARE_NAME, archivo_actual, archivo_nuevo)

            elif cmd == "delete":
                archivo = partes[1]

                eliminar_archivo(conexion, SHARE_NAME, archivo)

            elif cmd == "exit":
                break

            else:
                print("Comando no reconocido.")

        except Exception as e:
            print(f"Error ejecutando comando: {e}")

    cerrar_conexion(conexion)


if __name__ == "__main__":
    main()