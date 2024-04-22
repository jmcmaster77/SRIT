from fastapi import APIRouter, Depends, Security as Secu
from pydantic import BaseModel
from datetime import datetime
# from uuid import uuid4 as uuid
from utils.db import dbcon
from utils.Security import Security
from schemas.vehiculos import vehiculoEntity, vehiculosEntity
from bson import ObjectId
from fastapi.security.api_key import APIKeyHeader

rinfraccion = APIRouter()


token_key = APIKeyHeader(name="Authorization")


class Dinfraccion(BaseModel):
    id: str
    fullname: str
    registrado: datetime = datetime.now()


class Token(BaseModel):
    token: str


def get_current_token(auth_key: str = Secu(token_key)):
    return auth_key


@rinfraccion.put("/rinfraccion")
def registro_de_ingracciones(datos: Dinfraccion, curren_token: Token = Depends(get_current_token)):
    acceso = Security.verify_token_r(str(curren_token).split(" ")[1])
    if acceso:
        todo = "go"
    else:
        todo = "more todo"
    return