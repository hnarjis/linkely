from django.contrib.auth.models import User
from rest_framework import serializers
from links.models import Article


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ["id", "url", "title", "date", "user"]
        read_only_fields = ["id", "title", "date", "user"]
