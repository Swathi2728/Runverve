from typing import List, Optional
from datetime import datetime, timedelta

from fastapi import HTTPException
from .product_schema import DeviceRegister
from uuid import UUID,uuid4
from sqlmodel import Field,SQLModel,select
from utils.database import Session,engine


class Device(SQLModel, table=True):
    id: UUID= Field(default_factory=uuid4, primary_key=True)
    device_uuid: str = Field(unique=True, index=True)
    user_id: UUID = Field(foreign_key="user.id")
    
    
class DeviceDAO:
    
    def device_register(user_id: UUID, device: DeviceRegister):
        with Session(engine) as session:
            existing = session.exec(select(Device).where(Device.device_uuid == device.device_uuid)).first()
            if existing:
                raise HTTPException(status_code=400, detail="Device already registered")

            new_device = Device(user_id=user_id, device_uuid=device.device_uuid)
            session.add(new_device)
            session.commit()
            session.refresh(new_device)
            return new_device
        
    