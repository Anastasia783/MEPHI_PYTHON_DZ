from datetime import datetime, timedelta, timezone
from typing import Any, Dict

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

algorithm = "HS256"
access_token_expire_minutes = 30 


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
    *,
    user_id: int,
    role: str,
    expires_delta: timedelta | None = None,
) -> str:
    now = datetime.now(timezone.utc)
    if expires_delta is None:
        expires_delta = timedelta(minutes=access_token_expire_minutes)

    expire = now + expires_delta

    payload: Dict[str, Any] = {
        "sub": str(user_id),
        "role": role,
        "iat": int(now.timestamp()),
        "exp": expire,
    }

    encoded_jwt = jwt.encode(
        payload,
        settings.jwt_secret,
        algorithm=algorithm,
    )
    return encoded_jwt


def decode_access_token(token: str) -> Dict[str, Any]:
    """
    Декодирует и валидирует JWT.
    При протухшем токене бросает JWTError.
    """
    return jwt.decode(
        token,
        settings.jwt_secret,
        algorithms=[algorithm],
    )