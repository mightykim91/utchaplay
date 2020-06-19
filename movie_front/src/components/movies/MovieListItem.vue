<template>
  <div class="row ml-auto mr-auto">
        <MovieListItemModal :movie="movie" />
  </div>
</template>

<script>
import MovieListItemModal from './MovieListItemModal.vue'


export default {
    name:"MovieListItem",
    
    components:{
        MovieListItemModal,
    },
    props:{
      movie:Object,
    },
    computed:{
      dataTarget() {
        return `#movie${this.movie.id}`
      }
    }
}

</script>

<style>
.posterimg{
  width: 300px;
  height: 400px;
}
</style>