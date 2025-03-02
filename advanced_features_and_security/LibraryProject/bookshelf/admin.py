from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser, Review
from django.utils.translation import gettext_lazy as _

"""
Admin configuration for the Library app.

This module customizes the admin interface for managing books, reviews, 
and the custom user model.
"""

# Admin configuration for the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Book model.

    Features:
        - Displays title, author, and publication year in the admin list view.
        - Allows searching by title, author, and publication year.
        - Filters the list view by title, author, and publication year.
    """
    list_display = ("title", "author", "publication_year")
    search_fields = ["title", "author", "publication_year"]
    list_filter = ("title", "author", "publication_year")

# Admin configuration for the Review model
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Review model.

    Features:
        - Displays book, user, and review text in the admin list view.
    """
    list_display = ["book", "user", "review_text"]

# Register the custom user model with a CustomUserAdmin that inherits from the default useradmin
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # List of fields to display in the user list page of the admin interface
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_active', 'is_staff')

    # Fields that can be used for filtering users
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups')

    # Fields to be included in the search bar
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Fields that will appear when adding/editing a user
    ordering = ('username',)
        # Define which fields will be displayed in the detail view (edit page)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'date_of_birth')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Define which fields will be shown when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'date_of_birth', 'is_active', 'is_staff')}
        ),
    )

    # Customizing how the password is set
    def get_fieldsets(self, request, obj=None):
        if not obj:  # Adding a new user
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

admin.site.register(CustomUser, CustomUserAdmin)
