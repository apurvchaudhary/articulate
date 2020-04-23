from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from articulate_app.models import Article
from articulate_app.serializers import ArticleSerializer


def response(data, code=status.HTTP_200_OK):
    """
    Overrides rest_framework response
    :param data: data to be send in response
    :param code: response status code(default has been set to 200)
    :param error: error message(if any, not compulsory)
    """
    return Response(data=data, status=code)


def get_about_page(request):
    return render(request, template_name="about.html")


def get_home_page(request):
    articles = Article.objects.order_by("-created_at")
    article_serilizer = ArticleSerializer(articles, many=True)
    return render(request, template_name="home.html", context={"data" : article_serilizer.data})


def get_movie_page(request):
    article_id = request.query_params.get("article_id")
    article_obj = Article.objects.get(id=article_id)
    article_serializer = ArticleSerializer(article_obj)
    return render(request, template_name="moviedetail.html", context={"data" : article_serializer.data})


def get_sorted_data(request):
    type = request.query_params.get("type")
    if type == "1":
        articles = Article.objects.order_by("-rating", "-created_at")
        article_serilizer = ArticleSerializer(articles, many=True)
        return render(request, template_name="home.html", context={"data": article_serilizer.data})
    elif type == "2":
        articles = Article.objects.order_by("rating", "-created_at")
        article_serilizer = ArticleSerializer(articles, many=True)
        return render(request, template_name="home.html", context={"data": article_serilizer.data})
    else:
        return response(data="No type found in request", code=status.HTTP_400_BAD_REQUEST)
