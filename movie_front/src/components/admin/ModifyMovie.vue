<template>
  <div id="modify">
    <h1 v-if="!movieToModify">수정을 원하는 영화를 선택해주세요</h1>
    <h1 v-if="movieToModify" class="text-center">영화 수정하기</h1>
    <hr v-if="movieToModify" class="bg-white">
    <h5 v-if="movieToModify">현재 선택된 영화</h5>
    <select class="form-control bg-dark text-white" v-model="movieToModify">
        <option v-for="movie in movies" :key="movie.id" :value="movie">
            {{ movie.title }}
        </option>
    </select><br>
    <div v-if="movieToModify">
        <h4>현재 수정중인 영화: {{ movieToModify.title }}</h4>
        <hr class="bg-white">
        <form v-on:submit.prevent="modifyMovie">
            <div class="form-group">
                <label for="title">영화 제목</label>
                <input type="text" id="title" v-model="dataToModify.title" class="form-control bg-dark text-white">
            </div>
            <div class="form-group">
                <label for="original-title">영화 원제목</label>
                <input type="text" id="original-title" 
                class="form-control  bg-dark text-white"
                v-model="dataToModify.original_title">
            </div>
            <div class="form-group">
                <label for="release-date">개봉일</label>
                <input type="date" id='release-date' 
                class="form-control  bg-dark text-white"
                v-model="dataToModify.release_date"><br>
            </div>
            <div class="form-group">
                <label for="genre">장르선택</label><br>
                <div class="container border">
                    <div class="row">
                        <div class="form-check border col-3 d-flex justify-content-between bg-dark text-white" v-for="genre in genres" v-bind:key="genre.id">
                        <label v-bind:for="genre.genre_name">{{ genre.genre_name}}</label>
                        <input type="checkbox"
                            v-bind:id="genre.genre_name"  
                            v-bind:value="genre.id"
                            v-model="dataToModify.genres_ids">
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="form-group">
                <label for="adult">관람등급</label>
                <select class="form-control bg-dark text-white" v-model="dataToModify.adult" id="adult" required>
                    <option disabled class="bg-dark text-white" value="">관람등급을 선택해주세요.</option>
                    <option v-for="option in adultOptions" 
                    v-bind:key="option.id" 
                    v-bind:value="option.value">
                        {{ option.grade }}
                    </option>
                </select>
            </div>
            <div class="form-group">
                <label for="overview">줄거리</label>
                <textarea id="overview" v-model="dataToModify.overview"
                class="form-control bg-dark text-white"
                rows="5"
                ></textarea>
            </div>
            <div class="form-group">
                <label for="poster-path">포스터 url</label>
                <input type="text" id="poster-path" 
                class="form-control bg-dark text-white"
                v-model="dataToModify.poster_path">
            </div>
            <input type="submit" class="btn btn-primary" value="수정하기"><br>
    </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const BACKEND_URL = "http://127.0.0.1:8000/"

export default {
    name: 'ModifyMovie',
    data() {
        return {
            movies: [],
            movieToModify: null,
            dataToModify: null,
            adultOptions: [
                { grade: '18' , value: true},
                { grade: '15' , value: false},
                { grade: '12' , value: false},
                { grade: '전체관람가' , value: false},
            ],
            genres: []
        }
    },
    methods: {
        getMovieList() {
            axios.get(BACKEND_URL + 'movies/')
            .then(response=>{
                this.movies = response.data
            })
        },
        modifyMovie() {
            axios.put(BACKEND_URL + 'movies/modify_movie/' + `${this.movieToModify.id}/`, this.dataToModify)
            .then(response=>{
                alert(`${response.data.title} 의 정보가 성공적으로 수정되었습니다.`)
            })
            this.getMovieList()
        },
        getGenres() {
            axios.get(BACKEND_URL + 'movies/getgenres/')
            .then(response => {
            this.genres = response.data
            console.log(this.genres)
            })
            
        },
    },
    created() {
        this.getMovieList()
        this.getGenres()
    },
    watch:{
        movieToModify: function() {
            const originalData = {
                title: this.movieToModify.title,
                original_title: this.movieToModify.original_title, 
                release_date: this.movieToModify.release_date, 
                genres_ids: this.movieToModify.genres_ids, //require array
                adult: this.movieToModify.adult, 
                overview: this.movieToModify.overview, 
                poster_path: this.movieToModify.poster_path,  
            }
            this.dataToModify = originalData
        }
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