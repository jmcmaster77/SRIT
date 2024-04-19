from .models.User import User
from utils.db import dbcon
from schemas.users import userEntity, usersEntity
from passlib.hash import sha256_crypt

class AuthService():

    @classmethod
    def login_user(cls, user):
        try:

            authenticated_user = None

            rconsult = userEntity(
                dbcon.pruebas.users.find_one({'id': int(user.id)}))

            if user.username == rconsult["username"] and sha256_crypt.verify(user.password, rconsult["password"]):
                authenticated_user = User(
                    rconsult["id"], rconsult["username"], None, rconsult["fullname"])
            return authenticated_user

        except Exception as ex:
            raise Exception(ex)
