# Proyecto FastAPI - Gestión de Clientes, Facturas y Transacciones

Este proyecto implementa una API con **FastAPI** organizada en módulos y routers para manejar clientes, facturas y transacciones.

---

## Pasos realizados

### 1. Estructura del proyecto
Se organizó el proyecto en la carpeta `app/` con subcarpetas para **modelos** y **enrutador**:


### 2. Creación de `__init__.py`
- Se agregó `__init__.py` en **app**, **modelos** y **enrutador** para que las carpetas sean reconocidas como paquetes.
- En `app/__init__.py` se inicializó la instancia principal de FastAPI y se incluyeron los routers.

### 3. Routers con APIRouter
Se implementaron routers CRUD en `enrutador/`:
- **clientes.py** → Endpoints para listar, crear, editar y eliminar clientes.
- **facturas.py** → Endpoints para listar, crear, editar y eliminar facturas.
- **transacciones.py** → Endpoints para listar, crear, editar y eliminar transacciones.

Cada router se conecta en `main.py` mediante `app.include_router(...)`.

### 4. Archivo `requirements.txt`
Se creó el archivo `requirements.txt` en la raíz del proyecto con las dependencias necesarias:


Esto permite instalar todas las librerías con:
```bash 

Hecho por Esteban banquet perez Ficha: 3407186
