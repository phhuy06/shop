from fastapi import APIRouter
from Fastapi.database.CRUD import create_user, read_user, update_user, delete_user
from Fastapi.database.database import User

admin = APIRouter()


@admin.get("/admin/read_user")
async def readUser(id : int):
    return read_user(id=id) #return list

@admin.post("/admin/create_user")
async def createUser(user : User):
    return create_user(user=user)

@admin.delete("/admin/delete_user")
async def deleteUser(id : int):
    return delete_user(id=id)

@admin.put("/admin/update_user")
async def updateUser(id : int, user: User):
    return update_user(id=id, user=user)