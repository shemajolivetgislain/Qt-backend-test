from rest_framework import serializers
from .models import User
from utils.validators import validate_password

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    password = serializers.CharField(
        write_only=True,
        min_length=8,
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password',   'is_staff', 'is_active']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',  'is_staff', 'is_active']