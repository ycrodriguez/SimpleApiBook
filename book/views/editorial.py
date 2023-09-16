from rest_framework import viewsets
from book.api.serializers import EditorialSerializer
from book.models import Editorial


class EditorialViewSet(viewsets.ModelViewSet):
    serializer_class = EditorialSerializer
    queryset = Editorial.objects.all()
