<template>
  <div>
        <h1 v-if="!movieToDelete">삭제를 원하는 영화를 선택해주세요</h1>
        <h1 v-if="movieToDelete" class="text-center">영화 삭제하기</h1>
        <select class="form-control bg-dark text-white" v-model="movieToDelete">
            <option v-for="movie in movies" :key="movie.id" :value="movie">
                {{ movie.title }}
            </option>
        </select><br>
        <button class="btn btn-primary float-right" v-if="movieToDelete" v-on:click="deleteMovie">삭제</button>
  </div>
</template>

<script>
import axios from 'axios'

const BACKEND_URL = "http://127.0.0.1:8000/"

export default {
    name: 'DeleteMovie',
    data() {
        return {
            movies: [],
            movieToDelete: null,
        }
    },
    methods: {
        getMovieList() {
            axios.get(BACKEND_URL + 'movies/')
            .then(response=>{
                this.movies = response.data
            })
        },
        deleteMovie() {
            const confimation = confirm(`${this.movieToDelete.title} 을 삭제하시겠습니까?`)
            if (confimation === true) {
                axios.delete(BACKEND_URL + `movies/delete_movie/${this.movieToDelete.id}/`)
                .then(response=>{
                    alert(`${response.data.title} 가 삭제되었습니다.`)
                })
                this.getMovieList()
            }
        }
    },
    created() {
        this.getMovieList()
    }
}
</script>

<style scoped>
* {
  font-family: 'Jua', sans-serif;
  color: white;
  text-align: left;
}
</style>