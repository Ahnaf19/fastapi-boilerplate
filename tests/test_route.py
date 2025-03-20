from fastapi.testclient import TestClient
from loguru import logger

from app.main import app


class TestRouter:
    client: TestClient

    @classmethod
    def setup_class(cls) -> None:
        """
        Setup the test client and initial data for the tests.
        """
        cls.client = TestClient(app)
    
    def test_read_data(self) -> None:
        """
        Test reading all data.
        """
        response = self.client.get("/group/")
        assert response.status_code == 200
        logger.debug(response.json())
        assert response.json() == {'message': 'ok'}
