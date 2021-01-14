<template>
  <div class="home">
    <div class="container">
      <h1>Filmes populares: </h1>
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
  name: "Home",
  components: {
      Movie
  },
  data() {
    return {
      movies: []
    }
  },
  methods: {
    getMovies() {
      let endpoint = "/api/movies/popular/";
      apiService(endpoint)
        .then(data => {
          this.movies.push(...data.results);
        })
    },
  },
  created() {
    this.getMovies();
  }
};
</script>
