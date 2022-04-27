from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class WarehouseModel(Base):
    __tablename__ = "warehouse"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    zone = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Warehouse product zone: id = {self.id}, price = {self.price}, quantity = {self.quantity}, " \
               f"zone = {self.zone}>"
