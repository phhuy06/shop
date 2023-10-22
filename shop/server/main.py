from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from Fastapi.routes.admin.admin import admin
from Fastapi.routes.auth.auth import auth
from Fastapi.routes.user.user import user


origins = ["*"]


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(admin, tags=["admin"])
app.include_router(auth, tags=["auth"])
app.include_router(user, tags=["user"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)