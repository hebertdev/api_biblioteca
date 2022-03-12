"""user serializer"""

#django
from django.contrib.auth import authenticate, password_validation

#django-rest-framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


#user & profile models 
from apps.users.models import User ,  Profile

#profile serializer
from apps.api.users.serializers.profiles import ProfileModelSerializer



class UserModelSerializer(serializers.ModelSerializer):

    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'is_manager',
            'profile',   
        )


        
class UserSignUpSerializer(serializers.Serializer):
    """user signup serializer"""
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        passwd = data['password']
        passwd2 = data['password_confirmation']

        if passwd != passwd2:
            raise serializers.ValidationError('Las contraseñas no coinciden')
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)

        usuario = User.objects.filter(username=user.username).first()
        token, created = Token.objects.get_or_create(user=usuario)
        
        return user , token.key


class UserLoginSerializer(serializers.Serializer):
    """user login serializer"""
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        # verified credentials
        user = authenticate(username=data['email'], password=data['password'])

        if not user:
            raise serializers.ValidationError('invalid credentials')

        self.context['user'] = user
        self.context['profile'] = user.profile
        return data

    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer for password change endpoint."""
    model = User
    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)