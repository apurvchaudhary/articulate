from django.urls import re_path
from articulate_app.views import HomePageView, MoviePageView, SortPageView, AboutPageView

urlpatterns = [
    re_path(r'^home/$', HomePageView.as_view(), name="home-page"),
    re_path(r'^movie/$', MoviePageView.as_view(), name="movie-page"),
    re_path(r'^sort/$', SortPageView.as_view(), name="sort-rating"),
    re_path(r'^about/$', AboutPageView.as_view(), name="about"),
]
