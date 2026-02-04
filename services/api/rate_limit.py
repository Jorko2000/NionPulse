from fastapi import Request, HTTPException
import time

visits = {}

def rate_limit(request: Request):
    ip = request.client.host
    now = time.time()
    window = 10
    limit = 5
    if ip not in visits:
        visits[ip] = []
    visits[ip] = [t for t in visits[ip] if now - t < window]
    if len(visits[ip]) >= limit:
        raise HTTPException(429, "Too many requests")
    visits[ip].append(now)
