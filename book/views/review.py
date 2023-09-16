from rest_framework import viewsets
from book.api.serializers import ReviewSerializer
from book.models import Review


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()