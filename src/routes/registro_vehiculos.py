from fastapi import FastAPI, APIRouter, Request, Header
from pydantic import BaseModel, EmailStr
from datetime import datetime
# from uuid import uuid4 as uuid
from utils.db import dbcon
from utils.Security import Security
from bson import ObjectId

rvehiculos = APIRouter()


class Dvehiculos(BaseModel):
    _id: str
    idp: str
    placa: str
    marca: str
    color: str
    registrado: datetime = datetime.now()


@rvehiculos.post("/rvehiculos")
def registro_personas(datos: Dvehiculos, Authorization: str = Header()):
    datos = dict(datos)
    v = Security.virify_token_r(Authorization.split(" ")[1])

    if v:
        con = dbcon.srit.personas.find_one({'_id': ObjectId(datos["idp"])})

        if con != None:
            bplaca = dbcon.srit.vehiculos.find_one(
                {'placa': datos["placa"]})
            if bplaca == None:
                registro = dbcon.srit.vehiculos.insert_one(datos)
                return {"message": "Vehiculo registrado"}
            else:
                return {"message": "Vehiculo ya registrado"}
        else:

            return {"error": "Persona no registrada"}
    else:
        respuesta = {"Auth": "No autorizado"}
        return respuesta, 401
