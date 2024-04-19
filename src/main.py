from fastapi import FastAPI
from fastapi import APIRouter
from routes.Auth import auth
from routes.consulta import consulta
from routes.rpersonas import rpersonas
from routes.registro_vehiculos import rvehiculos
import uvicorn

app = FastAPI()

app.include_router(rpersonas, tags=["Registro de Personas"])
app.include_router(rvehiculos, tags=["Registro de Vehiculos"])
app.include_router(auth, tags=["Autenticacion"])
app.include_router(consulta, tags=["Consultas"])


if __name__ == '__main__':
    config = uvicorn.Config("main:app", port=5000,
                            log_level="info", reload=True)
    server = uvicorn.Server(config)

    server.run()

    # uvicorn.run(app, host='127.0.0.1', port=5000)
