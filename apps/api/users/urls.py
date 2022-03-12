"""user api  urls"""

#django
from django.urls import path, include

# django rest framework
from rest_framework.routers import DefaultRouter

#views
from .views import users as user_views


router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
    path('change_password/', user_views.ChangePasswordView.as_view(),
         name='change-password'),
]
