from .models import Review
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class ExampleForm(forms.ModelForm):
    """
    A form for submitting reviews on books.

    Attributes:
        model: The model associated with the form (Review).
        fields: The fields to include in the form ('book', 'review_text').
        labels: Human-readable labels for the fields in the form.
    """
    class Meta:
        model = Review
        fields = ['book', 'review_text']
        labels = {
            'book': 'Select Book',
            'review_text': 'Your Review',
        }

