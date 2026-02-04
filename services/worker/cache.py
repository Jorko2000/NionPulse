import redis, json

r = redis.Redis(host="redis", port=6379, db=0)

def cache_result(key, value, ttl=60):
    r.set(key, json.dumps(value), ex=ttl)

def get_cache(key):
    v = r.get(key)
    return json.loads(v) if v else None
