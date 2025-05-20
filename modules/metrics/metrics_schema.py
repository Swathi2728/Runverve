from pydantic import BaseModel
from uuid import UUID

class Metrics(BaseModel):
    device_uuid:UUID
    hydration:float
    fatigue:str
    posture:str
