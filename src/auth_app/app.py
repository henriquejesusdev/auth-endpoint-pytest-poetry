"""Aplicação simples com endpoint de autenticação.

Cenário:
- Existe um único usuário fixo (email e senha pré-definidos).
- O endpoint /auth valida as credenciais e retorna:
  - Sucesso (200) com token e mensagem
  - Erro (401) com detalhe de erro
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Auth Exercise")

# Usuário fixo (para o exercício)
FIXED_USER_EMAIL = "user@example.com"
FIXED_USER_PASSWORD = "123456"


class AuthRequest(BaseModel):
    email: EmailStr
    password: str


class AuthSuccessResponse(BaseModel):
    token: str
    message: str


@app.post("/auth", response_model=AuthSuccessResponse)
def authenticate(payload: AuthRequest) -> AuthSuccessResponse:
    if payload.email == FIXED_USER_EMAIL and payload.password == FIXED_USER_PASSWORD:
        return AuthSuccessResponse(token="fake-jwt-token", message="Authenticated")
    raise HTTPException(status_code=401, detail="Invalid credentials")
