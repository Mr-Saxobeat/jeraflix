<template>
  <div class="home">
    <div class="container">
      <h1>Busca: </h1>
      <form @submit.prevent="searchMovies">
          <input v-model="query" type="text">
          <button type="submit">Buscar</button>
      </form>
      <div v-for="movie in movies"
           :key="movie.tmdb_id">
        <Movie :movie="movie" :key="movie.tmdb_id"></Movie>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service"
import Movie from "../components/Movie"
export default {
  name: "Search",
  components: {
      Movie
  },
  data() {
    return {
        movies: [],
      query: null,
    }
  },
  methods: {
    searchMovies() {
        this.movies = [];
        let endpoint = "/api/movies/search/?query=" + this.query;
        apiService(endpoint)
            .then(data => {
            this.movies.push(...data.results);
        })
    },
  },
};
</script>
