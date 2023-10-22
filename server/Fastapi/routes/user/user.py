from fastapi import APIRouter


user = APIRouter()


@user.get("/user")
async def home():
    return({"msg" : "user"})