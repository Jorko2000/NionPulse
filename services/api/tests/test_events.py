from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_event():
    r = client.post("/events/", json={"type": "test", "payload": {"a":1}})
    assert r.status_code == 200

test_cache.py

from services.api.services.cache import cache_result, get_cache

def test_cache():
    cache_result("key1", {"val": 123}, ttl=1)
    val = get_cache("key1")
    assert val == {"val": 123}
