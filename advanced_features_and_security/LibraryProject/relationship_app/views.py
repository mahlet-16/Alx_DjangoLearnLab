from django.shortcuts import render, redirect, HttpResponse
from .models import Author, Book, Librarian, Library, UserProfile
from django.template import loader
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth import get_user_model

from django.contrib.auth import login as auth_login


# Helper functions to check roles
def has_role(user, role):
    return UserProfile.objects.filter(user=user.id, role=role).exists()

def member_test(user):
    return has_role(user, "Member")

def librarian_test(user):
    return has_role(user, "Librarian")

def admin_test(user):
    return has_role(user, "Admin")


# Role-based Views
@user_passes_test(member_test)
def member_view(request):
    """
    View for the Member page. This page is accessible only to users with the 'Member' role.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response containing the Member page template.
    """
    return render(request, 'relationship_app/member_view.html')


@user_passes_test(librarian_test)
def librarian_view(request):
    """
    View for the Librarian page. This page is accessible only to users with the 'Librarian' role.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response containing the Librarian page template.
    """
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(admin_test)
def admin_view(request):
    """
    View for the Admin page. This page is accessible only to users with the 'Admin' role.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response containing the Admin page template.
    """
    return render(request, 'relationship_app/admin_view.html')


# General Views
def index(request):
    return HttpResponse('Hello and welcome?')

def list_books(request):
    """
    Lists all the books available in the library.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response containing the list of books.
    """
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    """
    Class-based view to display the details of a specific library, including its books.

    Args:
        request (HttpRequest): The HTTP request object.
        kwargs: Arguments passed to the view for dynamic behavior (e.g., library ID).
    
    Returns:
        HttpResponse: The rendered response containing the library's details and its books.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()  # Add books to context
        return context
    
# Class-based View for User Registration
from .forms import MyUserCreationForm
class RegisterView(CreateView):
    """
    A class-based view for user registration.

    This view uses the `MyUserCreationForm` form to register new users. 
    On successful registration, the user is redirected to the login page.

    Attributes:
        form_class (Form): The form used to create a new user.
        success_url (str): The URL to redirect to after a successful form submission (login page).
        template_name (str): The template to render for user registration.

    Methods:
        get_context_data(**kwargs): (Inherited) Adds additional context to the template.
    """
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'


# Class-based View for Profile
class ProfileView(TemplateView):
    """
    A class-based view to display the user's profile page.

    This view renders the user's profile template, allowing users to see their personal information.

    Attributes:
        template_name (str): The template to render for the profile page.
    """
    template_name = 'relationship_app/profile.html'


# Permission-based View
@permission_required("relationship_app.can_add_book", "relationship_app.can_delete_book", "relationship_app.can_change_book")
def book_relation(request):
    """
    A view to manage book-related permissions.

    This view is restricted to users who have specific permissions (`can_add_book`, `can_delete_book`, `can_change_book`).
    When a user with the correct permissions accesses this view, a welcome message is displayed.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The response with a welcome message for the user.
    """
    return HttpResponse('Welcome to the relationship site!')

#to be implemented later
def add_book():
    return HttpResponse('<h1>Coming Soon!<h1>')

def edit_book():
    return HttpResponse('<h1>Coming Soon!<h1>')

def delete_book():
    return HttpResponse('<h1>Coming Soon!<h1>')







    
