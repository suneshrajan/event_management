"""Module imports"""
# pylint: disable=E0401, R0205, R0903
from rest_framework import serializers
from apps.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer
    """

    class Meta(object):
        """
        Inner Meta class
        """

        model = User
        fields = ["id", "first_name", "last_name", "password", "email"]


class UserProfileSerializer(serializers.ModelSerializer):
    """
    UserProfile Serializer
    """

    class Meta(object):
        """
        Inner Meta class
        """

        model = User
        fields = ["id", "first_name", "last_name", "email"]
