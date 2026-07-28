from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base # Si te marca error, probá con: from database.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio_venta = Column(Float, nullable=False)
    costo = Column(Float,nullable=False)
    stock = Column(Integer, nullable=False)

    
    # Esto es magia de Python: vincula el producto con su historial de ventas
    detalles = relationship("DetalleVenta", back_populates="producto")