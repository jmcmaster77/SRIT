from fastapi import APIRouter, Depends, Security as Secu
from schemas.personas import personaEntity, personasEntity
from utils.db import dbcon
from utils.Security import Security
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel, EmailStr

token_key = APIKeyHeader(name="Authorization")


class Token(BaseModel):
    token: str


consulta = APIRouter()


def get_current_token(auth_key: str = Secu(token_key)):

    return auth_key


@consulta.get('/personas')
def consulta_personas(curren_token: Token = Depends(get_current_token)):
    # tk = str(curren_token).split(' ')[1]

    has_access = Security.verify_token_r(str(curren_token).split(' ')[1])
    if has_access:
        try:
            consulta = dbcon.srit.personas.find()
            return personasEntity(consulta)
        except Exception as error:

            return {"Mensaje": error}
    else:
        respuesta = {"Auth": "No autorizado"}
        return respuesta, 401


@consulta.get("/get_person_by_email")
def buscar_persona_por_email(email:EmailStr):
    
    dbcommit = dbcon.srit.personas.find_one({"email":email})
    if dbcommit == None:
        return {"mensaje":"correo no encontrado"}
    else:
        return personaEntity(dbcommit)