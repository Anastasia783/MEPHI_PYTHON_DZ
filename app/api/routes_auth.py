from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.deps import (
    get_auth_usecase,
    get_current_user_id,
)
from app.core.errors import (
    ConflictError,
    NotFoundError,
    UnauthorizedError,
)
from app.schemas.auth import RegisterRequest, TokenResponse
from app.schemas.user import UserPublic
from app.usecases.auth import AuthUseCase


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    response_model=UserPublic,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    request: RegisterRequest,
    auth_usecase: AuthUseCase = Depends(get_auth_usecase),
) -> UserPublic:
    try:
        user = await auth_usecase.register(
            email=request.email,
            password=request.password,
        )
        return UserPublic.model_validate(user)
    except ConflictError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )


@router.post(
    "/login",
    response_model=TokenResponse,
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_usecase: AuthUseCase = Depends(get_auth_usecase),
) -> TokenResponse:
    try:
        access_token = await auth_usecase.login(
            email=form_data.username,
            password=form_data.password,
        )
        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
        )
    except UnauthorizedError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.get(
    "/me",
    response_model=UserPublic,
)
async def me(
    user_id: int = Depends(get_current_user_id),
    auth_usecase: AuthUseCase = Depends(get_auth_usecase),
) -> UserPublic:
    try:
        user = await auth_usecase.get_profile(user_id=user_id)
        return UserPublic.model_validate(user)
    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )
    except UnauthorizedError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
            headers={"WWW-Authenticate": "Bearer"},
        )