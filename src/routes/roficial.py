from fastapi import APIRouter, Depends, Security as Secu
from pydantic import BaseModel
from datetime import datetime
from schemas.oficiales import oficialEntity, oficialesEntity
# from uuid import uuid4 as uuid
# para validacion del token
from fastapi.security.api_key import APIKeyHeader
from utils.db import dbcon
from utils.Security import Security
from bson import ObjectId
from passlib.hash import sha256_crypt

roficial = APIRouter()
token_key = APIKeyHeader(name="Authorization")


class Doficial(BaseModel):
    fullname: str
    username: str
    password: str
    password2: str
    registrado: datetime = datetime.now()


class Token(BaseModel):
    token: str


def get_current_token(auth_key: str = Secu(token_key)):
    return auth_key


@roficial.post("/roficial")
def registro_oficiales(datos: Doficial, curren_token: Token = Depends(get_current_token)):
    datosd = dict(datos)
    v = Security.verify_token_r(curren_token)

    if v:
        con = dbcon.srit.oficiales.find_one({'username': datosd["username"]})
        # dbv3 = dbcon.srit.oficiales.count_documents({})
        # dbv3 += 1
        resultado = dbcon.srit.oficiales.find({}).sort({"idof": -1 }).limit(1)
    
        if resultado != None:
            ll = resultado.next()
            dbv3 = int(ll["idof"])
            dbv3 += 1
            datosd.update({"idof": dbv3})

        if con == None:
            if datosd["password"] == datosd["password2"]:
                del datosd["password2"]
                datosd["password"] = sha256_crypt.encrypt(datosd["password"])

                registro = dbcon.srit.oficiales.insert_one(datosd)

                return {"message": "Oficial registrado"}
            else:
                return {"message": "password no coinciden"}

        else:

            return {"error": "Usuario ya existe"}
    else:
        respuesta = {"mensaje": "No autorizado"}
        return respuesta, 401


@roficial.get("/roficial")
def buscar_oficiales(curren_token: Token = Depends(get_current_token)):
    acceso = Security.verify_token_r(curren_token)
    if acceso:
        dbcommit = dbcon.srit.oficiales.find()
        if dbcommit != None:
            return oficialesEntity(dbcommit)
        else:
            return {"mensaje": " No se encontraron registros"}, 404

    else:

        return {"mensaje": "No autorizado"}


@roficial.get("/roficial/{id}")
def buscar_oficial_id(id: int, curren_token: Token = Depends(get_current_token)):
    acceso = Security.verify_token_r(curren_token)
    if acceso:
        dbcommit = dbcon.srit.oficiales.find_one({"idof": id})
        if dbcommit != None:
            return oficialEntity(dbcommit)
        else:
            return {"mensaje": " Id no encontrado"}, 404
    else:

        return {"mensaje": "No autorizado"}


@roficial.put("/roficial/{id}")
def modificar_registro_de_oficial_obj_id(id: str, datos: Doficial, curren_token: Token = Depends(get_current_token)):
    acceso = Security.verify_token_r(curren_token)
    if acceso:
        fo = dict(datos)
        if fo["password"] == fo["password2"]:
            del fo["password2"]
            fo["password"] = sha256_crypt.encrypt(fo["password"])
            dbcommit = dbcon.srit.oficiales.find_one_and_update(
                {"_id": ObjectId(id)}, {"$set": fo})
            if dbcommit != None:
                return {"mensaje": "Registro de oficial modificado"}
            else:
                return {"mensaje": "Id no encontrado "}, 404
        else:
            return {"mensaje": "password no coinciden"}
    else:
        to_do = "no go"

        return {"mensaje": "No autorizado"}


@roficial.delete("/roficial/{id}")
def borrar_registo_de_oficial(id: str, curren_token: Token = Depends(get_current_token)):
    acceso = Security.verify_token_r(curren_token)
    if acceso:
        dbv = dbcon.srit.oficiales.find_one({"_id": ObjectId(id)})
        if dbv != None:
            
            datosv = oficialEntity(dbv)
            cdb = dbcon.srit.infracciones.find_one({"idof": datosv["idof"]})
            if cdb == None:
                dbcon.srit.oficiales.find_one_and_delete({"_id": ObjectId(id)})

                return {"mensaje": "Registro de oficial eliminado"}
            else:
                return {"mensaje": "Oficial tiene registros infraccion asignados, debe asignar a otros oficiales"}
        else:
            return {"mensaje": "Registro de oficial no encontrado"}
    else:

        return {"Mensaje": "No autorizado"}

from bson.json_util import dumps, loads

# @roficial.get("/prueba")
# def prueba():

#     resultado = dbcon.srit.oficiales.find({}).sort({"idof": -1 }).limit(1)
    
#     if resultado != None:
#         print(resultado)
#         ll = resultado.next()
#         print("Resultado", int(ll["idof"]))
#         gdata = int(ll["idof"])
#         gdata += 1
#         print("gdata +1 carajo", gdata)
#         # for doc in resultado:
#         #     print(doc)
        
        
    
#         # print("resultado 2 ", resultado)
        
#     return {"Mensaje": "Dev"}