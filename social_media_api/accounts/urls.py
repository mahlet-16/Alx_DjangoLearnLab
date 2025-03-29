from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import RegisterView, follow_user, unfollow_user
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path("follow/<int:user_id>/", follow_user, name="follow_user"),
    path("unfollow/<int:user_id>/", unfollow_user, name="unfollow_user"),]