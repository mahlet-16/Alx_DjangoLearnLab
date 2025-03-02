from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Book relations - possibly handling add, delete, and edit in one view
    path("relations/", views.book_relation, name='book_relation'),
    
    # Add, delete, and edit book paths
    path("add_book/", views.add_book, name='add_book'),
    path("delete_book/", views.delete_book, name='delete_book'),
    path("edit_book/", views.edit_book, name='edit_book'),
    
    # Home page and book list
    path('', views.index, name='index'),
    path('listbooks/', views.list_books, name='listbooks'),
    
    # Library detail view
    path('librarydetail/<int:pk>/', views.LibraryDetailView.as_view(), name='librarydetailview'),
    
    # User registration, login, and logout
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # User profile
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    # Views for members, librarians, and admins
    path('members/', views.member_view, name='members'),
    path('librarian/', views.librarian_view, name='librarian'),
    path('admin/', views.admin_view, name="admin"),
]
