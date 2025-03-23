from rest_framework import serializers 
from django.contrib.auth.models import User
from ..models import Profile


# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import Profile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio','profile_picture']
         



class ChangeEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required =True)
    profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ['email', 'profile']
    
    def validate_email(self, value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError("Email is already in use")
        return value
    def update(self, instance, validated_data):
        instance.email = validated_data['email']
        instance.save()
        
        profile_data = validated_data.get('profile', {})
        profile = instance.profile  # Access the related profile
        profile.bio = profile_data.get('bio', profile.bio)
        profile.profile_picture = profile_data.get('profile_picture', profile.profile_picture)
        profile.save()
        return instance