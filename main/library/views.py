from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"Failed to fetch books: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )