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


class UserOut(Schema):
    """Schema para resposta de dados do usuário"""
    id: int
    username: str
    email: str
    first_name: str
    last_name: str


class ErrorOut(Schema):
    """Schema para resposta de erro"""
    detail: str
