from flask import Blueprint, request, jsonify

from utils.Security import Security

consulta = Blueprint("consulta", __name__)


@consulta.route("/consulta")
def get_consulta():
    has_access = Security.verivy_token(request.headers)
    if has_access:
        try:
            consulta = [{"id": 1, "item": "Uno"}, {"id": 2, "item": "Dos"}, {
                "id": 3, "item": "Tres"}, {"id": 4, "item": "Cuatro"}]
            return consulta
        except Exception as error:
            print(error)
            return jsonify({"message": "ERROR", "success": False})
    else:
        respuesta = jsonify({"Auth": "No autorizado"})
        return respuesta, 401
