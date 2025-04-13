import datetime
from dataclasses import dataclass

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


@dataclass(frozen=True, slots=True)
class LoginResult:
    access_token: str
    refresh_token: str
    access_token_expires: datetime.datetime
    refresh_token_expires: datetime.datetime


def login_user(user: User):
    refresh_token = RefreshToken.for_user(user)
    refresh_token.set_exp(
        lifetime=settings.SIMPLE_JWT.get(
            "REFRESH_TOKEN_LIFETIME",
            datetime.timedelta(days=24),
        ),
    )
    refresh_token.set_iat()
    refresh_token.set_jti()

    access_token = refresh_token.access_token
    access_token.set_exp(
        lifetime=settings.SIMPLE_JWT.get(
            "ACCESS_TOKEN_LIFETIME",
            datetime.timedelta(hours=1),
        ),
    )
    access_token.set_iat()

    access_token_expires: int = refresh_token.access_token['exp']
    refresh_token_expires: int = refresh_token['exp']

    return LoginResult(
        access_token=str(access_token),
        refresh_token=str(refresh_token),
        access_token_expires=datetime.datetime.fromtimestamp(access_token_expires),
        refresh_token_expires=datetime.datetime.fromtimestamp(refresh_token_expires),
    )
