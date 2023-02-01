from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Book(models.Model):
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='books',
        default=None,
        null=True,
        blank=True
    )
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        unique=True,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
    )
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=64)
    summary = models.TextField(help_text='Enter a brief description of the book.')
    notes = models.TextField()
    date_read = models.DateTimeField(auto_now_add=True)
    entry_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
