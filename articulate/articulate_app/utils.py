from django.db.models import ObjectDoesNotExist

from articulate_app.models import Article
from articulate_app.serializers import ArticleSerializer


def get_home_page():
    articles = Article.objects.order_by("-created_at")
    article_serilizer = ArticleSerializer(articles, many=True)
    return article_serilizer.data


def get_movie_data(article_id):
    try:
        article_obj = Article.objects.get(id=article_id)
        article_serializer = ArticleSerializer(article_obj)
        return None, article_serializer.data
    except ObjectDoesNotExist:
        return f"No article found with this id : {article_id}", None


def get_high_to_low():
    articles = Article.objects.order_by("-rating", "-created_at")
    article_serilizer = ArticleSerializer(articles, many=True)
    return article_serilizer.data


def get_low_to_high():
    articles = Article.objects.order_by("rating", "-created_at")
    article_serilizer = ArticleSerializer(articles, many=True)
    return article_serilizer.data
