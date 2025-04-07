from django.contrib import admin
from django.urls import path, include
from .views import get_all_books, add_books

urlpatterns = [
    path('books/', get_all_books, name='get-all-books'),
    path('books/add/', add_books, name='add-books'),
]
