def infraccionEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "secuencial": item["secuencial"],
        "placa": item["placa"],
        "multa": item["multa"],
        "idof": item["idof"],
        "comentario": item["comentario"],
        "registrado": item["registrado"],
        "pagada": item["pagada"]
    }


def infracionesEntity(entity) -> list:
    return [infraccionEntity(item) for item in entity]