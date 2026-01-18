from ninja import Router
from ninja.errors import HttpError
from django.contrib.auth import authenticate
from ninja_jwt.tokens import RefreshToken
from ninja_jwt.tokens import Token
from authentication.schemas.auth import LoginIn, TokenOut, RefreshIn
from authentication.schemas.auth import VerifyInput, SuccessMessage, ErrorDetail, RegisterIn



router = Router()



@router.post(
    "/register",
    response={201: dict, 400: ErrorDetail},
    summary="Cadastro de usuario.",
    description="Cadastro de um novo usuario."
)
def register(request, registro: RegisterIn):
    pass


@router.post(
    "/login", 
    response={200: TokenOut, 401: ErrorDetail},
    summary="Login",
    description="Autentica o usuário e retorna um par de tokens (access e refresh)."
)
def login(request, login: LoginIn):
    """
    Endpoint de login que retorna tokens JWT
    """
    user = authenticate(username=login.username, password=login.password)

    if not user:
        raise HttpError(401, "Credenciais inválidas")
    
    refresh = RefreshToken.for_user(user)

    return {
        "access_token": str(refresh.access_token),
        "refresh": str(refresh)
    }
 

@router.post(
    "/refresh", 
    response={200: TokenOut, 401: ErrorDetail},
    summary="Refresh token",
    description="Renova o access token usando o refresh token."
)
def refresh_token(request, data: RefreshIn):
    """
    Endpoint para refresh do token JWT
    """
    try:
        refresh = RefreshToken(data.refresh)
        access_token = str(refresh.access_token)
        return 200, {"access": new_access_token}

    except Exception as e:
        raise HttpError(401, "Refresh token inválido")


@router.post(
    "/verify",
    response={200: SuccessMessage, 401: ErrorDetail},
    summary="Verify Token",
    description="Verifica a validade de um token (access ou refresh)."
)
def verify_token(request, data: VerifyInput):
    """
    Endpoint para verificação de token JWT
    """
    try:
        if not data.token:
            raise HttpError(401, "Token inválido")
        
        token_instancia = Token(data.token)
        return 200, {"detail": "Token válido"}
    except:
        raise HttpError(401, "Token inválido")
   