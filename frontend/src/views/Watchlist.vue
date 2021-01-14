<template>
  <div>
    <div class="container">
      <h1>Minha lista: </h1>
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
  name: "Watchlist",
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
      let endpoint = "/api/movies/watchlist/";
      apiService(endpoint)
        .then(data => {
          this.movies.push(...data.results)
        })
    },
  },
  created() {
    this.getMovies()
  }
};
</script>
