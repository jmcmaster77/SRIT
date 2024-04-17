from flask import Blueprint, request, jsonify

from services.models.User import User
from services.AuthService import AuthService
from utils.Security import Security 

auth = Blueprint("auth", __name__)


@auth.route("/")
def test():
    return ("Aqui vamos con blue")


@auth.route("/", methods=["POST"])
def get_user_data():
    username = request.json["username"]
    password = request.json["password"]

    _user = User(0, username, password, None)

    authenticated_user = AuthService.login_user(_user)

    if (authenticated_user != None):
        encode_token = Security.generate_token(authenticated_user)
        return jsonify({'success': True, 'token': encode_token})
    else:
        return jsonify({"success": False})
