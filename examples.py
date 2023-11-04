from sqlalchemy.sql.expression import desc

import tables
from db import session


# result = session.query(tables.Flights.flight_id, tables.Flights.flight_no).first()
# result = session.query(tables.Flights.flight_id, tables.Flights.flight_no).all()
# result = session.query(tables.Flights.flight_id, tables.Flights.flight_no).filter(tables.Flights.flight_id==180).one_or_none()
# result = session.query(
#     tables.Flights.flight_id, tables.Flights.flight_no
# ).filter(tables.Flights.flight_id > 100,
#              tables.Flights.flight_id < 150
# ).all()

# Подзапрос subquery() выведет в консоль SQL запрос, который сгенерировал sqlalchemy
# flights_ids = session.query(tables.Flights.flight_id).filter(tables.Flights.flight_id > 180).subquery()
# result = session.query(tables.Flights.departure_airport).filter(tables.Flights.flight_id.in_(flights_ids)).all()

# flights_ids = session.query(tables.Flights.flight_id, tables.Flights.flight_no).order_by(tables.Flights.flight_id).all()
# flights_ids = session.query(tables.Flights.flight_id, tables.Flights.flight_no).order_by(desc(tables.Flights.flight_id)).all()
# flights_ids = session.query(tables.Flights.flight_id, tables.Flights.flight_no).order_by(desc(tables.Flights.flight_id)).limit(1).all()

flights_ids = session.query(tables.Flights.flight_id, tables.Flights.flight_no).order_by(desc(tables.Flights.flight_id)).limit(2).offset(3).all()

# if flights_ids:
#     print("All good")
# else:
#     print("Not good")

print(flights_ids)