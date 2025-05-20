from fastapi import APIRouter,Request
from fastapi import  FastAPI,HTTPException


from utils.auth import authenticate
from .product_schema import DeviceRegister
from .product_service import DeviceService

device_router=APIRouter(prefix="/Devices",tags=["Devices"])
@device_router.post("/device/register")
def device_register(req:Request,device:DeviceRegister):
    user_id=authenticate(req)
    return DeviceService.device_register(user_id,device)
    