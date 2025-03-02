from typing import Any
from django.db import models
from LibraryProject import settings

class Author(models.Model):
    """
    Represents an author of a book.

    Attributes:
        - name (str): The author's name. Maximum length: 100 characters.
    """

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Returns a string representation of the author."""
        return self.name


class Book(models.Model):
    """
    Represents a book in the library.

    Attributes:
        - title (str): The title of the book. Maximum length: 200 characters.
        - author (Author): A foreign key to the Author model, representing the author of the book.
                           Deletes related books if the referenced author is deleted (CASCADE).
    """

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self) -> str:
        """Returns a string representation of the book with its title and author."""
        return f"'{self.title}' by {self.author}"

    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]


class Library(models.Model):
    """
    Represents a library containing books.

    Attributes:
        - name (str): The name of the library. Maximum length: 200 characters.
        - books (ManyToMany[Book]): A many-to-many relationship with the Book model.
                                    Multiple libraries can have the same books.
    """

    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='library')

    def __str__(self) -> str:
        """Returns the name of the library."""
        return self.name


class Librarian(models.Model):
    """
    Represents a librarian working at a library.

    Attributes:
        - name (str): The name of the librarian. Maximum length: 100 characters.
        - library (Library): A one-to-one relationship with the Library model, representing where the librarian works.
                             If the associated library is deleted, the librarian's library is set to Null.
    """

    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        """Returns the name of the librarian."""
        return self.name


class UserProfile(models.Model):
    """
    Represents a user profile with specific roles within the application.

    Attributes:
        - user (User): A one-to-one relationship with the default user model (AUTH_USER_MODEL).
        - role (str): The role of the user within the application, chosen from 'Admin', 'Librarian', or 'Member'.
    """

    class Roles(models.TextChoices):
        ADMIN = "Admin", "Administrator"
        LIBRARIAN = "Librarian", "Librarian"
        MEMBER = "Member", "Member"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='userprofiles'
    )
    role = models.CharField(
        max_length=20, choices=Roles.choices, default=Roles.MEMBER
    )

    def __str__(self) -> str:
        """Returns a string representation of the user profile."""
        return f"{self.user.username}'s profile."

