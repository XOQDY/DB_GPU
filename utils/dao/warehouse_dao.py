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
        statement = select(self.__warehouse).filter_by(zone=zone)
        result = self.__session.execute(statement).all()
        return result

    def get_all_by_smaller_price(self, price):
        statement = select(self.__warehouse).filter(self.__warehouse.price <= price)
        result = self.__session.execute(statement).all()
        return result

    def get_all_have(self):
        statement = select(self.__warehouse).filter(self.__warehouse.quantity > 0)
        result = self.__session.execute(statement).all()
        return result

    def add_new_stock_warehouse(self, product_id, quantity):
        self.__session.query(self.__warehouse).filter(self.__warehouse.id == product_id)\
            .update({self.__warehouse.quantity: self.__warehouse.quantity + quantity})
        self.__session.commit()

        statement = self.__session.query(self.__warehouse).filter(self.__warehouse.id == product_id).first()
        print(f"Now Product_id: {statement.id} have {statement.quantity} pcs. in stock")
