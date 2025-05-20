from .product_schema import DeviceRegister
from uuid import UUID
from .product_model import DeviceDAO


class DeviceService:
    def device_register(user_id:UUID,device:DeviceRegister):
        return DeviceDAO.device_register(user_id,device)
        
        