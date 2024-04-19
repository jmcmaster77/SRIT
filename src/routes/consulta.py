from flask import Blueprint, request, jsonify
from schemas.personas import personaEntity, personasEntity
from utils.db import dbcon
from utils.Security import Security

consulta = Blueprint("consulta", __name__)


@consulta.route("/consulta")
def get_consulta():
    has_access = Security.verivy_token(request.headers)
    if has_access:
        try:
            consulta = (personasEntity(dbcon.pruebas.personas.find()))
            return consulta
        except Exception as error:
            print(error)
            return jsonify({"message": "ERROR", "success": False})
    else:
        respuesta = jsonify({"Auth": "No autorizado"})
        return respuesta, 401
