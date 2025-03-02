from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from LibraryProject import settings

"""
Models for the Bookshelf app.

Includes models for books, reviews, and a custom user model with a custom manager.
"""

# Book model
class Book(models.Model):
    """
    Represents a book in the library.

    Fields:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - publication_year (int): The year the book was published.

    Permissions:
        - Custom permissions for reviewing, viewing, editing, creating, and deleting books.
    """
    class Meta:
        permissions = [
            ('review_book', "Can review a book"),
            ('can_view', 'Can view books'),
            ('can_edit', 'Can edit a book'),
            ('can_create', "Can create a new book"),
            ("can_delete", 'Can delete a book')
        ]
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book:'{self.title}', Author: {self.author}, Year: {self.publication_year}'"

# Review model
class Review(models.Model):
    """
    Represents a review for a book.

    Fields:
        - book (ForeignKey): The book being reviewed.
        - user (ForeignKey): The user who wrote the review.
        - review_text (str): The content of the review.
        - created_at (datetime): The date and time the review was created.
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_reviews")
    review_text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.book.title} by {self.user.username}"

# Custom user manager
from django.contrib.auth.models import BaseUserManager
class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model.

    Methods:
        - create_user: Creates a regular user with the given fields.
        - create_superuser: Creates a superuser with the given fields.
    """
    def create_user(self, username: str, email: str | None = ..., password: str | None = ..., **extra_fields: Any) -> Any:
        return super().create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username: str, email: str | None, password: str | None, **extra_fields: Any) -> Any:
        return super().create_superuser(username, email, password, **extra_fields)

# Custom user model
class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.

    Fields:
        - date_of_birth (date): The user's date of birth.
        - profile_pic (ImageField): The user's profile picture.
    """
    class Meta:
        db_table = 'auth_user'

    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_pics/')
    objects = CustomUserManager()

