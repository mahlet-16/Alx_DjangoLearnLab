from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the feature")
        return value
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)    

    class Meta:
        model = Author
        fields = '__all__'

    