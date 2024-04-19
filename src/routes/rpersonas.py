from fastapi import FastAPI, APIRouter, Request, Header
from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import uuid4 as uuid
from utils.db import dbcon
from utils.Security import Security

rpersonas = APIRouter()


class Dpersonas(BaseModel):
    _id: str
    fullname: str
    email: EmailStr
    registrado: datetime = datetime.now()


@rpersonas.post("/rpersonas")
def registro_personas(datos: Dpersonas, Authorization: str = Header()):
    nr = dict(datos)
    v = Security.virify_token_r(Authorization.split(" ")[1])
    
    if v:
        con = dbcon.srit.personas.find_one({'email': nr["email"]})

        if con == None:
            registro = dbcon.srit.personas.insert_one(nr)
            #print("NR:", registro)
            return {"message": "correo registrado"}
        else:
            
            return {"error": "correo ya registrado"}
    else:
        respuesta = {"Auth": "No autorizado"}
        return respuesta, 401
