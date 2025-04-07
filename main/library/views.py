from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import status

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
        pdf_files = request.data 
        
        if not pdf_files:
            return Response({"error": "No files provided."}, status=400)

        created_books = []
        for pdf_file in pdf_files:
            file_name = pdf_file.get('pdf')
            if file_name:
                book = Book(name=file_name, pdf=file_name)
                book.save()
                created_books.append(book)
        
        return Response({"message": "Books added successfully!", "books": [book.name for book in created_books]}, status=201)
    return Response({"error": "Invalid request"}, status=400)