from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from articulate_app import utils

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


def response(data, code=status.HTTP_200_OK):
    return Response(data=data, status=code)


@api_view()
@cache_page(CACHE_TTL)
def about_page_view(request):
    return render(request, template_name="about.html")


class HomePageView(APIView):

    def get(self, request):
        if "article_home" in cache:
            return render(request, template_name="home.html", context={"data": cache.get("article_home")})
        data = utils.get_home_page()
        cache.set("article_home", data)
        return render(request, template_name="home.html", context={"data": data})


class SortPageView(APIView):

    def get(self, request):
        type = request.query_params.get("type")
        if type:
            if type == "1":
                if "hl" in cache:
                    return render(request, template_name="home.html", context={"data": cache.get("hl")})
                data = utils.get_high_to_low()
                cache.set("hl", data)
                return render(request, template_name="home.html", context={"data": data})
            elif type == "2":
                if "lh" in cache:
                    return render(request, template_name="home.html", context={"data": cache.get("lh")})
                data = utils.get_low_to_high()
                cache.set("lh", data)
                return render(request, template_name="home.html", context={"data": data})
            return response(data="Wrong type given", code=status.HTTP_400_BAD_REQUEST)
        return response(data="No type found in request", code=status.HTTP_400_BAD_REQUEST)


class MoviePageView(APIView):

    def get(self, request):
        article_id = request.query_params.get("article_id")
        if article_id:
            if "article_id:" + article_id in cache:
                return render(
                    request, template_name="moviedetail.html", context={"data": cache.get("article_id:" + article_id)}
                )
            error, data = utils.get_movie_data(article_id)
            if error:
                return response(data=error, code=status.HTTP_404_NOT_FOUND)
            cache.set("article_id" + article_id, data)
            return render(request, template_name="moviedetail.html", context={"data": data})
        return response("No article_id provided", status.HTTP_400_BAD_REQUEST)
