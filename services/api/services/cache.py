import redis, json
from config import settings

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

def cache_result(key, value, ttl=60):
    r.set(key, json.dumps(value), ex=ttl)

def get_cache(key):
    val = r.get(key)
    return json.loads(val) if val else None
