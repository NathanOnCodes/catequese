from ninja import Router
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from auth.schemas.auth import LoginIn, RefreshIn, TokenOut, UserOut, ErrorOut

router = Router()


@router.post("/login", response={200: TokenOut, 401: ErrorOut})
def login(request, data: LoginIn):
    """
    Endpoint de login que retorna tokens JWT
    """
    user = authenticate(username=data.username, password=data.password)
    
    if user is None:
        return 401, {"detail": "Credenciais inválidas"}
    
    refresh = RefreshToken.for_user(user)
    
    return {
        "access_token": str(refresh.access_token),
        "refresh_token": str(refresh),
        "token_type": "Bearer"
    }


@router.post("/refresh", response={200: TokenOut, 401: ErrorOut})
def refresh_token(request, data: RefreshIn):
    """
    Endpoint para refresh do token JWT
    """
    try:
        refresh = RefreshToken(data.refresh_token)
        access_token = str(refresh.access_token)
        
        # Gera um novo refresh token e invalida o antigo
        refresh.blacklist()
        new_refresh = RefreshToken.for_user(
            type('User', (), {'id': refresh.payload.get('user_id')})()
        )
        
        return {
            "access_token": access_token,
            "refresh_token": str(new_refresh),
            "token_type": "Bearer"
        }
    except Exception as e:
        return 401, {"detail": f"Token inválido: {str(e)}"}


@router.get("/me", response={200: UserOut, 401: ErrorOut})
def get_current_user(request):
    """
    Endpoint para obter informações do usuário atual
    """
    if not request.user.is_authenticated:
        return 401, {"detail": "Não autenticado"}
    
    return {
        "id": request.user.id,
        "username": request.user.username,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
    }
