# Retrieve all books
>>> books = Book.objects.all()
>>> for book in books:
...     print(book.title, book.author, book.publication_year)
1984 George Orwell 1949  # Expected output

