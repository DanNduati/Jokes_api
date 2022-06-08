import os

import pytest
from starlette.testclient import TestClient

from app.config import Settings, get_settings
from app.main import create_application


# https://fastapi.tiangolo.com/advanced/testing-dependencies/
def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


# Define a test_app fixture
@pytest.fixture(scope="module")
def test_app():
    # set up
    # Overide the get_settings() dependency using the app.dependency_overrides attribute
    # To override a dependency for testing, you put as a key the original dependency (a function), and as the value, your dependency override (another function).
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    # Starlette's TestClient allows you to make requests against your ASGI application, using the requests library.
    with TestClient(app) as test_client:
        # testing
        yield test_client
    # tear down
