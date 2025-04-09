from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from django.core.files.storage import default_storage
import os
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def get_books(request):
    # Get all books from the database
    books = Book.objects.all()
    
    # Serialize the book data to send it to the client
    serializer = BookSerializer(books, many=True)
    
    # Return the book data as JSON
    return Response(serializer.data, status=status.HTTP_200_OK)

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