"""book serializer"""

#django-rest-framework
from rest_framework import serializers

#book model
from apps.books.models import Book


class BookModelSerializer(serializers.ModelSerializer):
    """Book model serializer."""
    class Meta:
        """Meta class."""
        model = Book
        fields = '__all__'       
        read_only_fields = (
            'id',
        )






