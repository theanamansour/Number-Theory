from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.millerrabin import miller_rabin

router = APIRouter()

class MillerRabinRequest(BaseModel):
    n: int
    a: int

@router.post("/")
def test_miller_rabin(request: MillerRabinRequest):
    try:
        return miller_rabin(request.n, request.a)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))