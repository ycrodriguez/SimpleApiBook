from rest_framework import viewsets
from book.api.serializers import ReaderSerializer
from book.models import Reader


class ReaderViewSet(viewsets.ModelViewSet):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()
