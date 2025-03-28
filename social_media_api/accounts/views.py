from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    """Allows the authenticated user to follow another user."""
    try:
        user_to_follow = User.objects.get(id=user_id)
        request.user.following_set.add(user_to_follow)
        return Response({'status': f'Now following {user_to_follow.username}'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    """Allows the authenticated user to unfollow another user."""
    try:
        user_to_unfollow = User.objects.get(id=user_id)
        request.user.following_set.remove(user_to_unfollow)
        return Response({'status': f'Unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
