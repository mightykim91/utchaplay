<template>
  <div class="home">
    <MovieList/>
  </div>
</template>

<script>
import MovieList from "../components/movies/MovieList.vue"


export default {
  name: 'Home',
  components: {
    MovieList,
  }
}
</script>
<style>

</style>
