from sqlalchemy import Boolean, Column, Integer, String

from db import Model


class Flights(Model):
    __tablename__ = 'flights'
    
    flight_id = Column(Integer, primary_key=True)
    status = Column(String)
    flight_no = Column(String, index=True)
    departure_airport = Column(String)
    