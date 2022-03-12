"""API v1 urls"""

#django
from django.urls import path, include

# django rest framework
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', include(('apps.api.users.urls', 'user_api'), namespace="user_api")),
    path('', include(('apps.api.books.urls', 'books_api'), namespace="books_api")),
]
