# Generated by Django 4.1.5 on 2023-02-01 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_book_book_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_owner',
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]
