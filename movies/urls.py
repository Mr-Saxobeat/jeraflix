from django.urls import path
from movies.api import views

urlpatterns = [
    path('popular/', 
        views.PopularMoviesAPIView.as_view(),
        name='popular-movies'),
]