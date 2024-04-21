from fastapi import APIRouter, Depends, Security as Secu
from pydantic import BaseModel, EmailStr
from datetime import datetime
# from uuid import uuid4 as uuid
# para validacion del token
from fastapi.security.api_key import APIKeyHeader
from utils.db import dbcon
from utils.Security import Security

rpersonas = APIRouter()
token_key = APIKeyHeader(name="Authorization")


class Dpersonas(BaseModel):
    _id: str
    fullname: str
    email: EmailStr
    registrado: datetime = datetime.now()


class Token(BaseModel):
    token: str


def get_current_token(auth_key: str = Secu(token_key)):
    return auth_key


@rpersonas.post("/rpersonas")
def registro_personas(datos: Dpersonas, curren_token: Token = Depends(get_current_token)):
    nr = dict(datos)
    # print("Auth_get:", Authorization)   # Ojito borrar
    v = Security.verify_token_r(str(curren_token).split(" ")[1])

    if v:
        con = dbcon.srit.personas.find_one({'email': nr["email"]})

        if con == None:
            registro = dbcon.srit.personas.insert_one(nr)
            # print("NR:", registro)
            return {"message": "persona registrada"}
        else:

            return {"error": "correo ya registrado"}
    else:
        respuesta = {"Auth": "No autorizado"}
        return respuesta, 401
