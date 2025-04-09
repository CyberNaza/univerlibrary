from django.contrib import admin
from django.urls import path, include
from .views import get_books, add_books, book_list_view

urlpatterns = [
    path('books/', get_books, name='get-all-books'),
    path('books/add/', add_books, name='add-books'),
    path('books/list/', book_list_view, name='book-list'),
]
