from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.dependencies import get_current_user_optional
from app.services.fastexp import fast_exponentiation
from app.services.history import save_history_entry

router = APIRouter()

class FastExponentiationRequest(BaseModel):
    a: int
    b: int
    n: int

    def validate_input(self):
        if self.b < 0:
            raise ValueError("Exponent b must be a non-negative integer.")
        if self.n <= 0:
            raise ValueError("Modulus n must be a positive integer greater than 0.")
        if abs(self.a) > 10**12:
            raise ValueError("Base a is too large. Please use a value between -10^12 and 10^12.")
        if self.b > 10**9:
            raise ValueError("Exponent b is too large. Please use a value less than or equal to 10^9.")
        if self.n > 10**12:
            raise ValueError("Modulus n is too large. Please use a value less than or equal to 10^12.")

@router.post("/")
def compute_fast_exponentiation(
    request: FastExponentiationRequest,
    current_user=Depends(get_current_user_optional)
):
    try:
        request.validate_input()
        result = fast_exponentiation(request.a, request.b, request.n)

        if current_user:
            save_history_entry(
                current_user["id"],
                "fast_exponentiation",
                {"a": request.a, "b": request.b, "n": request.n},
                result
            )

        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))