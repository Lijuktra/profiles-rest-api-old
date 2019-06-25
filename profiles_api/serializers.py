from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Test by Liju to test a name field for testing the APIView"""
    name = serializers.CharField(max_length=9)

class UserProfileSerializer(.Model)
