from models.warehouse_model import WarehouseModel
from sqlalchemy import select
from sqlalchemy.orm import Session


class WarehouseDao:
    def __init__(self, session: Session):
        self.__session = session
        self.__warehouse = WarehouseModel

    def get_all(self):
        statement = select(self.__warehouse)
        result = self.__session.execute(statement).all()
        return result

    def get_all_by_zone(self, zone):
        statement = select(self.__warehouse).filter_by(self.__warehouse.zone == zone)
        result = self.__session.execute(statement).all()
        return result

    def get_all_by_smaller_price(self, price):
        statement = select(self.__warehouse).filter_by(self.__warehouse.price <= price)
        result = self.__session.execute(statement).all()
        return result

    def get_all_have(self):
        statement = select(self.__warehouse).filter_by(self.__warehouse.quantity > 0)
        result = self.__session.execute(statement).all()
        return result

    def create_new_warehouse(self, warehouse: WarehouseModel):
        self.__session.add(warehouse)
        self.__session.commit()
        print(f"Insert Data: id = {warehouse.id}, price = {warehouse.price}, quantity = {warehouse.quantity}, "
              f"zone = {warehouse.zone} Complete!")
