from fastapi import FastAPI
from routes import Auth, rpersonas, registro_vehiculos, roficial, infracciones
import uvicorn

app = FastAPI()

app.include_router(rpersonas.rpersonas, tags=["Personas"])
app.include_router(registro_vehiculos.rvehiculos, tags=["Vehiculos"])
app.include_router(roficial.roficial, tags=["Oficiales"])
app.include_router(infracciones.rinfraccion, tags=["Infracciones"])
app.include_router(Auth.auth, tags=["Gestion Usuario"])


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)
