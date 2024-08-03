from django.urls import path
from .views import CustomTokenObtainPairView, CreateUserView, ListUserAPIView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('create/',CreateUserView.as_view(), name='create-users'),
    path('list/', ListUserAPIView.as_view(), name='list-users'),  # List all users
]