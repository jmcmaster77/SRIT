from fastapi import FastAPI, APIRouter, Request
from schemas.personas import personaEntity, personasEntity
from utils.db import dbcon
from utils.Security import Security

consulta = APIRouter()


@consulta.get('/consulta')
def get_consulta(request: Request):

    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            consulta = (personasEntity(dbcon.srit.personas.find()))
            return consulta
        except Exception as error:
            print(error)
            return
    else:
        respuesta = {"Auth": "No autorizado"}
        return respuesta, 401
