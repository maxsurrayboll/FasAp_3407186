from fastapi import APIRouter
from app.modelos.facturas import Factura, FacturaCrear, FacturaEditar

# Crear el router específico para facturas
router = APIRouter(
    prefix="/facturas",
    tags=["facturas"]
)

# Endpoints CRUD básicos

# Obtener todas las facturas
@router.get("/", response_model=list[Factura])
def listar_facturas():
    # Aquí iría la lógica para traer facturas de la BD
    return []

# Crear una nueva factura
@router.post("/", response_model=Factura)
def crear_factura(factura: FacturaCrear):
    # Aquí iría la lógica para guardar en la BD
    return factura

# Editar una factura existente
@router.put("/{factura_id}", response_model=Factura)
def editar_factura(factura_id: int, factura: FacturaEditar):
    # Aquí iría la lógica para actualizar en la BD
    return factura

# Eliminar una factura
@router.delete("/{factura_id}")
def eliminar_factura(factura_id: int):
    # Aquí iría la lógica para borrar en la BD
    return {"mensaje": f"Factura {factura_id} eliminada"}
