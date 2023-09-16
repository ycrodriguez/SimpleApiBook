from rest_framework import viewsets
from book.api.serializers import GenderSerializer
from book.models import Gender


class GenderViewSet(viewsets.ModelViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()
