from dataclasses import dataclass

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


@dataclass(frozen=True, slots=True)
class LoginResult:
    access_token: str
    refresh_token: str
    access_token_expires: int
    refresh_token_expires: int


def login_user(user: User):
    refresh_token = RefreshToken.for_user(user)
    access_token = str(refresh_token.access_token)
    access_token_expires: int = refresh_token.access_token['exp']
    refresh_token_expires: int = refresh_token['exp']
    return LoginResult(
        access_token=access_token,
        refresh_token=str(refresh_token),
        access_token_expires=access_token_expires,
        refresh_token_expires=refresh_token_expires,
    )
