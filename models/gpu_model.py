from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class GPUModel(Base):
    __tablename__ = "gpu"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    asic = Column(Text)
    vendor = Column(Text, nullable=False)
    device = Column(Text, nullable=False)
    apu = Column(Integer, nullable=False)
    mobile_part = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<GPU Information: id {self.id}, name = {self.name}, asic/codename = {self.asic}, vendor id = {self.vendor}, " \
               f"device id = {self.device}, integrated/apu = {self.apu}, discrete mobile part = {self.mobile_part}>"
