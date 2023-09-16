from rest_framework import viewsets
from book.api.serializers import BookSerializer
from book.models import Book


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
