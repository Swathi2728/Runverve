

from sqlmodel import Field,SQLModel,select
from uuid import UUID,uuid4
from utils.database import Session,engine
from .metrics_schema import Metrics

class Metrics1(SQLModel, table=True):
    id: UUID= Field(default_factory=uuid4, primary_key=True)
    device_id:UUID=Field(foreign_key="device.id")
    user_id: UUID = Field(foreign_key="user.id")
    hydration:float
    fatigue:str
    posture:str



class MatricDAO:
    def add_metrics(user_id:UUID,metric:Metrics):
        with Session(engine) as session:
            new_metric=Metrics1(device_id=metric.device_uuid,user_id=user_id,hydration=metric.hydration,fatigue=metric.fatigue,posture=metric.posture)
            session.add(new_metric)
            session.commit()
            session.refresh(new_metric)
        return new_metric
    def get_metrics(user_id:UUID,device_id:UUID):
        with Session(engine) as session:
            metrics = session.exec(select(Metrics1).where(Metrics1.user_id == user_id, Metrics1.device_id == device_id)).all()
        return metrics

            
            
            
        