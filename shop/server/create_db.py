from Fastapi.database.database import init
import os
from Fastapi.env.env import dbpath

if os.path.exists(dbpath):
    os.remove(dbpath)

init()