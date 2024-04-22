from fastapi import FastAPI
from routes.Auth import auth
from routes import consulta, rpersonas, registro_vehiculos, roficial, infracciones
import uvicorn

app = FastAPI()

app.include_router(rpersonas.rpersonas, tags=["Personas"])
app.include_router(registro_vehiculos.rvehiculos, tags=["Vehiculos"])
app.include_router(roficial.roficial, tags=["Oficiales"])
app.include_router(infracciones.rinfraccion, tags=["Infracciones"])
app.include_router(auth, tags=["Gestion Usuario"])
app.include_router(consulta.consulta, tags=["Consultas"])


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000)
    # config = uvicorn.Config("main:app", host="0.0.0.0", port=5000,
    #                         log_level="info", reload=True)
    # server = uvicorn.Server(config)
    # server.run()

    # uvicorn.run(app, host='127.0.0.1', port=5000)
