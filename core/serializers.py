from rest_framework import serializers
from .models import NewPost
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class NewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewPost
        fields = ['title', 'content', 'created_at']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user_id': instance.id,
            'username': instance.username,
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }