from pathlib import Path

# Ruta raíz del proyecto
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Configuración del servidor SMB
SERVER_IP = "127.0.0.1"
SERVER_PORT = 1445
SHARE_NAME = "C$"

# -------------------------------------------------
# Rutas importantes del proyecto
# -------------------------------------------------

DATA_DIR = PROJECT_ROOT / "data"

# Carpeta compartida por el servidor SMB
SHARE_PATH = DATA_DIR / "simulacro_c_drive"