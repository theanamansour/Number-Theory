from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.services.auth import get_user_by_token

security = HTTPBearer(auto_error=False)


def get_current_user_optional(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)
):
    if credentials is None:
        return None

    if credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid authentication scheme.")

    token = credentials.credentials
    user = get_user_by_token(token)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token.")

    return user


def get_current_user_required(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)
):
    user = get_current_user_optional(credentials)

    if not user:
        raise HTTPException(status_code=401, detail="Authentication required.")

    return user