from sqlmodel import create_engine
from Fastapi.env.env import database_path


engine = create_engine(database_path,echo=True)     
