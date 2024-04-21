from fastapi import APIRouter, Depends, Security as Secu
from pydantic import BaseModel
from datetime import datetime
# from uuid import uuid4 as uuid
from utils.db import dbcon
from utils.Security import Security
from bson import ObjectId
from fastapi.security.api_key import APIKeyHeader

rvehiculos = APIRouter()

token_key = APIKeyHeader(name="Authorization")


class Token(BaseModel):
    token: str


class Dvehiculos(BaseModel):
    _id: str
    idp: str
    placa: str
    marca: str
    color: str
    registrado: datetime = datetime.now()


def get_current_token(auth_key: str = Secu(token_key)):

    return auth_key


@rvehiculos.post("/rvehiculos")
def registro_personas(datos: Dvehiculos, curren_token: Token = Depends(get_current_token)):
    datosd = dict(datos)
    v = Security.verify_token_r(str(curren_token).split(" ")[1])

    if v:
        con = dbcon.srit.personas.find_one({'_id': ObjectId(datosd["idp"])})

        if con != None:
            bplaca = dbcon.srit.vehiculos.find_one(
                {'placa': datosd["placa"]})
            if bplaca == None:
                registro = dbcon.srit.vehiculos.insert_one(datosd)
                return {"message": "Vehiculo registrado"}
            else:
                return {"message": "Vehiculo ya registrado"}
        else:

            return {"error": "Persona no registrada"}
    else:
        respuesta = {"Auth": "No autorizado"}
        return respuesta, 401
