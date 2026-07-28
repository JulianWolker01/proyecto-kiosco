from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List
from .detalle_venta import DetalleVentaCreate, DetalleVentaResponse

class VentaBase(BaseModel):
    metodo_pago: str

class VentaCreate(VentaBase):
    # Recibimos una lista de detalles directamente cuando creamos la venta
    detalles: List[DetalleVentaCreate]

class VentaResponse(VentaBase):
    id: int
    fecha: datetime
    # Devolvemos la venta con todos sus ítems adentro
    detalles: List[DetalleVentaResponse] = []
    
    model_config = ConfigDict(from_attributes=True)