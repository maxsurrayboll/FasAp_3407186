from fastapi import FastAPI

# Crear la instancia principal de FastAPI
app = FastAPI()

# Aquí puedes importar y registrar routers si quieres centralizar
from app.enrutador import clientes, facturas, transacciones

app.include_router(clientes.router)
app.include_router(facturas.router)
app.include_router(transacciones.router)
