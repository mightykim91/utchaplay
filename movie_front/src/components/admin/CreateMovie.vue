<template>
  <div>
    <h1>새로운 영화 등록하기</h1>
    <form v-on:submit.prevent="createMovie">
      <div class="form-group">
        <label for="title">영화 제목</label>
        <input type="text" id="title" class="form-control bg-dark text-white" v-model="movieDetail.title" required>
      </div>
      <div class="form-group">
        <label for="original-title">원제목</label>
        <input type="text" id="original-title" class="form-control bg-dark text-white" v-model="movieDetail.original_title" required>
      </div>
      <div class="form-group">
        <label for="release-date">개봉일</label>
        <input type="date" id='release-date' class="form-control bg-dark text-white" v-model="movieDetail.release_date" required>
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
                v-model="movieDetail.genres_ids">
            </div>
          </div>
        </div>
      </div>
      
      <div class="form-group">
        <label for="adult">관람등급</label>
        <select class="form-control bg-dark text-white" v-model="movieDetail.adult" id="adult" required>
          <option disabled value="" class="text-white">관람등급을 선택해주세요.</option>
          <option v-for="option in adultOptions" 
          v-bind:key="option.id" 
          v-bind:value="option.value">
            {{ option.grade }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="overview">줄거리</label>
        <textarea id="overview" v-model="movieDetail.overview" 
        placeholder="줄거리를 입력해주세요"
        class="form-control bg-dark text-white" rows="5" required></textarea>
      </div>
      <div class="form-group">
        <label for="poster-path">포스터 url</label>
        <input type="text" id="poster-path"
        class="form-control bg-dark text-white" 
        v-model="movieDetail.poster_path">
      </div>
      <input type="submit" class="btn btn-primary" value="새로운영화 생성">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const BACKEND_URL = "http://127.0.0.1:8000/"

export default {
    name: 'CreateMovie',
    data() {
      return {
        movieDetail: {
          title: null,
          original_title: null, 
          release_date: null, 
          genres_ids: [], //require array
          adult: null, 
          overview: null, 
          poster_path: null,  
        },

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
      createMovie() {
        axios.post(BACKEND_URL + 'movies/add_movie/', this.movieDetail)
        .then(response=>{
          console.log(response.data)
          alert(response.data.title + '가 성공적으로 추가되었습니다.')
        })
        
      },
      getGenres() {
        axios.get(BACKEND_URL + 'movies/getgenres/')
        .then(response => {
          this.genres = response.data
          console.log(this.genres)
        })
      }
    },
    created(){
      this.getGenres()
    }
    
}
</script>

<style scoped>
h1 {
  color: white;
  font-family: 'Jua', sans-serif;
}


form {
  text-align: left;
  color: white;
  font-family: 'Jua', sans-serif;
}
</style>