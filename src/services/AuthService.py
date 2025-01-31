from .models.User import User
from utils.db import dbcon
from schemas.users import userEntity
from schemas.oficiales import oficialEntity
from passlib.hash import sha256_crypt


class AuthService():

    @classmethod
    def login_user(cls, user):
        try:

            authenticated_user = None

            rconsult = userEntity(dbcon.srit.users.find_one({'id': int(user.id)}))

            if user.username == rconsult["username"] and sha256_crypt.verify(user.password, rconsult["password"]):
                authenticated_user = User(
                    rconsult["id"], rconsult["username"], None, rconsult["fullname"])
            return authenticated_user

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def login_oficial(cls, user):
        try:

            authenticated_user = None

            rconsult = oficialEntity(
                dbcon.srit.oficiales.find_one({'id': int(user.id)}))

            if user.username == rconsult["username"] and sha256_crypt.verify(user.password, rconsult["password"]):
                authenticated_user = User(
                    rconsult["id"], rconsult["username"], None, rconsult["fullname"])
            return authenticated_user

        except Exception as ex:
            raise Exception(ex)
