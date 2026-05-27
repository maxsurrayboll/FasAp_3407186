from datetime import datetime

from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear
from modelos.transacciones import Transacciones, TransaccionesCrear
app = FastAPI()

#lista de clientes BD
lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transacciones]


#listar clientes
@app.get("/clientes")
async def listar_clientes():
    # Creacion de sms mas adecuado al usuario
    return {"Clientes": lista_clientes}


@app.get("/clientes/{id}")
async def listar_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return cliente


@app.post("/clientes", response_model=Cliente)
async def crear_clientes(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    cliente_val.id = len(lista_clientes) + 1  # id incremento
    lista_clientes.append(cliente_val)
    return cliente_val
    # return {"Cliente": cliente_val}


@app.put("/clientes/{id}")
def editar_clientes(id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = id
            lista_clientes[i] = cliente_val

    return {
        "mensaje": "Se actualizo el cliente satisfactoriamente.",
        "Cliente": cliente_val,
    }


@app.delete("/clientes")
def eliminar_clientes():
    return {"Cliente": "Cliente eliminado"}


