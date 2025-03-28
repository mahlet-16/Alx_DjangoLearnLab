from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, permissions
from .models import Post, Comment
from rest_framework.response import Response
from rest_framework import filters

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
        "Post.objects.filter(author__in=following_users).order_by", "following.all()"
