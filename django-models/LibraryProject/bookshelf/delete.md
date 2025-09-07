# delete

```python
from bookshelf.models import Book

book = Book.objects.get(title="nineteen eighty-four")
book.delete()

print(Book.objects.all())

```