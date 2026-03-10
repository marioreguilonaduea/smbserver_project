import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def listar_archivos(conexion, share):
    """
    Lista archivos del recurso compartido.
    """
    logging.info(f"Listando contenido del recurso compartido {share}")

    archivos = conexion.listPath(share, "*")

    for archivo in archivos:
        nombre = archivo.get_longname()
        tamanio = archivo.get_filesize()
        es_directorio = archivo.is_directory()
        fecha_mod = archivo.get_mtime_epoch()

        tipo = "DIRECTORIO" if es_directorio else "ARCHIVO"

        logging.info(f"{tipo} | {nombre} | {tamanio} bytes | mtime: {fecha_mod}")

def subir_archivo(conexion, share, archivo_local, archivo_remoto):
    """
    Sube un archivo local al share SMB.
    """

    logging.info(f"Subiendo archivo {archivo_local} al share {share} como {archivo_remoto}")

    with open(archivo_local, "rb") as f:
        conexion.putFile(share, archivo_remoto, f.read)

    logging.info(f"Archivo {archivo_remoto} subido correctamente")