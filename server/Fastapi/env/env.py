import os
from dotenv import load_dotenv

load_dotenv()

database_path = os.getenv("database_path")
dbpath = os.getenv('dbpath')
SECRET_KEY = os.getenv("SECRET_KEY")
SECURITY_ALGORITHM = os.getenv("SECURITY_ALGORITHM")