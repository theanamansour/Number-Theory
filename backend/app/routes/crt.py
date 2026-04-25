from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.dependencies import get_current_user_optional
from app.services.crt import crt_compute_residues, crt_recover_A
from app.services.history import save_history_entry

router = APIRouter()


class CRTResiduesRequest(BaseModel):
    A: int
    moduli: list[int]

    def validate_input(self):
        if len(self.moduli) == 0:
            raise ValueError("Please provide at least one modulus.")
        if len(self.moduli) > 10:
            raise ValueError("Please provide at most 10 moduli.")
        if any(m <= 1 for m in self.moduli):
            raise ValueError("Each modulus must be greater than 1.")
        if any(m > 10**9 for m in self.moduli):
            raise ValueError("Each modulus must be less than or equal to 10^9.")
        if abs(self.A) > 10**12:
            raise ValueError("Number A is too large. Please use a value between -10^12 and 10^12.")


class CRTRecoverRequest(BaseModel):
    residues: list[int]
    moduli: list[int]

    def validate_input(self):
        if len(self.residues) == 0:
            raise ValueError("Please provide at least one residue.")
        if len(self.moduli) == 0:
            raise ValueError("Please provide at least one modulus.")
        if len(self.residues) != len(self.moduli):
            raise ValueError("Residues and moduli must have the same length.")
        if len(self.moduli) > 10:
            raise ValueError("Please provide at most 10 moduli.")
        if any(m <= 1 for m in self.moduli):
            raise ValueError("Each modulus must be greater than 1.")
        if any(m > 10**9 for m in self.moduli):
            raise ValueError("Each modulus must be less than or equal to 10^9.")


@router.post("/residues")
def compute_residues(
    request: CRTResiduesRequest,
    current_user=Depends(get_current_user_optional)
):
    try:
        request.validate_input()
        result = crt_compute_residues(request.A, request.moduli)

        if current_user:
            save_history_entry(
                current_user["id"],
                "crt_residues",
                {"A": request.A, "moduli": request.moduli},
                result
            )

        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/recover")
def recover_A(
    request: CRTRecoverRequest,
    current_user=Depends(get_current_user_optional)
):
    try:
        request.validate_input()
        result = crt_recover_A(request.residues, request.moduli)

        if current_user:
            save_history_entry(
                current_user["id"],
                "crt_recover",
                {"residues": request.residues, "moduli": request.moduli},
                result
            )

        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))