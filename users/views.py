from rest_framework.response import Response
from rest_framework import generics, status
from users.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from rest_framework.permissions import AllowAny
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
       
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Customize the response data
        response_data = {
            "message": "Account created successfully",
            "user": serializer.data
        }

        # Return a Response object with the custom data and status code
        return Response(response_data, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user = User.objects.get(email=request.data['email'])
            refresh = RefreshToken.for_user(user)
            access_token = response.data['access']
            refresh_token = str(refresh)
            payload = {
                'id': user.id,
                'email': user.email,
                # 'username': user.username,
                'lastname':user.last_name,
                'firstname':user.first_name,
                "is_active":user.is_active
            }
            response.data = {
                'Message': "Login successful",
                'user': payload,
                'access_token': access_token,
                'refresh_token': refresh_token,
            }
        return response