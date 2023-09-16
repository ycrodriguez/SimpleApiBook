from rest_framework import viewsets
from book.api.serializers import AuthorSerializer
from book.models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
