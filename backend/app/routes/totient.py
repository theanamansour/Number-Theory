from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.totient import euler_totient

router = APIRouter()

class TotientRequest(BaseModel):
    n: int

@router.post("/")
def compute_totient(request: TotientRequest):
    try:
        return euler_totient(request.n)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))