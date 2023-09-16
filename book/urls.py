from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from rest_framework import routers
from book.views import *

router = routers.DefaultRouter()
router.register(r'author', AuthorViewSet, 'author')
router.register(r'book', BookViewSet, 'book')
router.register(r'editorial', EditorialViewSet, 'editorial')
router.register(r'gender', GenderViewSet, 'gender')
router.register(r'reader', ReaderViewSet, 'reader')
router.register(r'review', ReviewViewSet, 'review')

urlpatterns = [
    path('doc/', include_docs_urls(title='Simple API Rest Book')),
    path('book/', include(router.urls))
]
