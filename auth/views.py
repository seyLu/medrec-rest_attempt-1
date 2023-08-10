from django.contrib.auth import authenticate
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from auth.models import LoginSerializer
from users.serializers import UserSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Bad Request",
                    "data": serializer.errors,
                },
                status.HTTP_400_BAD_REQUEST,
            )

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, email=email, password=password)
        if user is None:
            raise serializers.ValidationError({"detail": "Invalid Email or Password!"})

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "token": str(refresh),
            }
        )
