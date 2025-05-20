from pydantic_settings import BaseSettings
import jwt
from fastapi import Request,HTTPException
from sqlmodel import select
from utils.database import Session,engine
from modules .users.user_model import User

Algorithm='HS256'
class Secret_key(BaseSettings):
    secret_key:str
    class Config:
        env_file = ".env"
secret_key=Secret_key()
def jwt_token_encrypt(new_user):
    payload={
        "sub": str(new_user.id),
        "name":new_user.name,
        "email":new_user.email,
        
    }
    token = jwt.encode(payload, secret_key.secret_key, algorithm=Algorithm)
    return token
def jwt_token_decrypt(jwt_token):
   try:
        payload = jwt.decode(jwt_token, secret_key.secret_key, algorithms=Algorithm)
        return payload
 
   except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

from fastapi import Request, HTTPException

def authenticate(request: Request):
    from modules.users.user_model import User, engine, Session  # Avoid circular import
    
    bearer_token = request.headers.get("Authorization")
    
    if not bearer_token or not bearer_token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid or missing Authorization header")

    try:
        jwt_token = bearer_token.split(" ")[1]
    except IndexError:
        raise HTTPException(status_code=401, detail="Malformed Authorization header")

    payload = jwt_token_decrypt(jwt_token)
    email = payload.get("email")

    with Session(engine) as session:
        user = session.exec(select(User).where(User.email == email)).first()
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return user.id

    
