def personaEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "rid": item["rid"],
        "name": item["name"],
        "ci": item["ci"]
    }


def personasEntity(entity) -> list:
    return [personaEntity(item) for item in entity]