from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer


class RefreshTokenApi(APIView):

    def post(self, request: Request, *args, **kwargs) -> Response:
        refresh_token = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(refresh_token)
        print(refresh_token.payload)

        access_token = refresh_token.access_token

        response = Response(status=status.HTTP_200_OK)
        response.set_cookie(
            key='refresh_token',
            value=str(refresh_token),
            httponly=True,
            secure=True,
            samesite='Strict',
            expires=refresh_token.get('exp', None),
        )
        response.set_cookie(
            key='access_token',
            value=str(access_token),
            httponly=True,
            secure=True,
            samesite='Strict',
            expires=access_token.get('exp', None),
        )
        return response
