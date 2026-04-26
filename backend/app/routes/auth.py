from fastapi import APIRouter, Depends, HTTPException, Security
from pydantic import BaseModel
from fastapi.security import HTTPAuthorizationCredentials
from app.dependencies import get_current_user_required, security
from app.services.auth import create_user, login_user, delete_session_token, check_email_status
router = APIRouter()


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str

class EmailStatusRequest(BaseModel):
    email: str

@router.post("/register")
def register(request: RegisterRequest):
    try:
        user = create_user(request.username, request.email, request.password)
        return {
            "message": "Account created successfully.",
            "user": user
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login(request: LoginRequest):
    try:
        return login_user(request.email, request.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/me")
def me(current_user=Depends(get_current_user_required)):
    return {
        "user": current_user
    }

@router.post("/logout")
def logout(
    credentials: HTTPAuthorizationCredentials = Security(security),
    current_user=Depends(get_current_user_required)
):
    token = credentials.credentials

    deleted = delete_session_token(token)

    return {
        "message": "Logged out successfully." if deleted else "Session already removed."
    }

@router.post("/email-status")
def email_status(request: EmailStatusRequest):
    try:
        return check_email_status(request.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))