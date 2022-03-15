"""book views"""
from rest_framework import viewsets , filters

#django rest framework
from rest_framework import mixins, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from django_filters.rest_framework import DjangoFilterBackend


#custom permission
from apps.api.books.permissions.books import IsManager



#models
from apps.books.models import Book

#serializers
from apps.api.books.serializers import (BookModelSerializer , LikeBookSerialzier) 


class BookViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
                  
    queryset = Book.objects.all().order_by('-created')
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter , filters.OrderingFilter , DjangoFilterBackend]
    search_fields = ['title' , 'author' , 'edition' , 'quantity' , 'publication_date']
    ordering_fields = ['publication_date']
    filterset_fields = {
        'title':['contains'],
        'author':['contains'],
        'publication_date':['contains'],
    }
    

    def get_permissions(self):
        permissions = [IsAuthenticated]
        if self.action in ['update' , 'partial_update' , 'destroy']:
            permissions.append(IsManager)
        return [p() for p in permissions]

    def get_serializer_context(self):
        context = super(BookViewSet , self).get_serializer_context()
        return context

    def get_serializer_class(self):
        if self.action == 'likes':
            return LikeBookSerialzier
        return BookModelSerializer

    #action para editar , tambien se puede sobreescribir el metodo Update del mixin    
    @action(detail=True, methods=['put', 'patch'])
    def edit_book(self, request, *args, **kwargs):
        book = self.get_object()
        partial = request.method == 'PATCH'
        serializer = BookModelSerializer(
            book,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = BookModelSerializer(book , context={'request': request}).data
        return Response(data)

    @action(detail=True, methods=['delete'])
    def delete_book(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def likes(self, request, *args, **kwargs):
        book = self.get_object()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(
            book,
            data={'user': request.user},
            context={'book':
                     book, 'user': request.user},
        )

        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        data = BookModelSerializer(book).data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def favorite_books(self, request , *args , **kwargs):
        user = request.user
        books = user.likes.all().order_by('-created')
        data = {
            'books':BookModelSerializer(books , many=True , context={'request':request} ).data
        }
        return Response(data)



