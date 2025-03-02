from django.urls import path
from . import views

urlpatterns = [
    # Uncomment the next line to enable the index view
    # path("", views.index, name='index'),  
    
    # Path for the homepage
    path('home/', views.homepage, name='home'),
    
    # Path to view the list of books
    path('books/', views.bookshop, name='books'),
    
    # Path to create a new review for a book (requires user to be logged in)
    path('books/reviews/', views.BookReviewView.as_view(), name='reviews'),
]
