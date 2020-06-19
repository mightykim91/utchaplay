<template>
  <div id="reviewitemmodify">
    <h3 class="text-white">리뷰 수정</h3>
    <div>
      <label for="title"></label>
      <input class="titleinput" v-model="reviewData.title" type="text" id="title">
    </div>
    <div class="form-group">
      <label for="exampleFormControlSelect1"></label>
        <p class="rankmsg">평점을 수정해주세요 :)</p>

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
      <textarea class="contentinput" v-model="reviewData.content" type="text" id="content"></textarea>
    </div>
    <button class="modifybtn" @click="modifyReview">수정완료</button>
  </div>

</template>

<script>
import axios from 'axios'
const BACKEND_URL='http://127.0.0.1:8000/'

export default {
    name:"ReviewItemModify",
    props:{
        // review:Object,
        id:Number,
    },
    data(){
        return{
            reviewData: {
                "title":null,
                "content":null,
                "rank":Number,
            },

        
        }
    },


    methods:{
        getReview(){
        axios.get(BACKEND_URL+'reviews/get_review/'+ this.id + '/')
            .then(response => {            
            this.reviewData = response.data
            })
        },
        modifyReview(){
            const config ={
                headers:{
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
            }
            axios.put(BACKEND_URL + 'reviews/modify/' + this.id + '/', this.reviewData, config)
                .then(() => {
                    alert('수정이 완료되었습니다 :)')
                    this.$router.go(-1)
                    // this.$router.push({ name: 'ReviewList' })
            })
        }

    },
    mounted(){
      this.getReview()
    }
    
}
</script>


<style>
#reviewitemmodify{
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
.modifybtn{
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