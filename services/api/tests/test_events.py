from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_event():
    r = client.post("/events/", json={"type": "test", "payload": {"a":1}})
    assert r.status_code == 200
