from datetime import datetime, timedelta, timezone
from authlib.jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from authlib.jose.errors import JoseError
 

# constants

SECRET_KEY='my_secret'
AGALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=30

# functions
def create_access_token(data:dict):
    header={"alg":AGALGORITHM}
    expire=datetime.now(timezone.utc)+timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    payload=data.copy()
    payload.update({"exp":expire})
    return jwt.encode(header,payload,SECRET_KEY).decode('utf-8')

def verify_token(token:str):
    try:
        claims=jwt.decode(token,SECRET_KEY)
         
        username=claims.get('sub')
        if username is None:
            raise HTTPException(status_code=401,detail='could not validate credentials')
        return {'username':username} 
    except JoseError:
        raise HTTPException(status_code=401,detail='could not validate credentials')