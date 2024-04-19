def personaEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "fullname": item["fullname"],
        "email": item["email"],
        "registrado": item["registrado"]
    }


def personasEntity(entity) -> list:
    return [personaEntity(item) for item in entity]