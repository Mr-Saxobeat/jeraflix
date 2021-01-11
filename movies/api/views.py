import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.api.serializers import MovieSerializer

class PopularMoviesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        payloads = {'api_key': 'b6be2efeb72ba2ee8e22040e88b8da53', 'page': '1'}
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
        serializer = MovieSerializer(queryset, many=True)

        return Response(serializer.data)


class SearchMovieAPIView(APIView):
    pass

