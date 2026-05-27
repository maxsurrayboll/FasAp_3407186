from fastapi import APIRouter
from app.modelos.clientes import Cliente, ClienteCrear, ClienteEditar

# Crear el router específico para clientes
router = APIRouter(
    prefix="/clientes",
    tags=["clientes"]
)

# Endpoints CRUD básicos

# Obtener todos los clientes
@router.get("/", response_model=list[Cliente])
def listar_clientes():
    # Aquí iría la lógica para traer clientes de la BD
    return []

# Crear un nuevo cliente
@router.post("/", response_model=Cliente)
def crear_cliente(cliente: ClienteCrear):
    # Aquí iría la lógica para guardar en la BD
    return cliente

# Editar un cliente existente
@router.put("/{cliente_id}", response_model=Cliente)
def editar_cliente(cliente_id: int, cliente: ClienteEditar):
    # Aquí iría la lógica para actualizar en la BD
    return cliente

# Eliminar un cliente
@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    # Aquí iría la lógica para borrar en la BD
    return {"mensaje": f"Cliente {cliente_id} eliminado"}
