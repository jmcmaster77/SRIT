from fastapi import FastAPI
from routes.Auth import auth
from routes import consulta, rpersonas, registro_vehiculos, roficial
import uvicorn

app = FastAPI()

app.include_router(rpersonas.rpersonas, tags=["Registro"])
app.include_router(registro_vehiculos.rvehiculos, tags=["Registro"])
app.include_router(roficial.roficial, tags=["Registro"])
app.include_router(auth, tags=["Autenticacion"])
app.include_router(consulta.consulta, tags=["Consultas"])


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000)
    # config = uvicorn.Config("main:app", host="0.0.0.0", port=5000,
    #                         log_level="info", reload=True)
    # server = uvicorn.Server(config)
    # server.run()

    # uvicorn.run(app, host='127.0.0.1', port=5000)
