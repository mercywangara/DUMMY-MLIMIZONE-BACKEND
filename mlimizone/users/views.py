from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.conf import settings
from .models import User
from .serializers import RegisterSerializer, WholesalerProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            if user.role == "admin":
                whitelist = getattr(settings, 'ADMIN_EMAIL_WHITELIST', [])
                if user.email not in whitelist:
                    return Response({'error': 'Admin not whitelisted'}, status=status.HTTP_403_FORBIDDEN)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class AuthenthicationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.email}! You are authenticated."})

class ProfileEditView(generics.RetrieveUpdateAPIView):
    serializer_class = WholesalerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        print("DEBUG: get_object called, user:", self.request.user)
        user = self.request.user
        if user.role != 'wholesaler':
            raise PermissionDenied("Only wholesalers can update their profile.")
        return user

    def put(self, request, *args, **kwargs):
        print("DEBUG: PUT method called with data:", request.data)
        return super().put(request, *args, **kwargs)