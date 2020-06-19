<template>
  <div id="reviewitemdetail">
      <div class="jumbotron">
        <div class="row justify-content-center">
            <!-- <div class="col-1"> -->
            <h5 class="badge badge-pill badge-light user_name">{{ review.user.username }}님의 리뷰</h5>
            <!-- </div>/ -->
            <!-- <div class="col-1">/ -->
            <span class="badge badgerank rankbadge-info">{{ review.rank }}</span>
            <!-- </div> -->
        </div>
        <h1 class="display-4">{{ review.title }}</h1>
        <p class="lead">{{ review.content }}</p>
        

        <hr>
        <small>작성시간 : {{ review.created_at}}</small><br>
        <small>수정시간 : {{ review.updated_at}}</small>
        <div v-if="review.user.id == currentUser">
            <br>
            <span><button class="btn btn-outline-info my-2 my-sm-0" @click="modifyReview(review)" type="button">글수정</button></span>
            <span><button class="btn btn-outline-info my-2 my-sm-0" @click="deleteReview(movieId)" type="button">글삭제</button></span>
        </div>
        
        <hr class="my-4">
        <!-- 댓글리스트 -->
          <div>
            <h5 class="text-left">댓글</h5>
            <hr>
                <p class="text-muted" v-if="comments.length === 0">작성된 댓글이 없습니다 :(</p>
                <div class="commentlistarea">
                    <ul class="commentlist form-row" v-for="(comment,index) in comments" :key="comment.id">
                        <div class="col-10"><li v-text="comment.content"></li></div>
                        <div class="col-2"><button type="button" class="close" aria-label="Close" v-if="comment.user == currentUser" @click="deleteComment(comment.id,index)"><span aria-hidden="true">&times;</span></button></div>
                    </ul>
                </div>
            </div>
            <hr class="my-4">

            <!-- 댓글 작성 -->
            <div class="form-row">
                <div class="col-10">
                    <input @keypress.enter="createComment" v-model="commentData.content" class="commentinput form-control mr-sm-2" type="text" placeholder="Leave a comment here.">
                </div>
                <div class="col-2">
                <button class="btn btn-outline-info my-2 my-sm-0" @click="createComment" type="button">댓글 작성</button>
                </div>
            </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
const BACKEND_URL='http://127.0.0.1:8000/'

export default {
    name: "ReviewItemDetail",
    props:{
        id:Number,
        movieId:Number,
    },
    data(){
        return{
          review:{
              "title":null,
              "cotent":null,
              "id":Number,
              "rank":Number,
              "created_at":null,
              "updated_at":null,
              "user":{
                  "id":Number,
                  "username":null,
              }
          },
          commentData: {
                content: null,
                id:Number,
                movie_id:Number,
                user:Number,
          },
          comments: [],

          userValidation: false,
          currentUser: null,

        }
    },

    methods:{
        getReview(){
        axios.get(BACKEND_URL+'reviews/get_review/'+ this.id + '/')
            .then(response => {            
            this.review = response.data
            })
        },
        createComment() {

        const config={
            headers:{
                'Authorization' : `Token ${this.$cookies.get('auth-token')}`
            }
        }
        if (this.commentData.content){
            axios.post(BACKEND_URL + 'reviews/create_comment/' + this.id+ '/', this.commentData, config)
                
                .then(response => {
                console.log(response.data)
                this.comment = response.data
                this.comments.unshift(this.comment)
                this.commentData.content=''
                })
            }

        },
        modifyReview(data) {
            this.$router.push({ name:'ReviewItemModify', params:{ review:data}})
        },
        deleteReview() {
            axios.post(BACKEND_URL + 'reviews/delete/' + this.id+ '/')
                .then(() => {
                    alert('게시물 삭제가 완료되었습니다 :)')
                    this.$router.go(-1)
                    // this.$router.push({ name: 'ReviewList'})
                })
      },
      getComment() {
    
        axios.get(BACKEND_URL + 'reviews/get_comments/' + this.id +'/')
            .then(response => {
                this.comments = response.data
            })
      },
      validateUser() {
          const config = {
            headers:{
                'Authorization' : `Token ${this.$cookies.get('auth-token')}`
            }
        }
          axios.get(BACKEND_URL + 'rest-auth/user/', config)
          .then(response=>{
              if (response.data.username === this.review.user.username) {
                  this.userValidation = true
              }
          })
        },
        deleteComment(commentId,index){
                    console.log(this.commentData.id)
        axios.delete(BACKEND_URL + 'reviews/delete_comment/' + commentId + '/')
            .then(() => {
                alert('댓글이 삭제되었습니다 :)')

            })
        this.comments.splice(index, 1)
        },
        commentUserValidation() {
            const config = {
                headers:{
                    'Authorization' : `Token ${this.$cookies.get('auth-token')}`
                }
            }
            axios.get(BACKEND_URL + 'rest-auth/user/', config)
            .then(response=>{
                this.currentUser = response.data.id
                }
            )
        }
    },


    mounted(){
      this.getReview()
      this.getComment()
      this.validateUser()
      this.commentUserValidation()
    },
    created() {
        // this.validateUser()
        // this.commentUserValidation()
    }
}
</script>

<style scoped>

#reviewitemdetail{
    margin: 70px 70px;
}
.jumbotron{
    background-color: #F7F4F0;
}

.user_name{
  font-size: 20px;
  margin: 0 0 50px 0;
  height: 50px;
  padding: 0px 10px;
  line-height: 50px;
  vertical-align: middle;
  background-color:#E2DACE;
}
.badgerank{
    font-size: 30px;
    background-color: #417378;
    vertical-align: middle;
    line-height: 40px;
    height: 50px;
    margin:0px 10px;
    border-radius: 20px;
    color:white;
    /* bottom: 20px; */
    /* float: right; */
}
/* 댓글기능 */
input::placeholder {
	color: #C3C3C3;
}

.commentinput{
    background-color: #c5bcb542;
    /* width: 360px; */
    border:1.5px #C6C6C6;
}

.commentlist{
    list-style:none;
    text-align: left;
    padding:0px 10px;
    margin:0px;
    line-height: 40px;
    vertical-align: middle;
}
.close{
    line-height: 40px;
    vertical-align: middle;
}
.commentlist>hr{
    border:0;
    height: 2px;
    background:white;
}
.commentlistarea{
    background-color: #e2dace;
    opacity: 0.8;
    border-radius: 4px;
    max-height: 180px;
    overflow: scroll;
    
}
.btn-outline-info{
    border:1px solid #417378;
    color:#417378;
}
.btn-outline-info:hover{
    background-color: #417378;
    color:white;
}

</style>