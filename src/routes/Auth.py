from flask import Blueprint, request, jsonify

from services.models.User import User
from services.AuthService import AuthService
from utils.Security import Security 
from passlib.hash import sha256_crypt
auth = Blueprint("auth", __name__)

# hast = sha256_crypt.hash("srit20240419*.")

@auth.route("/")
def test():
    return ("Aqui vamos con blue")


@auth.route("/", methods=["POST"])
def get_user_data():
    id = request.json["id"]
    username = request.json["username"]
    password = request.json["password"]
    # para aplicar el hash con passlib 
    # print("ps: ", sha256_crypt.encrypt(password)) 

    _user = User(id, username, password, None)

    authenticated_user = AuthService.login_user(_user)

    if (authenticated_user != None):
        encode_token = Security.generate_token(authenticated_user)
        return jsonify({'success': True, 'token': encode_token})
    else:
        return jsonify({"success": False})
