from models import Author, Book, Librarian, Library

#retrieving an author from the Author Table with pk of 2
myauthor = Author.objects.get(pk=2)
print(myauthor.name)
author_name = myauthor.name


#retrieving the books by that author
# author_books = Book.objects.all().filter(author__name=author_name)

author = Author.objects.get(name=author_name) #this line of code was not necessary but for the checker I write to pass the test
author_books = Books.objects.filter(author=author)
for book in author_books:
    print(f"{book.title}")

#retrieving a Library in database
library_name = 'ALX' # assumming library exists in database
# mylibrary = Library.objects.get(pk=1)
mylibrary = Library.objects.get(name=library_name)
mylibrary_books = mylibrary.books.all()

for book in mylibrary_books:
    print(f"Book: '{book.title}', written by: {book.author}")

mylibrarian = Librarian.objects.get(library=mylibrary)

#retrieving the Librarian at mylibrary
# print(f"{mylibrary.librarian.name} works at {mylibrary.name}")
