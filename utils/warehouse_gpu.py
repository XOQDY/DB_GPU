from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.dao.gpu_dao import GPUDao
from utils.dao.warehouse_dao import WarehouseDao
from utils.dao.warehouse_gpu_dao import WarehouseGPUDao


class WarehouseGPU:
    def __init__(self, connection_url="sqlite:///warehouse.db"):
        engine = create_engine(connection_url, echo=True)
        session = sessionmaker(bind=engine)
        self.__db_session = session()

    def gpu(self):
        return GPUDao(self.__db_session)

    def warehouse(self):
        return WarehouseDao(self.__db_session)

    def warehouse_gpu(self):
        return WarehouseGPUDao(self.__db_session)
