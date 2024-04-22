def oficialEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "idof": item["idof"],
        "fullname": item["fullname"],
        "username": item["username"],
        "password": item["password"],
        "registrado": item["registrado"]
    }


def oficialesEntity(entity) -> list:
    return [oficialEntity(item) for item in entity]