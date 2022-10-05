from unittest.mock import patch
from flask.testing import FlaskClient
from werkzeug.exceptions import BadRequest

from app.test.fixtures import client, app
from .service import OperatorService
from .schema import OperatorSchema
from .model import Operator
from . import BASE_ROUTE


def make_operator(operator_id: int = 1) -> Operator:
    return Operator(id=operator_id, name=f"Operator {operator_id}")


class TestOperatorsResource:
    @patch.object(
        OperatorService,
        "get_all",
        lambda: [
            make_operator(operator_id=1),
            make_operator(operator_id=2),
        ],
    )
    def test_get(self, client: FlaskClient):
        """Test get endpoint"""
        with client:
            results = client.get(
                f"/api/{BASE_ROUTE}/", follow_redirects=True
            ).get_json()
            expected = OperatorSchema(many=True).dump(
                [
                    make_operator(operator_id=1),
                    make_operator(operator_id=2),
                ]
            )
            for r in results:
                assert r in expected


class TestOperatorResource:
    @patch.object(
        OperatorService,
        "apply_operator_to_stack",
        lambda stack_id, operator_id: 1
    )
    def test_post_works(self, client: FlaskClient):
        """Test post endpoint works"""
        with client:
            result = client.post(f"/api/{BASE_ROUTE}/1/stack/1", json={"value": 1}).get_json()
            assert result == 1

    @patch.object(
        OperatorService,
        "apply_operator_to_stack",
        side_effect=BadRequest("An exception")
    )
    def test_post_fails(self, mocked_function, client: FlaskClient):
        """Test post endpoint fails"""
        with client:
            result = client.post(f"/api/{BASE_ROUTE}/1/stack/1", follow_redirects=True)
            assert result.status_code == 400
            assert result.get_json()["message"] == "An exception"
