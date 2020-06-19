<template>
    <!-- 리뷰작성 폼 -->
    <div id="createreview" class="createreviewform">
      <h3 class="text-white">리뷰 작성</h3>
      <div>
        <label for="title"></label>
        <input class="titleinput" v-model="reviewData.title" type="text" id="title" placeholder="리뷰 제목을 입력하세요">
      </div>

      <div class="form-group">
        <label  for="exampleFormControlSelect1"></label>
        <p class="rankmsg">평점을 선택해주세요 :)</p>
        <select v-model="reviewData.rank" class="rankinput form-control" id="exampleFormControlSelect1">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
        </select>
      </div>
      <div>
        <label for="content"></label>
        <textarea class="contentinput" v-model="reviewData.content" type="text" id="content" placeholder="내용을 입력하세요"></textarea>
      </div>
      <button class="createbtn" @click="createReview">작성</button>
    </div>

</template>

<script>
import axios from 'axios'
const BACKEND_URL='http://127.0.0.1:8000/'
export default {
    name:'CreateReview',
    data(){
      return{
        reviewData:{
          title:null,
          content:null,
          rank:Number,
        }
      }
    },
    props:{
      id:Number,
    },
    methods:{
      createReview(){
        const config ={
          headers:{
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
      axios.post(BACKEND_URL + 'reviews/create/' + this.id + '/', this.reviewData, config)
        .then(()=> {
          this.$router.push({ name: 'ReviewList' })
        })
      }
    }
}
</script>

<style scoped>

#createreview{
  margin: 70px;
}


/* 영화 리뷰 작성 */
.titleinput{
  font-weight: 400;
  width: 550px;
  padding: 10px 10px 10px 14px;
  border-radius: 7px 7px 0px 0px;
  border: none;
  height: 60px;
  background-color: #F7F4F0;
}

.rankinput{
  background-color: #F7F4F0;
  font-weight: 400;
  width: 550px;
  padding: 10px 10px 10px 14px;
  border-radius: 0px;
  height: 60px;
  border-top: 1px #C7C7C7;
  border-bottom: none;
  border-right: none;
  border-left: none;
}

select{
  margin:0px auto;
}

.contentinput{
  background-color: #F7F4F0;
  font-weight: 400;
  width: 550px;
  padding: 10px 10px 10px 14px;
  border-radius: 0px 0px 7px 7px;
  border: none;
  height: 150px;
}
.createbtn{
  background-color: rgb(252, 66, 106);
  color: rgb(255, 255, 255);
  font-weight: 700;
  letter-spacing: -0.1px;
  text-align: center;
  width: 550px;
  font-size: 16px;
  border-radius: 40px;
  border:none;
  height: 50px;
  margin-top: 20px;
}
.rankmsg{
  color: white;
  opacity: 0.8;
}

input::placeholder{
  color:#8C8C8C;
}
textarea::placeholder{
  color: #8C8C8C;
}
</style>