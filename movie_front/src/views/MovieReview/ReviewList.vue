<template>
  <div id="reviewlist">
    <h1 class="text-white">리뷰</h1>
    <div v-if="isLoggedIn">
      <div class="row">
        <div class="col-12">
          <button class="float-right btn btn btn-outline-light" @click="createReview">새로운 리뷰 작성</button><br>
        </div>
        <div class="col-12">
        <table class="table text-white">
          <thead>
            <tr>
              <th scope="col">No</th>
              <th scope="col">리뷰 제목</th>
              <th scope="col">작성자</th>
              <th scope="col">상세보기</th>
            </tr>
          </thead>
          
          <ReviewListItem :movieId="movieId" :movie="movie" :reviews="reviews"/>

          </table>
          </div>
        </div>
    </div>


  </div>
</template>

<script>
import axios from 'axios'
const BACKEND_URL = 'http://127.0.0.1:8000/'

import ReviewListItem from '../../components/reviews/ReviewListItem.vue'
export default {
    name:'ReviewList',
    components: {
      ReviewListItem,
    },
    props: {
      movie:Object,
      id: Number, //영화id
    },
    data(){
      return{
        // movie:Object,
        reviews:[],
        isLoggedIn:false,
        errorMessage:null,
        movieId:this.id,
      }
    },

    methods:{

      loginCheck() {
        if (this.$cookies.isKey('auth-token')){
          this.isLoggedIn = true
        } else{
          alert('로그인이 필요합니다 :)')
          this.$router.push({name:'Login'})
        }
        
      },

      setCookies(token){
        this.$cookies.set('auth-token',token)
        this.isLoggedIn=true
      },
      getReviews(){
        
        axios.get(BACKEND_URL + 'reviews/get_reviews/' + this.id )
          .then(response =>{
            console.log(response.data)
            this.reviews = response.data
          })
      },
      createReview(){
        this.$router.push({ name: 'CreateReview' ,params: {id:this.id}})
      }
    },
    mounted() {
      this.loginCheck()
      this.getReviews()

    }

}
</script>

<style scoped>

#reviewlist{
  margin: 70px 50px;
}

.btn-outline-light{
  border:2px solid;
  margin: 30px;
}

</style>