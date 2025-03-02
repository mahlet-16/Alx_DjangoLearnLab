from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class MyUserCreationForm(UserCreationForm):
    """
    A customized user creation form for adding extra fields during user registration.

    Attributes:
        model: The user model used for authentication (retrieved via get_user_model).
        fields: The fields to include in the form ('username', 'date_of_birth').
    """
    class Meta:
        model = get_user_model()
        fields = ['username', 'date_of_birth']
