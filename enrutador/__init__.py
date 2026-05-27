from . import clientes
from . import facturas
from . import transacciones

# Opcional: si quieres exportar directamente los routers
from .clientes import router as clientes_router
from .facturas import router as facturas_router
from .transacciones import router as transacciones_router

# Lista de routers para incluir fácilmente en main.py
routers = [
    clientes_router,
    facturas_router,
    transacciones_router,
]
