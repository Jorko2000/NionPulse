from fastapi import Request, HTTPException
import jwt

def verify_jwt(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(401, "Missing token")
    try:
        payload = jwt.decode(token.split()[1], options={"verify_signature": False})
        return payload
    except Exception:
        raise HTTPException(401, "Invalid token")
