from fastapi import APIRouter, Depends
from app.dependencies import get_current_user_required
from app.services.history import get_user_history

router = APIRouter()


@router.get("/me")
def my_history(current_user=Depends(get_current_user_required)):
    history = get_user_history(current_user["id"])
    return {
        "user": current_user,
        "history": history
    }