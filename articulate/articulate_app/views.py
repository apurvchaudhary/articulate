from rest_framework.views import APIView
from articulate_app import utils


class HomePageView(APIView):

    def get(self, request):
        return utils.get_home_page(request)


class MoviePageView(APIView):

    def get(self, request):
        return utils.get_movie_page(request)


class SortPageView(APIView):

    def get(self, request):
        return utils.get_sorted_data(request)


class AboutPageView(APIView):

    def get(self, request):
        return utils.get_about_page(request)
