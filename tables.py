from sqlalchemy import Boolean, Column, Integer, String

from db import Model


class Flights(Model):
    __tablename__ = 'flights'
    
    flight_id = Column(Integer, primary_key=True)
    status = Column(String)
    flight_no = Column(String, index=True)
    departure_airport = Column(String)
    
    
class ItemType(Model):
    __tablename__ = 'item_type'
    
    item_id = Column(Integer, primary_key=True)
    item_type = Column(String)
    