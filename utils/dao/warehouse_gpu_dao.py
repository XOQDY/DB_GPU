from models.warehouse_model import WarehouseModel
from models.gpu_model import GPUModel
from sqlalchemy import select
from sqlalchemy.orm import Session


class WarehouseGPUDao:
    def __init__(self, session: Session):
        self.__session = session
        self.__gpu = GPUModel
        self.__warehouse = WarehouseModel

    def get_all_gpu_by_zone(self, zone):
        statement = select(self.__gpu, self.__warehouse).join(self.__warehouse, self.__gpu.id == self.__warehouse.id)
        result = self.__session.execute(statement).all()
        return result

    def get_name_zone_by_zone(self, zone):
        statement = select(self.__gpu.name, self.__warehouse.zone).join(self.__warehouse, self.__gpu.id ==
                                                                        self.__warehouse.id)
        result = self.__session.execute(statement).all()
        return result
