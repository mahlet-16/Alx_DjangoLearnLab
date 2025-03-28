from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

        def create(self, validated_data):
            user = get_user_model().objects.create_user(**validated_data)
            serializers.CharField()
            Token.objects.create(user=user)
            return user


