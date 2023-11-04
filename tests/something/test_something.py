import tables


def test_get_data_flights(get_db_session):
    data = get_db_session.query(tables.Flights).first()
    
    print()
    print(data.flight_id)
    print(data.flight_no)
    print(data.status)
    
    
def test_try_to_delete_something():
    pass

