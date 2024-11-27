from ..main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_post_dishs():
    response = client.post(
        "/recipes",
        json={
            "title": "Борщ",
            "cooking_time": 40,
            "ingredients": "свекла, картофель, морковь",
            "recipe": "нарезать, варить"
        }
    )
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_dishs():
    response = client.get("/recipes", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_dish():
    response = client.get("/recipes/1", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert len(response.json()) > 0
