<template>
  <div>
    <!-- <button v-on:click="getMovieList">클릭!</button> -->
    <h1 v-if="!userId" class=my-5>인기상영작</h1>
    <h1 v-if="userId" class=my-5>{{username}} 님을 위한 추천영화</h1>
    <div class="container">
        <div 
        class='row ml-auto mr-auto movieList'
        v-if="!userId">
                <div class="col-3" v-for="movie in movieList" v-bind:key="movie.id">
                    <img v-bind:src="'https://image.tmdb.org/t/p/w185/'+ movie.poster_path " alt="posterUrl">
                </div>
        </div>
    </div>
    <!--포문테스트-->
    <!--여기까지-->
<div v-for="(value, name) in recommendations" v-bind:key="name" class="my-5 container">
    <h3 class="text-left"> {{ name }}</h3>
    <div class="container">
        <div class="row">
            <div class="col-3" v-for="movie in value" v-bind:key="movie.id">
                <img class="d-block w-100" v-bind:src="'https://image.tmdb.org/t/p/w185/' + movie.poster_path" >
            </div>
        </div>
    </div>
</div>

  </div>
</template>
<script>
import axios from 'axios'

const BACKEND_SERVER = 'http://127.0.0.1:8000/'

export default {
    data() {
        return {
            movieList: [],
            userId: null,
            isStaff: null,
            username: null,
            recommendations: null,
            
        }
    },
    methods: {
        getMovieList(){
            axios.get(BACKEND_SERVER + 'movies/')
            .then(response => {
                this.movieList = response.data
            })
        },
        getUserInfo(){
            const config = {
                headers:{
                    'Authorization' : `Token ${this.$cookies.get('auth-token')}`
                }
            }
            axios.get(BACKEND_SERVER + 'rest-auth/user/', config)
            .then(response => {
                console.log(response)
                this.userId = response.data.id
                this.isStaff = response.data.is_staff
                this.username = response.data.username
            })
        },
        getRecommendation(){
            const config = {
                headers:{
                    'Authorization' : `Token ${this.$cookies.get('auth-token')}`
                }
            }
            axios.get(BACKEND_SERVER + 'movies/recommendation/', config)
            .then(response => {
                console.log(response)
                this.recommendations = response.data
            })
        },
    },
    created(){
        this.getMovieList()
        this.getUserInfo()
        this.getRecommendation()
    },
    computed: {
        recom_genres: function() {
            return Object.keys(this.recommendations)
        }
    }

}
</script>

<style scoped>
* {
    color: white;
}

h3{
    margin-left: 16px;
}
</style>