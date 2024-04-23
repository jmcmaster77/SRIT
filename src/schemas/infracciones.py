def infraccionEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "secuencial": item["secuencial"],
        "placa": item["placa"],
        "multa": item["multa"],
        "idof": item["idof"],
        "comentario": item["comentario"],
        "registrado": item["registrado"],
        "pagado": item["pagado"]
    }


def infracionesEntity(entity) -> list:
    return [infraccionEntity(item) for item in entity]


def infraccionxeEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "fullname": item["fullname"],
        "email": item["email"],
        "idp": item["idp"],
        "placa": item["placa"],
        "marca": item["marca"],
        "multa": item["multa"],
        "comentario": item["comentario"],
        "pagado": item["pagado"]
    }


def infraccionxesEntity(entity) -> list:
    return [infraccionxeEntity(item) for item in entity]
