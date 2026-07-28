from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. La "dirección" de tu base de datos física
SQLALCHEMY_DATABASE_URL = "sqlite:///./kiosco.db"

# 2. El "Motor": Es el encargado de establecer la comunicación real con SQLite.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    # check_same_thread=False es un truquito obligatorio para que SQLite 
    # no se trabe cuando FastAPI reciba muchas peticiones al mismo tiempo.
    connect_args={"check_same_thread": False} 
)

# 3. La "Fábrica de Sesiones": Crea conexiones individuales para cada usuario que entra.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. El Molde Base: ¿Te acordás que en los Modelos pusimos "class Producto(Base):"? 
# Bueno, de acá sale ese "Base". Es lo que une la clase de Python con el Motor.
Base = declarative_base()

# 5. El Administrador de Conexiones (Dependencia)
def get_db():
    db = SessionLocal() # Abrimos una conexión nueva
    try:
        yield db # Se la prestamos a FastAPI para que haga lo que necesite
    finally:
        db.close() # Cuando FastAPI termina, cerramos la conexión para no saturar el sistema