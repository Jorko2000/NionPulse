from services.api.services.cache import cache_result, get_cache

def test_cache():
    cache_result("key1", {"val": 123}, ttl=1)
    val = get_cache("key1")
    assert val == {"val": 123}
