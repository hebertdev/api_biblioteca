"""book api  urls"""

#django
from django.urls import path, include

# django rest framework
from rest_framework.routers import DefaultRouter

#views
from .views import books as book_views


router = DefaultRouter()
router.register(r'books', book_views.BookViewSet, basename="books")

urlpatterns = [
    path('', include(router.urls)),
]
