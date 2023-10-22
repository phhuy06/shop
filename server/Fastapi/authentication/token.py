from datetime import datetime, timedelta
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
SECURITY_ALGORITHM = os.getenv("SECURITY_ALGORITHM")



def generate_token() -> str:
    expire_day = 3
    expire_time = datetime.utcnow() + timedelta(days=expire_day)
    encode = {
        "exp": expire_time,
        "exp_day": expire_day,
    }
    token = jwt.encode(encode, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
    return token