
from fastapi.middleware.cors import CORSMiddleware
from app.db import init_db
from app.routes import factorization, totient, millerrabin, fastexp, crt, auth, history, education
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from app.error_handlers import (
    validation_exception_handler,
    http_exception_handler,
    general_exception_handler
)

app = FastAPI(
    title="Number Theory Web Application",
    description="Educational cryptography toolkit",
    version="1.0.0"
)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "https://number-theory-toolkit.vercel.app"
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

app.include_router(
    auth.router,
    prefix="/api/auth",
    tags=["Authentication"]
)

app.include_router(
    history.router,
    prefix="/api/history",
    tags=["History"]
)

app.include_router(
    education.router,
    prefix="/api/education",
    tags=["Education"]
)

app.include_router(
    factorization.router,
    prefix="/api/factorization",
    tags=["Factorization"]
)

app.include_router(
    totient.router,
    prefix="/api/totient",
    tags=["Totient"]
)

app.include_router(
    millerrabin.router, 
    prefix="/api/millerrabin", 
    tags=["Miller-Rabin"]
)

app.include_router(
    fastexp.router, 
    prefix="/api/fastexp", 
    tags=["Fast Exponentiation"]
)

app.include_router(
    crt.router, 
    prefix="/api/crt", 
    tags=["Chinese Remainder Theorem"]
)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}