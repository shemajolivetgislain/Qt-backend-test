from rest_framework.response import Response
from rest_framework import generics, status
from users.serializers import UserSerializer, ReadUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            # Customize the response data
            response_data = {
                "message": "Account created successfully",
                "user": serializer.data
            }

            # Return a Response object with the custom data and status code
            return Response(response_data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            # Extract the error message for the email field
            email_errors = e.detail.get('email', [])
            if email_errors:
                return Response({"error": email_errors[0]}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)


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
    

    # Listing of users
class ListUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            users = User.objects.all()
            serializer = ReadUserSerializer(users, many=True)
            message = "List of all users retrieved successfully."
            data = {
                "message": message,
                "users": serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)