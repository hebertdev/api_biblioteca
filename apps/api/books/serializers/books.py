"""book serializer"""

#django-rest-framework
from rest_framework import serializers

#book model
from apps.books.models import Book


class BookModelSerializer(serializers.ModelSerializer):
    """Book model serializer."""
    is_like = serializers.SerializerMethodField('verify_like_user')
    num_likes = serializers.SerializerMethodField('num_likes_book')

    def verify_like_user(self, book):
        if self.context:
            user = self.context['request'].user
            if not user.is_anonymous:
                return book.likes.filter(pk=self.context['request'].user.id).exists()
            else:
                return False
        else:
            return False

    def num_likes_book(self , book):
        if self.context:
            return book.likes.count()

    class Meta:
        """Meta class."""
        model = Book
        fields = ('id' , 'title' , 'author' , 'num_likes' , 'is_like' , 'edition' , 'publication_date' , 'cover' , 'quantity')       
        read_only_fields = (
            'id',
        )


class LikeBookSerialzier(serializers.ModelSerializer):
    """like book serializer"""
    class Meta:
        model = Book
        fields = (
            'id', 'likes'
        )

    def update(self, instance, data):
        """update model serializer"""
        book = self.context['book']
        user = self.context['user']

        if book.likes.filter(pk=self.context['user'].id).exists():
            book.likes.remove(user)
            return book
        else:
            book.likes.add(user)
            return book
