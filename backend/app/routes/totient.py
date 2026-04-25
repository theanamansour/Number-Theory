from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.dependencies import get_current_user_optional
from app.services.totient import euler_totient
from app.services.history import save_history_entry

router = APIRouter()

class TotientRequest(BaseModel):
    n: int

    def validate_input(self):
        if self.n <= 0:
            raise ValueError("Please enter a positive integer greater than 0.")
        if self.n > 10**12:
            raise ValueError("Please enter a smaller number. The maximum allowed value is 10^12.")

@router.post("/")
def compute_totient(
    request: TotientRequest,
    current_user=Depends(get_current_user_optional)
):
    try:
        request.validate_input()
        result = euler_totient(request.n)

        if current_user:
            save_history_entry(
                current_user["id"],
                "euler_totient",
                {"n": request.n},
                result
            )

        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))