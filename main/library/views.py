from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Book
from .serializers import BookSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class BookListView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="name",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                description="Optional book name"
            ),
            openapi.Parameter(
                name="pdf",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                description="PDF file",
                required=True
            ),
        ],
        operation_description="Upload a new book PDF"
    )
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
