def oficialEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "id": item["id"],
        "fullname": item["fullname"],
        "registrado": item["registrado"]
    }


def oficialesEntity(entity) -> list:
    return [oficialEntity(item) for item in entity]