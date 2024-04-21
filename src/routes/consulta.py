from fastapi import APIRouter, Depends, Security as Secu
from schemas.personas import personaEntity, personasEntity
from utils.db import dbcon
from utils.Security import Security
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel

token_key = APIKeyHeader(name="Authorization")


class Token(BaseModel):
    token: str


consulta = APIRouter()


def get_current_token(auth_key: str = Secu(token_key)):

    return auth_key


@consulta.get('/consulta')
def get_consulta(curren_token: Token = Depends(get_current_token)):
    # tk = str(curren_token).split(' ')[1]

    has_access = Security.verify_token_r(str(curren_token).split(' ')[1])
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
