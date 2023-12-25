#def userEntity(item) -> dict:
#    return {
#        "id":str(item["_id"]),
#        "name":item["name"],
#        "email":item["email"],
#        "phone":item["phone"]
#    }

#def usersEntity(entity) -> list:
#    return [userEntity(item) for item in entity]


def userEntity(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def usersEntity(entity) -> list:
    return [userEntity(a) for a in entity]