from datetime import datetime

from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear
from modelos.transacciones import Transacciones, TransaccionesCrear


app = FastAPI()

lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transacciones] = []  # inicializar lista vacía

# ---------------- CLIENTES ----------------

@app.get("/clientes")
async def listar_clientes():
    return {"Clientes": lista_clientes}


@app.get("/clientes/{id}")
async def listar_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@app.post("/clientes", response_model=Cliente)
async def crear_clientes(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    cliente_val.id = len(lista_clientes) + 1
    lista_clientes.append(cliente_val)
    return cliente_val


@app.put("/clientes/{id}")
def editar_clientes(id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = id
            lista_clientes[i] = cliente_val
            return {
                "mensaje": "Se actualizó el cliente satisfactoriamente.",
                "Cliente": cliente_val,
            }
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@app.delete("/clientes/{id}")
def eliminar_clientes(id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            lista_clientes.pop(i)
            return {"mensaje": "Cliente eliminado"}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# ---------------- FACTURAS ----------------

@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas


@app.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_facturas(cliente_id: int, datos_factura: FacturaCrear):
    cliente_encontrado = next((c for c in lista_clientes if c.id == cliente_id), None)

    if not cliente_encontrado:
        raise HTTPException(
            status_code=400,
            detail=f"Cliente con id {cliente_id} no existe, debes crear.",
        )

    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.id = len(lista_facturas) + 1
    factura_val.fecha = datetime.now()
    factura_val.cliente = cliente_encontrado
    lista_facturas.append(factura_val)
    return factura_val


# ---------------- TRANSACCIONES ----------------

@app.get("/transacciones", response_model=list[Transacciones])
async def listar_transacciones():
    return lista_transacciones


@app.post("/transacciones/{factura_id}")
async def crear_transaccion(
    factura_id: int, datos_transaccion: TransaccionesCrear, cliente_id: int
):
    cliente_encontrado = next((c for c in lista_clientes if c.id == cliente_id), None)

    if not cliente_encontrado:
        raise HTTPException(
            status_code=400,
            detail=f"No existe un cliente con id {cliente_id}, debes crearlo primero.",
        )

    factura_encontrada = next((f for f in lista_facturas if f.id == factura_id), None)

    if factura_encontrada:
        if factura_encontrada.cliente.id == cliente_id:
            transaccion_val = Transacciones.model_validate(datos_transaccion.model_dump())
            transaccion_val.id = len(lista_transacciones) + 1
            transaccion_val.factura_id = factura_id
            lista_transacciones.append(transaccion_val)

            factura_encontrada.transacciones.append(transaccion_val)
            return {
                "mensaje": f"Transacción agregada a factura {factura_encontrada.id}",
                "factura": factura_encontrada,
            }
        else:
            return {
                "mensaje": f"Factura {factura_id} pertenece a otro cliente (id: {factura_encontrada.cliente.id})",
                "factura encontrada": factura_encontrada,
            }
    else:
        # si no se encontró factura, crear una nueva con la transacción
        transaccion_val = Transacciones.model_validate(datos_transaccion.model_dump())
        transaccion_val.id = len(lista_transacciones) + 1
        transaccion_val.factura_id = len(lista_facturas) + 1

        factura = FacturaCrear(
            cliente=cliente_encontrado,
            fecha=str(datetime.now()),
            transacciones=[transaccion_val],
        )

        factura_val = Factura.model_validate(factura.model_dump())
        factura_val.id = len(lista_facturas) + 1
        lista_facturas.append(factura_val)
        lista_transacciones.append(transaccion_val)

        return {
            "mensaje": f"No existía factura con id {factura_id}, se creó una nueva.",
            "factura": factura_val,
        }
