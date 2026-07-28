from pydantic import BaseModel, ConfigDict

class ProductoBase(BaseModel):
    nombre: str
    precio_venta: float
    stock: int

# Lo usamos para crear (por ahora es igual a la base)
class ProductoCreate(ProductoBase):
    pass

# Lo usamos para devolverle los datos al usuario
class ProductoResponse(ProductoBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)