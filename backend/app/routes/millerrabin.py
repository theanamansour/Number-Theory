from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.dependencies import get_current_user_optional
from app.services.history import save_history_entry
from app.services.millerrabin import miller_rabin

router = APIRouter()

class MillerRabinRequest(BaseModel):
    n: int
    a: int

    def validate_input(self):
        if self.n < 3:
            raise ValueError("Number n must be an odd integer greater than or equal to 3.")
        if self.n % 2 == 0:
            raise ValueError("Number n must be odd for the Miller-Rabin test.")
        if self.n > 10**18:
            raise ValueError("Number n is too large. Please use a value less than or equal to 10^18.")
        if self.a <= 1 or self.a >= self.n - 1:
            raise ValueError("Base a must satisfy 1 < a < n - 1.")

@router.post("/")
def test_miller_rabin(
    request: MillerRabinRequest,
    current_user=Depends(get_current_user_optional)
):
    try:
        request.validate_input()
        result = miller_rabin(request.n, request.a)

        if current_user:
            save_history_entry(
                current_user["id"],
                "miller_rabin",
                {"n": request.n, "a": request.a},
                result
            )

        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))