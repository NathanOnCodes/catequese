from ninja import Schema
from typing import Optional


class LoginIn(Schema):
    """Schema para requisição de login"""
    username: str
    password: str


class RefreshIn(Schema):
    """Schema para requisição de refresh token"""
    refresh_token: str


class TokenOut(Schema):
    """Schema para resposta de tokens JWT"""
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"


class VerifyInput(Schema):
    """Schema para os dados de entrada na verificação de token."""
    token: str

class SuccessMessage(Schema):
    """Schema genérico para mensagens de sucesso ou confirmação."""
    detail: str

# Exemplo de schema de erro (opcional, mas útil)
class ErrorDetail(Schema):
    """Schema para detalhes de erro."""
    detail: str