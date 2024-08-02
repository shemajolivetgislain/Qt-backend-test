from django.urls import path
from .views import CustomTokenObtainPairView, CreateUserView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('create/',CreateUserView.as_view(), name='create-users'),
]