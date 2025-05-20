from fastapi import APIRouter,Request
from fastapi import  FastAPI,HTTPException


from utils.auth import authenticate

from .user_schema import UserCreate,UserLogin
from .user_service import UserService



user_router=APIRouter(prefix="/users",tags=["Users"])

@user_router.post("/auth/register")
def register_users(user:UserCreate):
    return UserService.create_user(user)

@user_router.post("/auth/login")
def login_user(user_login:UserLogin):
    user= UserService.authernticate_user(user_login)
    access_token = user.get("access_token")
    if not access_token:
        raise HTTPException(status_code=500, detail="Error generating access token")

    return {"access_token": user["access_token"], "token_type": "bearer"}
@user_router.get("/auth/profile")
def get_user_profile(req:Request):
    user_id=authenticate(req)
    return UserService.get_user_profile(user_id)



    
    


