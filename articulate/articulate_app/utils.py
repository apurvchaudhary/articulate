from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from articulate_app.models import Article
from articulate_app.serializers import ArticleSerializer
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def response(data, code=status.HTTP_200_OK):
    """
    Overrides rest_framework response
    :param data: data to be send in response
    :param code: response status code(default has been set to 200)
    :param error: error message(if any, not compulsory)
    """
    return Response(data=data, status=code)


@cache_page(CACHE_TTL)
def get_about_page(request):
    return render(request, template_name="about.html")


def get_home_page(request):
    if "home" in cache:
        data = cache.get("home")
        return render(request, template_name="home.html", context={"data": data})
    articles = Article.objects.order_by("-created_at")
    article_serilizer = ArticleSerializer(articles, many=True)
    data = article_serilizer.data
    cache.set("home", data)
    return render(request, template_name="home.html", context={"data" : data})


def get_movie_page(request):
    article_id = request.query_params.get("article_id")
    if article_id in cache:
        data = cache.get(article_id)
        return render(request, template_name="moviedetail.html", context={"data": data})
    article_obj = Article.objects.get(id=article_id)
    article_serializer = ArticleSerializer(article_obj)
    data = article_serializer.data
    cache.set(article_id, data)
    return render(request, template_name="moviedetail.html", context={"data" : data})


def get_sorted_data(request):
    type = request.query_params.get("type")
    if type == "1":
        if "hl" in cache:
            data = cache.get("hl")
            return render(request, template_name="home.html", context={"data": data})
        articles = Article.objects.order_by("-rating", "-created_at")
        article_serilizer = ArticleSerializer(articles, many=True)
        data = article_serilizer.data
        cache.set("hl", data)
        return render(request, template_name="home.html", context={"data": data})
    elif type == "2":
        if "lh" in cache:
            data = cache.get("lh")
            return render(request, template_name="home.html", context={"data": data})
        articles = Article.objects.order_by("rating", "-created_at")
        article_serilizer = ArticleSerializer(articles, many=True)
        data = article_serilizer.data
        cache.set("lh", data)
        return render(request, template_name="home.html", context={"data": data})
    else:
        return response(data="No type found in request", code=status.HTTP_400_BAD_REQUEST)
