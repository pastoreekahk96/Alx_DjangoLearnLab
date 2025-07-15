# CRUD Operations on Book Model

---

## CREATE
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book
<Book: 1984>  # Object successfully created

---

## RETRIEVE
>>> Book.objects.all()
<QuerySet [<Book: 1984>]>  # Retrieved successfully

---

## UPDATE
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book
<Book: Nineteen Eighty-Four>  # Title updated

---

## DELETE
>>> book.delete()
(1, {'bookshelf.Book': 1})  # Book deleted
>>> Book.objects.all()
<QuerySet []>  # Confirmed deletion

