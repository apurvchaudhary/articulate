from rest_framework import serializers
from articulate_app.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer to serialize article all fields
    """
    class Meta:
        model = Article
        fields = ("id", "rating", "title", "type", "creatives", "review", "embed_link", "image", "imdb_rating")
