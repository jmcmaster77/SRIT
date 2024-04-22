def vehiculoEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "idp": item["idp"],
        "placa": item["placa"],
        "marca": item["marca"],
        "color": item["color"],
        "registrado": item["registrado"]
    }


def vehiculosEntity(entity) -> list:
    return [vehiculoEntity(item) for item in entity]