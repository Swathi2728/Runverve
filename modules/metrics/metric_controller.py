from fastapi import APIRouter,Request

from utils.auth import authenticate
from .metrics_schema import Metrics
from .metric_service import MetricService
from uuid import UUID,uuid4

metric_router=APIRouter(prefix="/Metrics",tags=["Metrics"])


@metric_router.post("add/metrics")
def add_metrics(req:Request,metric:Metrics):
    user_id=authenticate(req)
    return MetricService.add_metrics(user_id,metric)
@metric_router.get("/get/usermetrics/{device_id}")

def get_metrics(req:Request,device_id:UUID):
    user_id=authenticate(req)
    return MetricService.get_metrics(user_id,device_id)
    


    