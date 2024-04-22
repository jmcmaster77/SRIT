from fastapi import FastAPI, APIRouter, Depends, Security as Secu
from services.models.User import User
from schemas.users import userEntity, usersEntity
from services.AuthService import AuthService
from utils.Security import Security
from fastapi.security.api_key import APIKeyHeader
from passlib.hash import sha256_crypt
from pydantic import BaseModel
from utils.db import dbcon
auth = APIRouter()


@auth.get("/")
def test_server():
    return {"status": "Server Up"}


class Userget(BaseModel):
    id: int
    username: str
    password: str


@auth.post("/get_token")
def generacion_token_for_user(user: Userget):
    # print("ps: ", sha256_crypt.encrypt(user.password))

    _user = User(user.id, user.username, user.password, None)

    authenticated_user = AuthService.login_user(_user)

    if (authenticated_user != None):
        encode_token = Security.generate_token(authenticated_user)
        return {'success': True, 'token': encode_token}
    else:
        return {"success": False}


class Token(BaseModel):
    token: str


token_key = APIKeyHeader(name="Authorization")


def get_current_token(auth_key: str = Secu(token_key)):
    return auth_key


class Duser(BaseModel):
    id: int
    username: str
    fullname: str
    password: str
    password2: str


class Duser_m(BaseModel):
    username: str
    fullname: str
    password: str
    password2: str


@auth.post("/create_user")
def creacion_usuario(user_data: Duser, curren_token: Token = Depends(get_current_token)):
    has_access = Security.verify_token_r(str(curren_token).split(' ')[1])
    if has_access:

        if user_data.password == user_data.password2:
            rc = dbcon.srit.users.find_one({'id': int(user_data.id)})

            if rc == None:
                datos_user_formated = dict(user_data)
                del datos_user_formated["password2"]
                datos_user_formated["password"] = sha256_crypt.encrypt(
                    datos_user_formated["password"])
                dbcon.srit.users.insert_one(datos_user_formated)
                return {"mensaje", "usuario registrado"}
            else:
                return {"mensaje", "Usuario ya existe"}, 401
        else:
            return {"mensaje", "password no coinciden"}, 401
    else:
        return {"Auth": "No autorizado"}, 401


@auth.get("/users")
def consulta_usuarios(curren_token: Token = Depends(get_current_token)):
    has_access = Security.verify_token_r(str(curren_token).split(' ')[1])
    if has_access:

        consulta = (usersEntity(dbcon.srit.users.find()))
        return consulta
    else:
        return {"Auth": "No autorizado"}, 401


@auth.get("/users/{id}")
def consulta_usuario_por_id(id: int, curren_token: Token = Depends(get_current_token)):
    has_access = Security.verify_token_r(str(curren_token).split(' ')[1])
    if has_access:
        consulta = dbcon.srit.users.find_one({"id": id})
        if consulta != None:
            return userEntity(consulta)
        else:
            return {"mensaje": "Usuario no registrado"}, 401


@auth.put("/users/{id}")
def modificar_usuario(id: int, user: Duser_m, curren_token: Token = Depends(get_current_token)):
    has_access = Security.verify_token_r(str(curren_token).split(' ')[1])
    if has_access:

        if user.password == user.password2:
            dataUdict = dict(user)
            del dataUdict["password2"]
            dataUdict["password"] = sha256_crypt.encrypt(dataUdict["password"])
            try:
                dbcommit = dbcon.srit.users.find_one_and_update(
                    {"id": id}, {"$set": dataUdict})
                if dbcommit == None:
                    return {"mensaje": "Id no encontrado"}
                else:
                    return {"mensaje": "Usuario modificado"}
            except Exception as ex:

                return {"mensaje": Exception(ex)}

        else:
            return {"mensaje": "password no coinciden"}
    else:
        return {"Mensajes": "No autorizado"}


@auth.delete("/users/{id}")
def eliminar_usuario(id: int, curren_token: Token = Depends(get_current_token)):
    has_access = Security.verify_token_r(str(curren_token).split(' ')[1])
    if has_access:

        dbcommint = dbcon.srit.users.find_one_and_delete({"id": id})
        if dbcommint == None:
            return {"mensaje": "Id no encontrado"}
        else:
            return {"mensaje": "Usuario eliminado"}
    else:

        return {"Mensajes": "No autorizado"}


@auth.post("/verify/token")
def verify_token(curren_token: Token = Depends(get_current_token)):
    has_access = Security.verify_token_r(str(curren_token).split(' ')[1])
    if has_access:

        return {"Mensajes": "Token Valido"}

    else:

        return {"Auth": "No autorizado"}, 401
