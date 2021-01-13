import requests
from django.views.generic import base
from rest_framework.generics import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from movies.models import Movie
from movies.api.serializers import MovieSerializer

class ListPopularMoviesAPIView(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    api_key = 'b6be2efeb72ba2ee8e22040e88b8da53'

    def get_queryset(self):
        payloads = {'api_key': self.api_key, 'page': '1'}
        response = requests.get('https://api.themoviedb.org/3/movie/popular/',
                                params=payloads)
        response_json = response.json()
        list_of_tmdb_ids = []

        for movie in response_json['results']:
            movie_already_saved = Movie.objects.filter(tmdb_id=movie['id']).exists()
            if not movie_already_saved:
                Movie.objects.create(
                    tmdb_id=movie['id'],
                    title=movie['title']
                )

            list_of_tmdb_ids.append(movie['id'])

        queryset = Movie.objects.filter(tmdb_id__in=list_of_tmdb_ids)

        return queryset


class SearchMoviesAPIView(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['title']
    api_key = 'b6be2efeb72ba2ee8e22040e88b8da53'

    def get_queryset(self):
        queryset = Movie.objects.filter(title__icontains=self.request.GET['query'])

        if queryset.count() < 20:
            payloads = {'api_key': self.api_key, 'query': self.request.GET['query']}
            response = requests.get('https://api.themoviedb.org/3/search/movie/',
                                    params=payloads)
            response_json = response.json()
            list_of_tmdb_ids = []

            for movie in response_json['results']:
                movie_already_saved = Movie.objects.filter(tmdb_id=movie['id']).exists()
                if not movie_already_saved:
                    Movie.objects.create(
                        tmdb_id=movie['id'],
                        title=movie['title']
                    )

                list_of_tmdb_ids.append(movie['id'])

        queryset = Movie.objects.filter(tmdb_id__in=list_of_tmdb_ids)

        return queryset


class UserWatchListAPIView(generics.ListAPIView, generics.UpdateAPIView, base.ContextMixin):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    api_key = 'b6be2efeb72ba2ee8e22040e88b8da53'

    def get_queryset(self):
        profile_id = request.session['current-profile']
        profile = Profile.objects.get(pk=profile_id)
        queryset = profile.watch_list.all().order_by('title')
        return queryset

    def put(self, request):
        profile_id = request.session['current-profile']
        profile = Profile.objects.get(pk=profile_id)
        tmdb_id = self.request.POST['tmdb_id']

        try:
            movie = Movie.objects.get(tmdb_id=tmdb_id)
        except Movie.DoesNotExist:
            payloads = {'api_key': self.api_key }
            response = requests.get('https://api.themoviedb.org/3/search/movie/' + tmdb_id + '/',
                                    params=payloads)
            response_json = response.json()

            movie = Movie.objects.create(
                tmdb_id=response_json['id'],
                title=response_json['title']
            )


        movie_is_on_profile_watchlist = profile.watch_list.filter(tmdb_id=movie.tmdb_id).exists()

        if movie_is_on_profile_watchlist:
            profile.watch_list.remove(movie)
        else:
            profile.watch_list.add(movie)

        profile.save()
        serializer = self.serializer_class(profile.watch_list, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserWatchedListAPIView(generics.ListAPIView, generics.UpdateAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        profile_id = request.session['current-profile']
        profile = Profile.objects.get(pk=profile_id)
        queryset = profile.watched_list.all()
        return queryset

    def put(self, request):
        profile_id = request.session['current-profile']
        profile = Profile.objects.get(pk=profile_id)
        tmdb_id = self.request.POST['tmdb_id']
        
        try:
            movie = Movie.objects.get(tmdb_id=tmdb_id)
        except Movie.DoesNotExist:
            payloads = {'api_key': self.api_key }
            response = requests.get('https://api.themoviedb.org/3/search/movie/' + tmdb_id + '/',
                                    params=payloads)
            response_json = response.json()

            movie = Movie.objects.create(
                tmdb_id=response_json['id'],
                title=response_json['title']
            )

        movie_is_on_profile_watchedlist = profile.watched_list.filter(tmdb_id=movie.tmdb_id).exists()

        if movie_is_on_profile_watchedlist:
            print("existe")
            profile.watched_list.remove(movie)
        else:
            print("nao existe")
            profile.watched_list.add(movie)

        profile.save()
        serializer = self.serializer_class(profile.watched_list, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)




