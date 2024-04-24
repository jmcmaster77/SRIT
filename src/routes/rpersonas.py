from fastapi import APIRouter, Depends, Security as Secu
from pydantic import BaseModel, EmailStr
from datetime import datetime
from schemas.personas import personaEntity, personasEntity
# from uuid import uuid4 as uuid
# para validacion del token
from fastapi.security.api_key import APIKeyHeader
from utils.db import dbcon
from schemas.personas import personaEntity
from utils.Security import Security
from bson import ObjectId

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


@rpersonas.get('/personas')
def consulta_personas(curren_token: Token = Depends(get_current_token)):
    has_access = Security.verify_token_r(curren_token)
    if has_access:
        try:
            consulta = dbcon.srit.personas.find()
            return personasEntity(consulta)
        except Exception as error:

            return {"Mensaje": error}
    else:
        respuesta = {"Auth": "No autorizado"}
        return respuesta, 401


@rpersonas.get("/get_person_by_email")
def buscar_persona_por_email(email: EmailStr):

    dbcommit = dbcon.srit.personas.find_one({"email": email})
    if dbcommit == None:
        return {"mensaje": "correo no encontrado"}
    else:
        return personaEntity(dbcommit)


@rpersonas.post("/rpersonas")
def registro_persona(datos: Dpersonas, curren_token: Token = Depends(get_current_token)):
    nr = dict(datos)
    # print("Auth_get:", Authorization)   # Ojito borrar
    v = Security.verify_token_r(curren_token)

    if v:

        con = dbcon.srit.personas.find_one({'email': nr["email"]})

        if con == None:
            # dbv3 = dbcon.srit.personas.count_documents({})
            # dbv3 += 1
            resultado = dbcon.srit.personas.find({}).sort({"idp": -1 }).limit(1)
    
            if resultado != None:
                ll = resultado.next()
                dbv3 = int(ll["idp"])
                dbv3 += 1
                nr.update({"idp": dbv3})
                registro = dbcon.srit.personas.insert_one(nr)
            # print("NR:", registro)
            return {"message": "persona registrada"}
        else:

            return {"error": "correo ya registrado"}
    else:
        respuesta = {"Auth": "No autorizado"}
        return respuesta, 401


@rpersonas.put("/rpersonas/{id}")
def modificar_persona(id: str, persona: Dpersonas, curren_token: Token = Depends(get_current_token)):
    has_access = Security.verify_token_r(curren_token)
    if has_access:
        fp = dict(persona)

        dbcommit = dbcon.srit.personas.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": fp})

        if dbcommit == None:
            return {"mensaje": "Id no encontrado"}
        else:
            return {"mensaje": "Usuario modificado"}
    else:

        return {"Mensaje": "No autorizado"}, 401


@rpersonas.delete("/rpersonas/{id}")
def eliminar_personas(id: str, curren_token: Token = Depends(get_current_token)):
    has_access = Security.verify_token_r(curren_token)
    if has_access:
        # validacion si tiene vehiculos registrados

        dbv = dbcon.srit.personas.find_one({"_id": ObjectId(id)})
        if dbv != None:

            gdata = personaEntity(dbv)

            dbvalidacion = dbcon.srit.vehiculos.find_one({"idp": gdata["idp"]})

            if dbvalidacion == None:
                dbcommint = dbcon.srit.personas.find_one_and_delete(
                    {"_id": ObjectId(id)})

                if dbcommint == None:
                    return {"mensaje": "Id no encontrado"}

                else:
                    return {"mensaje": "Persona eliminado"}
            else:

                return {"mensaje": "Persona posee vehiculos registrados"}

    else:

        return {"Mensaje": "No autorizado"}, 401
