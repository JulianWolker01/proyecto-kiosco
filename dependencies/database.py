from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Ruta donde se va a crear el archivo de la base de datos
SQLALCHEMY_DATABASE_URL = "sqlite:///./kiosco.db"

# connect_args es un requisito exclusivo de SQLite en FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Creamos la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Esta función es la que van a usar tus rutas para pedir una conexión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()