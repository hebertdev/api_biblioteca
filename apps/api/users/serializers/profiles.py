"""profile serializer"""

#django-rest-framework
from rest_framework import serializers

#user & profile model
from apps.users.models import User, Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""
    class Meta:
        """Meta class."""

        model = Profile
        fields = (
            'id',
            'avatar',
        )
        read_only_fields = (
            'user',
            'id',
        )






