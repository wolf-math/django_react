from django.contrib.auth.models import User
from rest_framework import serializers
# import models
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password:": {"write_only": True}}

    def create(self, valideted_data):
        user = User.objects.create_user(**valideted_data)
        return user
    
# The model to be served as JSON
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}