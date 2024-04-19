from fastapi import FastAPI, APIRouter, Request
from services.models.User import User
from services.AuthService import AuthService
from utils.Security import Security
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
def get_user_data(user: Userget):
    # print("ps: ", sha256_crypt.encrypt(user.password))
    print("veamos:", user)
    _user = User(user.id, user.username, user.password, None)

    authenticated_user = AuthService.login_user(_user)

    if (authenticated_user != None):
        encode_token = Security.generate_token(authenticated_user)
        return {'success': True, 'token': encode_token}
    else:
        return {"success": False}
