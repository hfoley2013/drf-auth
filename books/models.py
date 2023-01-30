from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Book(models.Model):
    book_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                             help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=64)
    summary = models.TextField(help_text='Enter a brief description of the book.')
    notes = models.TextField()

    # DateTimeField

    # DateField.auto_now_add: Automatically set the field to now when the object is first created.
    # Useful for creation of timestamps.

    # The default time zone is the time zone defined by the TIME_ZONE setting.

    date_read = models.DateTimeField(auto_now_add=True)

    # DateField.auto_now: Automatically set the field to now every time the
    # object is saved. Useful for “last-modified” timestamps.
    # !! The options auto_now_add, auto_now, and default are mutually
    # exclusive.
    entry_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
