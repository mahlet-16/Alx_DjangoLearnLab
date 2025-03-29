from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, permissions, status
from .models import Post, Comment
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.contenttypes.models import ContentType
from rest_framework import filters
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializers):
        serializers.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializers):
        serializers.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author__in=user.following_set.all()).order_by('-created_at')


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"message": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification
        Notification.objects.create(
            recipient=post.user,
            actor=request.user,
            verb="liked your post",
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )

        return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)

        if not like.exists():
            return Response({"message": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
