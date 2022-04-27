from models.gpu_model import GPUModel
from sqlalchemy import select
from sqlalchemy.orm import Session


class GPUDao:
    def __init__(self, session: Session):
        self.__session = session
        self.__gpu = GPUModel

    def get_all(self):
        statement = select(self.__gpu)
        result = self.__session.execute(statement).all()
        return result

    def get_all_only_name(self):
        statement = select(self.__gpu.name)
        result = self.__session.execute(statement).all()
        return result

    def get_all_name_vendor_device(self):
        statement = select(self.__gpu.name, self.__gpu.vendor, self.__gpu.device)
        result = self.__session.execute(statement).all()
        return result

    def get_all_by_id(self, id):
        statement = select(self.__gpu).filter_by(id=id)
        result = self.__session.execute(statement).all()
        return result

    def get_name_mobile_part_by_mobile_part(self, mobile_part):
        statement = select(self.__gpu.name, self.__gpu.mobile_part).filter_by(mobile_part=mobile_part)
        result = self.__session.execute(statement).all()
        return result
