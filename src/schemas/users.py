def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "id": item["id"],
        "username": item["username"],
        "password": item["password"],
        "fullname": item["fullname"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
