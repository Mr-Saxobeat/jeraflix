from django.urls import path
from movies.api import views

urlpatterns = [
    path('popular/', 
        views.ListPopularMoviesAPIView.as_view(),
        name='popular-movies'),

    path('search/',
        views.SearchMoviesAPIView.as_view(),
        name='search-movies'),

    path('watchlist/',
        views.UserWatchListAPIView.as_view(),
        name='watchlist'),

    path('watchedlist/',
        views.UserWatchedListAPIView.as_view(),
        name='watchedlist'),
]


