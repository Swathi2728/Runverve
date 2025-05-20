from pydantic import BaseModel

class DeviceRegister(BaseModel):
    device_uuid:str
    