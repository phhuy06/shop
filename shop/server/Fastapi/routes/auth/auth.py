from fastapi import APIRouter


auth = APIRouter()


@auth.get("/auth")
async def home():
    return({"msg" : "auth"})