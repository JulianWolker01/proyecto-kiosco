from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class DetalleVenta(Base):
    __tablename__ = "detalles_venta"

    detalle_id = Column(Integer, primary_key=True, index=True)
    venta_id = Column(Integer, ForeignKey("ventas.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)

    # Le enseñamos a Python cómo viajar de un lado al otro
    venta = relationship("Venta", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalles")