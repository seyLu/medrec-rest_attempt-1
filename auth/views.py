from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from auth.serializers import LoginSerializer, RegisterSerializer


class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, email=email, password=password)
        if user is None:
            raise AuthenticationFailed({"detail": "Invalid Email or Password!"})

        return Response({"email": email, "message": "Succesfully logged in."})


class LogoutAPIView(APIView):
    pass
