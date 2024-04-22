from fastapi import APIRouter, Depends, Security as Secu
from pydantic import BaseModel, EmailStr
from typing import Text
from datetime import datetime
# from uuid import uuid4 as uuid
from utils.db import dbcon
from utils.Security import Security
from schemas.infracciones import infraccionEntity, infracionesEntity, infraccionxeEntity, infraccionxesEntity
from bson import ObjectId
from fastapi.security.api_key import APIKeyHeader

rinfraccion = APIRouter()


token_key = APIKeyHeader(name="Authorization")


class Dinfraccion(BaseModel):
    placa: str
    multa: float
    idof: int
    comentario: Text
    registrado: datetime = datetime.now()


class Token(BaseModel):
    token: str


def get_current_token(auth_key: str = Secu(token_key)):
    return auth_key


@rinfraccion.put("/rinfraccion")
def registro_de_ingracciones(datos: Dinfraccion, curren_token: Token = Depends(get_current_token)):
    acceso = Security.verify_token_r(str(curren_token).split(" ")[1])
    if acceso:
        datosp = dict(datos)

        dbv1 = dbcon.srit.vehiculos.find_one({"placa": datosp["placa"]})
        dbv2 = dbcon.srit.oficiales.find_one({"id": datosp["idof"]})
        # dbv3 = dbcon.srit.infracciones.find().sort({'secuecial' : -1})
        # db.infracciones.countDocuments({}, { hint: "_id_"})
        dbv3 = dbcon.srit.infracciones.count_documents({})
        dbv3 += 1
        datosp.update({"secuencial": dbv3})

        if dbv1 != None:
            if dbv2 != None:
                dbcon.srit.infracciones.insert_one(datosp)
                mensaje = f"Infraccion registrada con el numero de secuencia " + \
                    str(datosp["secuencial"])
                return {"mensaje": mensaje}
            else:
                return {"mensaje": "Id de oficial no encontrado"}
        else:
            return {"mensaje": "registro de placa de vehiculo no encontrado"}
    else:
        todo = "more todo"
    return {"mensaje": "No autorizado"}


@rinfraccion.get("/infracciones")
def consulta_de_infracciones(curren_token: Token = Depends(get_current_token)):
    acceso = Security.verify_token_r(str(curren_token).split(" ")[1])
    if acceso:
        dbcommit = dbcon.srit.infracciones.find()
        if dbcommit != None:
            return infracionesEntity(dbcommit)
        else:
            return {"mensaje": " No se encontraron registros"}, 404

    else:
        return {"mensaje": "No autorizado"}


@rinfraccion.get("/infracciones_email")
def consulta_ingracciones_por_email(email: EmailStr):

    pipeline = [
    {
        '$project': {
            'idp': 1, 
            'fullname': 1, 
            'email': 1
        }
    }, {
        '$lookup': {
            'from': 'vehiculos', 
            'localField': 'idp', 
            'foreignField': 'idp', 
            'as': 'vehiculos'
        }
    }, {
        '$unwind': {
            'path': '$vehiculos'
        }
    }, {
        '$project': {
            '_id': 1, 
            'idp': 1, 
            'fullname': 1, 
            'email': 1, 
            'placa': '$vehiculos.placa', 
            'marca': '$vehiculos.marca'
        }
    }, {
        '$lookup': {
            'from': 'infracciones', 
            'localField': 'placa', 
            'foreignField': 'placa', 
            'as': 'infracciones'
        }
    }, {
        '$unwind': {
            'path': '$infracciones'
        }
    }, {
        '$project': {
            '_id': 1, 
            'fullname': 1, 
            'email': 1, 
            'idp': 1, 
            'placa': 1, 
            'marca': 1, 
            'multa': '$infracciones.multa', 
            'comentario': '$infracciones.comentario', 
            'pagado': '$infracciones.pagada'
        }
    }, {
        '$match': {
            'email': email
        }
    }
    ]

    dbcommint = dbcon.srit.personas.aggregate(pipeline)
    
    # infraccionEntity(dbcommint)

    return infraccionxesEntity(dbcommint)
