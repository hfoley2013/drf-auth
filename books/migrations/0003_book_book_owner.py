# Generated by Django 4.1.5 on 2023-01-30 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_alter_book_author_alter_book_isbn_alter_book_summary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
