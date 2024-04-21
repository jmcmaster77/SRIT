from fastapi import FastAPI, APIRouter, Depends, Security as Secu
from services.models.User import User
from services.AuthService import AuthService
from utils.Security import Security
from fastapi.security.api_key import APIKeyHeader
from passlib.hash import sha256_crypt
from pydantic import BaseModel
auth = APIRouter()


@auth.get("/")
def test():
    return {"status": "Dev"}


class Userget(BaseModel):
    id: int
    username: str
    password: str


@auth.post("/")
def user_data_for_token(user: Userget):
    # print("ps: ", sha256_crypt.encrypt(user.password))

    _user = User(user.id, user.username, user.password, None)

    authenticated_user = AuthService.login_user(_user)

    if (authenticated_user != None):
        encode_token = Security.generate_token(authenticated_user)
        return {'success': True, 'token': encode_token}
    else:
        return {"success": False}


token_key = APIKeyHeader(name="Authorization")


class Token(BaseModel):
    token: str


def get_current_token(auth_key: str = Secu(token_key)):

    return auth_key


@auth.post("/verify/token")
def verify_token(curren_token: Token = Depends(get_current_token)):
    has_access = Security.verify_token_r(str(curren_token).split(' ')[1])
    print("Current: ", curren_token)
    print("Has_access: ", has_access)
    if has_access:

        return {'success': True}

    else:

        return {"Auth": "No autorizado"}, 401
