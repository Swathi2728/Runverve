from .metrics_schema import Metrics
from uuid import UUID
from .metrics_model import MatricDAO


class MetricService:
    def add_metrics(user_id:UUID,metric:Metrics):
        return MatricDAO.add_metrics(user_id,metric)
    def get_metrics(user_id:UUID,device_id:UUID):
        return MatricDAO.get_metrics(user_id,device_id)