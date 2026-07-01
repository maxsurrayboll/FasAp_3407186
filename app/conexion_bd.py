from sqlmodel import SQLModel, Session, create_engine
from fastapi import APIRouter, HTTPException, FastAPI
from typing import Annotated
from fastapi import Depends


nombre_bd = "bd_clientes_3407186.sqlite3"
url_bd = f"sqlite:///{nombre_bd}"

#motor de la BD
motor_db = create_engine(url_bd)

#definir el metodo para crear las tablas
def crear_tablas(app: FastAPI):
    SQLModel.metadata.create_all(motor_db)
    yield

#definir el metodo para crear las tablas
def obtener_sesion():
    with Session(motor_db) as mi_sesion:
        yield mi_sesion

#denominado inyeccion de dependencias.
#registrar la sesion como dependencia.
Sesion_dependencia = Annotated(Session, Depends(obtener_sesion)) 