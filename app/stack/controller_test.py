from unittest.mock import patch
from flask.testing import FlaskClient
from werkzeug.exceptions import BadRequest

from app.test.fixtures import client, app
from .service import StackService
from .schema import StackSchema
from .model import Stack
from . import BASE_ROUTE


def make_stack(stack_id: int = 1) -> Stack:
    return Stack(id=stack_id)


class TestStacksResource:
    @patch.object(
        StackService,
        "get_all",
        lambda: [
            make_stack(stack_id=1),
            make_stack(stack_id=2),
        ],
    )
    def test_get(self, client: FlaskClient):
        """Test get endpoint"""
        with client:
            results = client.get(
                f"/api/{BASE_ROUTE}/", follow_redirects=True
            ).get_json()
            expected = StackSchema(many=True).dump(
                [
                    make_stack(stack_id=1),
                    make_stack(stack_id=2),
                ]
            )
            for r in results:
                assert r in expected

    @patch.object(
        StackService,
        "create",
        lambda: Stack(id=1)
    )
    def test_post(self, client: FlaskClient):
        """Test post endpoint"""
        with client:
            result = client.post(f"/api/{BASE_ROUTE}/").get_json()
            expected = StackSchema().dump(Stack(id=1))
            assert result == expected


class TestStackResource:
    @patch.object(StackService, "delete_by_id", lambda stack_id: None)
    def test_delete_works(self, client: FlaskClient):
        """Test delete endpoint works"""
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/1")
            assert result.status_code == 204

    @patch.object(StackService, "delete_by_id", side_effect=BadRequest("An exception"))
    def test_delete_fails(self, mocked_function, client: FlaskClient):
        """Test delete endpoint fails"""
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/1")
            assert result.status_code == 400
            assert result.get_json()["message"] == "An exception"

    @patch.object(
        StackService,
        "get_by_id",
        lambda stack_id: make_stack(stack_id=stack_id)
    )
    def test_get_works(self, client: FlaskClient):
        """Test get endpoint works"""
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/1", follow_redirects=True).get_json()
            expected = StackSchema().dump(make_stack(stack_id=1))
            assert expected == result

    @patch.object(
        StackService,
        "get_by_id",
        side_effect=BadRequest("An exception")
    )
    def test_get_fails(self, mocked_function, client: FlaskClient):
        """Test get endpoint fails"""
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/1", follow_redirects=True)
            assert result.status_code == 400

    @patch.object(
        StackService,
        "add_operand_to_stack",
        lambda stack_id, value: make_stack(stack_id=stack_id)
    )
    def test_post_works(self, client: FlaskClient):
        """Test post endpoint works"""
        with client:
            result = client.post(f"/api/{BASE_ROUTE}/1", json={"value": 1}).get_json()
            assert result["id"] == 1

    @patch.object(
        StackService,
        "add_operand_to_stack",
        side_effect=BadRequest("An exception")
    )
    def test_post_fails(self, mocked_function, client: FlaskClient):
        """Test post endpoint fails"""
        with client:
            result = client.post(f"/api/{BASE_ROUTE}/1", follow_redirects=True)
            assert result.status_code == 400
