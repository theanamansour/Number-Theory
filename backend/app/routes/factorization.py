from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.factorization import prime_factorization

router = APIRouter()

class FactorizationRequest(BaseModel):
    n: int

@router.post("/")
def factorize_number(request: FactorizationRequest):
    try:
        return prime_factorization(request.n)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))