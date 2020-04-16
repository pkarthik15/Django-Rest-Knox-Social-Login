from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(email = validated_data['email'], first_name = validated_data['first_name'],  last_name=validated_data['last_name'],  password = validated_data['password'])

    return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")


# Social serializer
class SocialSerializer(serializers.Serializer):
  provider = serializers.CharField(max_length=255, required=True)
  access_token = serializers.CharField(allow_blank=False, trim_whitespace=True)
