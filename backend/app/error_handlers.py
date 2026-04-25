from fastapi import Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def friendly_field_name(field: str) -> str:
    names = {
        "n": "number n",
        "a": "base a",
        "b": "exponent b",
        "A": "number A",
        "email": "email",
        "password": "password",
        "moduli": "moduli list",
        "residues": "residues list",
    }
    return names.get(field, field)


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    messages = []

    for error in exc.errors():
        field = error["loc"][-1]
        error_type = error["type"]
        field_name = friendly_field_name(str(field))

        if error_type == "missing":
            messages.append(f"{field_name} is required.")
        elif "int" in error_type:
            messages.append(f"{field_name} must be a valid integer.")
        elif "list" in error_type:
            messages.append(f"{field_name} must be a valid list.")
        elif "string" in error_type:
            messages.append(f"{field_name} must be valid text.")
        else:
            messages.append(f"{field_name} has an invalid value.")

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": {
                "type": "validation_error",
                "message": "Please check your input and try again.",
                "details": messages
            }
        }
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "type": "request_error",
                "message": exc.detail
            }
        }
    )


async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "type": "server_error",
                "message": "Something went wrong on the server. Please try again later."
            }
        }
    )