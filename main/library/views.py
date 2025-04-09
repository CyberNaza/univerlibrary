from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from django.core.files.storage import default_storage
import os
from django.shortcuts import render
@api_view(['GET'])
def get_all_books(request):
    search_query = request.GET.get('search', '')  # get ?search= value
    books = Book.objects.all()
    
    if search_query:
        books = books.filter(name__icontains=search_query)  # case-insensitive search

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_books(request):
    if request.method == 'POST':
        # Check if any files are uploaded
        pdf_files = request.FILES.getlist('pdf_files')
        
        if not pdf_files:
            return Response({"error": "No files provided."}, status=400)

        created_books = []
        for pdf_file in pdf_files:
            # Save the uploaded PDF file to 'media/books_pdfs/'
            file_path = os.path.join('books_pdfs', pdf_file.name)
            file_name = default_storage.save(file_path, pdf_file)
            
            # Create a new Book entry with the saved file path
            book = Book(name=pdf_file.name, pdf=file_name)
            book.save()
            created_books.append(book)
        
        return Response({"message": "Books added successfully!", "books": [book.name for book in created_books]}, status=201)
    return Response({"error": "Invalid request"}, status=400)




def book_list_view(request):
    return render(request, 'index.html')