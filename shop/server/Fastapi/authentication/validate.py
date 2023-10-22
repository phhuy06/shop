from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer
from pydantic import ValidationError
import jwt
from datetime import datetime
from Fastapi.env.env import SECRET_KEY, SECURITY_ALGORITHM


token_receive = HTTPBearer(scheme_name="AUTH")

def validate_token(header = Depends(token_receive)):
    try:
        payload = jwt.decode(header, SECRET_KEY, SECURITY_ALGORITHM)
        if datetime.utcfromtimestamp(payload.get('exp')) < datetime.utcnow():
            raise HTTPException(status_code=403, detail="Token expired")
    except (jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=403,
            detail="Could not validate credentials",
        )