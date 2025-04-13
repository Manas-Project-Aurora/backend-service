from typing import Optional

from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, Token


class HttpOnlyCookiesAuthentication(JWTAuthentication):

    def get_header(self, request: Request) -> bytes:
        return request.COOKIES.get('access_token')

    def get_raw_token(self, header: bytes) -> Optional[bytes]:
        return header


class HttpOnlyRefreshTokenCookiesAuthentication(JWTAuthentication):

    def get_header(self, request: Request) -> bytes:
        return request.COOKIES.get('refresh_token')

    def get_raw_token(self, header: bytes) -> Optional[bytes]:
        return header

    def get_validated_token(self, raw_token) -> Token:
        return RefreshToken(raw_token)
