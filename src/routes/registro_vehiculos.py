from fastapi import APIRouter, Depends, Security as Secu
from pydantic import BaseModel
from datetime import datetime
# from uuid import uuid4 as uuid
from utils.db import dbcon
from utils.Security import Security
from schemas.vehiculos import vehiculoEntity, vehiculosEntity
from bson import ObjectId
from fastapi.security.api_key import APIKeyHeader

rvehiculos = APIRouter()

token_key = APIKeyHeader(name="Authorization")


class Token(BaseModel):
    token: str


class Dvehiculos(BaseModel):
    _id: str
    idp: int
    placa: str
    marca: str
    color: str
    registrado: datetime = datetime.now()


def get_current_token(auth_key: str = Secu(token_key)):

    return auth_key


@rvehiculos.post("/rvehiculos")
def registro_vehiculos(datos: Dvehiculos, curren_token: Token = Depends(get_current_token)):
    datosd = dict(datos)
    v = Security.verify_token_r(str(curren_token).split(" ")[1])

    if v:
        con = dbcon.srit.personas.find_one({'idp': datosd["idp"]})

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
        respuesta = {"Mensaje": "No autorizado"}
        return respuesta, 401


@rvehiculos.get("/rvehiculos")
def consulta_vehiculos(curren_token: Token = Depends(get_current_token)):
    acceso = Security.verify_token_r(str(curren_token).split(" ")[1])
    if acceso:
        consulta = dbcon.srit.vehiculos.find()

        if consulta != None:

            return vehiculosEntity(consulta)
        else:
            return {"Mensaje": "No se encontraron registros"}, 404
    else:

        return {"Mensaje": "No autorizado"}


@rvehiculos.get("/rvehiculos/{id}")
def consulta_vehiculos_por_id(id: str, curren_token: Token = Depends(get_current_token)):
    acceso = Security.verify_token_r(str(curren_token).split(" ")[1])
    if acceso:
        consulta = dbcon.srit.vehiculos.find_one({'_id': ObjectId(id)})
        
        if consulta != None:
            return vehiculoEntity(consulta)
        else:
            return {"Mensaje": "Id no encontrado"}
    else:

        return {"Mensaje": "No autorizado"}


@rvehiculos.get("/rvehiculos/p/{placa}")
def consulta_vehiculos_por_placa(placa: str, curren_token: Token = Depends(get_current_token)):
    acceso = Security.verify_token_r(str(curren_token).split(" ")[1])
    if acceso:
        consulta = dbcon.srit.vehiculos.find_one({'placa': placa})
        print(consulta)
        if consulta != None:
            return vehiculoEntity(consulta)
        else:
            return {"Mensaje": "Placa no registrada"}
    else:

        return {"Mensaje": "No autorizado"}                          
    


@rvehiculos.put("/rvehiculos/{id}")
def modificar_registro_vehiculo(id: str, vehiculo: Dvehiculos,  curren_token: Token = Depends(get_current_token)):
    acceso = Security.verify_token_r(str(curren_token).split(" ")[1])
    if acceso:
        fv = dict(vehiculo)
        # valida que el id de la persona este registrado
        dbvalidate = dbcon.srit.personas.find_one({"idp": fv["idp"]})

        if dbvalidate == None:
            return {"mensaje":"Id de Persona no validado"}
        
        else:

            dbcommit = dbcon.srit.vehiculos.find_one_and_update(
                {"_id": ObjectId(id)}, {"$set": fv})

            if dbcommit == None:
                return {"mensaje": "Id no encontrado"}
            else:
                return {"mensaje": "Registro modificado"}
    else:
        return


@rvehiculos.delete("/rvehiculos/{id}")
def eliminar_registro_vehiculos(id: str, curren_token: Token = Depends(get_current_token)):
    acceso = Security.verify_token_r(str(curren_token).split(" ")[1])
    if acceso:
        to_do = "Dev"
    else:
        more_to_do = "Dev dev"

    
        return {"Mensaje":"Dev"}