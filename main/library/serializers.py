from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'pdf']
        extra_kwargs = {
            'name': {'required': False, 'allow_blank': True},  # Allow blank name field
        }
