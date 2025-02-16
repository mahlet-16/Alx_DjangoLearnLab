from bookshelf.models import Book
book.delete()
# Expected output:
(1, {'bookshelf.Book': 1})

Book.objects.all()
# Expected output:
<QuerySet []>
