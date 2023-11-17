from sqlalchemy import String, Integer, Column, DateTime
from database import Base


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String)
    model = Column(String)
    wearness = Column(String) # степень износа
    reg_date = Column(DateTime)
    photo_of_car = Column(String)
    trader_number = Column(Integer)
    type = Column(String)
    cost = Column(String)






