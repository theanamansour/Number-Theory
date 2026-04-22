from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import factorization, totient, millerrabin, fastexp, crt

app = FastAPI(
    title="Number Theory Web Application",
    description="Educational cryptography toolkit",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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