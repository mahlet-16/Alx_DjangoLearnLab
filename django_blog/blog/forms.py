from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your comment here...'}),
            
        }
"TagWidget()", "tags"

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]