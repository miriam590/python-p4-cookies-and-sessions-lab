import pytest
from flask.testing import FlaskClient

class CustomTestClient(FlaskClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove Werkzeug version from user agent to avoid deprecation warning
        self.environ_base.pop('HTTP_USER_AGENT', None)

@pytest.fixture
def app():
    from app import app
    app.testing = True
    app.test_client_class = CustomTestClient
    return app
