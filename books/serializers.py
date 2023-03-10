# Imports the serializers module from the djangorestframework library. This module provides a set of classes for converting complex data types, such as Django models, into Python data types that can be easily rendered into JSON or other content types.
from rest_framework import serializers
# Imports the Book model from the same directory as the current file. This is the model that we will be serializing.
from .models import Book


# Defines a new class, BookSerializer, which subclasses serializers.ModelSerializer. This means that the BookSerializer class inherits all the behavior of serializers.ModelSerializer, but can also add or override behavior as needed.
class BookSerializer(serializers.ModelSerializer):
    # Defines an inner class, Meta, which is used to specify metadata about the serializer class.
    class Meta:
        # Specifies the fields from the Book model that should be included in the serialized representation.
        fields = ('id', 'owner', 'isbn', 'title', 'author', 'genre', 'summary', 'notes', 'date_read', 'entry_updated_at')
        # Specifies the model that the serializer should use to generate the serialized representation. This is the Book model that we imported earlier.
        model = Book
