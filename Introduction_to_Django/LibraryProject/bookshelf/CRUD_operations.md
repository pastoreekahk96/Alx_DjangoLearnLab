Create `CRUD_operations.md` in `Introduction_to_Django/` with:

```markdown
# CRUD Operations for the Book model

## 1. Create
```python
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
# Expected output: <Book: 1984>

## 2. Retrieve
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
(book.title, book.author, book.publication_year)
# Expected output: ('1984', 'George Orwell', 1949)

## 3. Update
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(id=book.id)
# Expected output: <Book: Nineteen Eighty-Four>

## 4. Delete
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Expected output: (1, {'bookshelf.Book': 1})
Book.objects.all()
# Expected output: <QuerySet []>


