from fastapi import APIRouter, Depends
from app.dependencies import get_current_user_required
from app.services.history import get_user_history, clear_user_calculation_history

router = APIRouter()


@router.get("/me")
def my_history(current_user=Depends(get_current_user_required)):
    history = get_user_history(current_user["id"])
    return {
        "user": current_user,
        "history": history
    }

@router.delete("/me")
def clear_my_calculation_history(current_user=Depends(get_current_user_required)):
    deleted_count = clear_user_calculation_history(current_user["id"])

    return {
        "message": "Calculation history cleared successfully.",
        "deleted_count": deleted_count
    }