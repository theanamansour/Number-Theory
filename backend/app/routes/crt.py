from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.crt import crt_compute_residues, crt_recover_A

router = APIRouter()


class CRTResiduesRequest(BaseModel):
    A: int
    moduli: list[int]


class CRTRecoverRequest(BaseModel):
    residues: list[int]
    moduli: list[int]


@router.post("/residues")
def compute_residues(request: CRTResiduesRequest):
    try:
        return crt_compute_residues(request.A, request.moduli)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/recover")
def recover_A(request: CRTRecoverRequest):
    try:
        return crt_recover_A(request.residues, request.moduli)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))