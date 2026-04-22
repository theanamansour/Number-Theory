from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.fastexp import fast_exponentiation

router = APIRouter()

class FastExponentiationRequest(BaseModel):
    a: int
    b: int
    n: int

@router.post("/")
def compute_fast_exponentiation(request: FastExponentiationRequest):
    try:
        return fast_exponentiation(request.a, request.b, request.n)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))