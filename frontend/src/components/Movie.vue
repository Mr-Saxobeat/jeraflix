<template>
  <div class="mt-2">
      <div class="container card-body">
          {{ movie.title }}
          <button 
            @click="removeFromWatchList(movie)"
            v-if="movie.is_on_my_watchlist"
          >Remover da Minha Lista
          </button>

          <button
            @click="addToWatchList(movie)"
            v-else
          >Adicionar à Minha Lista
          </button>

          <button
            @click="removeFromWatchedList(movie)"
            v-if="movie.watched"
            >Desmarcar assistido
          </button>

          <button 
            @click="addToWatchedList(movie)"
            v-else
          >Marcar assistido
          </button>
      </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service"
export default {
  name: "Movie",
  props: {
      movie: {
          type: Object,
          required: true,
      }
  },
  methods: {
    addToWatchList(movie) {
      var data = { "tmdb_id": movie.tmdb_id, "title": "" };
      console.log(data);
      var response = apiService("/api/movies/watchlist/", "PUT", data)
        .then(console.log(response));
      movie.is_on_my_watchlist = true;
    },
    removeFromWatchList(movie) {
      var data = { "tmdb_id": movie.tmdb_id, "title": "" };
      console.log(data);
      var response = apiService("/api/movies/watchlist/", "PUT", data)
        .then(console.log(response));
      movie.is_on_my_watchlist = false;
    },

    addToWatchedList(movie) {
      var data = { "tmdb_id": movie.tmdb_id, "title": "" };
      console.log(data);
      var response = apiService("/api/movies/watchedlist/", "PUT", data)
        .then(console.log(response));
      movie.watched = true;
    },
    removeFromWatchedList(movie) {
      var data = { "tmdb_id": movie.tmdb_id, "title": "" };
      console.log(data);
      var response = apiService("/api/movies/watchedlist/", "PUT", data)
        .then(console.log(response));
      movie.watched = false;
    }
  }
}
</script>

<style>

</style>
