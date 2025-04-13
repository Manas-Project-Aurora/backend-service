from typing import Optional

from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication


class HttpOnlyCookiesAuthentication(JWTAuthentication):

    def get_header(self, request: Request) -> bytes:
        return request.COOKIES.get('access_token')

    def get_raw_token(self, header: bytes) -> Optional[bytes]:
        return header
