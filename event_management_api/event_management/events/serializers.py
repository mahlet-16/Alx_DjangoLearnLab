from rest_framework import serializers
from .models import User, Event, Location, Category, EventRegistration, Feedback

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'created_at']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'address']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class EventSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    organizer = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date_time', 'location', 'category', 'capacity', 'organizer', 'created_at']

class EventRegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = EventRegistration
        fields = ['id', 'user', 'event', 'registered_at']

class FeedbackSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'user', 'event', 'rating', 'comment', 'created_at']