# retrieve

```python
from bookshelf.models import Book


books  = Book.objects.all()
print(books)

first_book = Book.objects.first()
print(first_book.title, first_book.author, first_book.publication_year)
```