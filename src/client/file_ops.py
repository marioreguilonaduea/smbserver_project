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

def listar_archivos_recursivo(conexion, share, ruta=""):
    """
    Lista archivos y carpetas recursivamente dentro del share SMB
    mostrando la ruta completa.
    """

    archivos = conexion.listPath(share, f"{ruta}*")

    for archivo in archivos:

        nombre = archivo.get_longname()

        #Ignorar las entradas especiales
        if nombre in [".", ".."]:
            continue

        ruta_completa = f"{ruta}{nombre}"

        es_directorio = archivo.is_directory()
        fecha_mod = archivo.get_mtime_epoch()

        tipo = "DIRECTORIO" if es_directorio else "ARCHIVO"

        if es_directorio:
            logging.info(f"{tipo} | {ruta_completa} | - | mtime: {fecha_mod}")
            listar_archivos_recursivo(conexion, share, ruta_completa + "/")
        else:
            tamanio = archivo.get_filesize()
            logging.info(f"{tipo} | {ruta_completa} | {tamanio} bytes | mtime: {fecha_mod}")


def subir_archivo(conexion, share, archivo_local, archivo_remoto):
    """
    Sube un archivo local al share SMB.
    """
    logging.info(f"Subiendo archivo {archivo_local} al share {share} como {archivo_remoto}")

    with open(archivo_local, "rb") as f:
        conexion.putFile(share, archivo_remoto, f.read)

    logging.info(f"Archivo {archivo_remoto} subido correctamente")

def descargar_archivo(conexion, share, archivo_remoto, archivo_local):
    """
    Descarga un archivo del share SMB al sistema local.
    """
    logging.info(f"Descargando archivo {archivo_remoto} desde {share} a {archivo_local}")

    with open(archivo_local, "wb") as f:
        conexion.getFile(share, archivo_remoto, f.write)

    logging.info(f"Archivo {archivo_remoto} descargado correctamente")

def renombrar_archivo(conexion, share, nombre_actual, nombre_nuevo):
    """
    Renombra un archivo dentro del share SMB.
    """

    logging.info(f"Renombrando archivo {nombre_actual} a {nombre_nuevo}")

    ruta_origen = f"/{nombre_actual}"
    ruta_destino = f"/{nombre_nuevo}"

    conexion.rename(share, ruta_origen, ruta_destino)

    logging.info(f"Archivo renombrado correctamente a {nombre_nuevo}")

def eliminar_archivo(conexion, share, archivo_remoto):
    """
    Elimina un archivo del share SMB.
    """
    logging.info(f"Borrando archivo {archivo_remoto}")

    conexion.deleteFile(share, archivo_remoto)

    logging.info(f"Archivo {archivo_remoto} eliminado correctamente")
