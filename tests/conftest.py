import pytest

from db import Session


@pytest.fixture
def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
        