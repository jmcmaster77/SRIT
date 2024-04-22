from fastapi import APIRouter, Depends, Security as Secu
from pydantic import BaseModel
from datetime import datetime
# from uuid import uuid4 as uuid
# para validacion del token
from fastapi.security.api_key import APIKeyHeader
from utils.db import dbcon
from utils.Security import Security

roficial = APIRouter()
token_key = APIKeyHeader(name="Authorization")


class Doficial(BaseModel):
    id: str
    fullname: str
    registrado: datetime = datetime.now()


class Token(BaseModel):
    token: str


def get_current_token(auth_key: str = Secu(token_key)):
    return auth_key


@roficial.post("/roficial")
def registro_oficiales(datos: Doficial, curren_token: Token = Depends(get_current_token)):
    datosd = dict(datos)
    v = Security.verify_token_r(str(curren_token).split(" ")[1])

    if v:
        con = dbcon.srit.oficiales.find_one({'id': datosd["id"]})

        if con == None:
            registro = dbcon.srit.oficiales.insert_one(datosd)
            # print("NR:", registro)
            return {"message": "Oficial registrado"}
        else:

            return {"error": "Id Oficial ya existe"}
    else:
        respuesta = {"Auth": "No autorizado"}
        return respuesta, 401
