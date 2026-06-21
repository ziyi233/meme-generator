from fastapi.testclient import TestClient

from meme_generator.app import app


def test_reload_memes_endpoint():
    client = TestClient(app)
    response = client.post("/memes/reload")

    assert response.status_code == 200
    data = response.json()
    assert data["ok"] is True
    assert isinstance(data["count"], int)
