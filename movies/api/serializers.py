from rest_framework import serializers
from movies.models import Movie
from accounts.models import Profile


class MovieSerializer(serializers.ModelSerializer):
    is_on_my_watchlist = serializers.SerializerMethodField(read_only=True)
    watched = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_is_on_my_watchlist(self, instance):
        the_request = self.context.get('request') 
        profile_id = the_request.session['current-profile']
        profile = Profile.objects.get(pk=profile_id)
        return profile.watch_list.filter(tmdb_id=instance.tmdb_id).exists()

    def get_watched(self, instance):
        the_request = self.context.get('request') 
        profile_id = the_request.session['current-profile']
        profile = Profile.objects.get(pk=profile_id)
        return profile.watched_list.filter(tmdb_id=instance.tmdb_id).exists()


