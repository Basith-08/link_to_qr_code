import pytest

from web.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Barcode" in res.data


def test_generate_qr(client):
    res = client.post("/generate", json={"text": "https://github.com", "type": "qr"})
    assert res.status_code == 200
    data = res.get_json()
    assert data["image"].startswith("data:image/png;base64,")
    assert data["filename"].endswith(".png")


def test_generate_code128(client):
    res = client.post("/generate", json={"text": "123456", "type": "code128"})
    assert res.status_code == 200
    data = res.get_json()
    assert "image" in data


def test_generate_empty_text(client):
    res = client.post("/generate", json={"text": "", "type": "qr"})
    assert res.status_code == 400
    assert "error" in res.get_json()


def test_generate_invalid_type(client):
    res = client.post("/generate", json={"text": "hello", "type": "invalid"})
    assert res.status_code == 400
