from django.shortcuts import render, HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView

from .models import Book, Review
from .forms import ExampleForm

"""
Views for the Book application.

This module includes views for rendering the homepage, displaying books, 
and handling book review creation.
"""

# Homepage view
def homepage(request):
    """
    Renders the homepage of the book application.

    Args:
        request: The HTTP request object.

    Returns:
        An HTTP response with the rendered homepage template.
    """
    template = "bookshelf/home.html/"
    return render(request, template_name=template, context={})

# Book list view
def bookshop(request):
    """
    Renders a list of all available books in the database.

    Args:
        request: The HTTP request object.

    Returns:
        An HTTP response with the rendered book list template.
    """
    all_books = Book.objects.all()
    template = loader.get_template('bookshelf/book_list.html')
    context = {
        "all_books": all_books
    }
    return HttpResponse(template.render(context, request))

# Book review creation view
class BookReviewView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    A view for creating a book review.

    Attributes:
        model: The model associated with the form (Review).
        form_class: The form class to use for this view (ExampleForm).
        template_name: The template to render the form.
        success_url: The URL to redirect to after successful form submission.
        permission_required: The permission required to access this view.
    """
    model = Review
    form_class = ExampleForm
    template_name = 'bookshelf/form_example.html'
    success_url = reverse_lazy('booklist')  
    permission_required = 'bookshelf.review_book'
    raise_exception = True

    def form_valid(self, form):
        """
        Automatically assigns the currently logged-in user as the review author.

        Args:
            form: The form instance being validated.

        Returns:
            The HTTP response for the successful form submission.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


# Create your views here.
# def index(request):
#     return HttpResponse("Hello and welcome to my book app.")