<template>
    <div class="modalitems">
        <a 
        data-toggle="modal"
        v-bind:data-target="dataTarget" 
        @click="validateLike">
            <!-- 모달 -->
            <figure  class="snip1273 scale">
                <img class="posterimg" 
                        v-bind:src="'https://image.tmdb.org/t/p/w342/'+ movie.poster_path "
                        alt="posterUrl">
            <figcaption>
                <div class="movietitleinfo">
                <h3 class="movietitle">{{ movie.title }}</h3>
                <small>상세정보 보기</small>
                </div>
            </figcaption>
            <a href="#"></a>
            </figure>
        <!-- 모달별 상세 내용 -->
        </a>
        <div class="modal fade" 
        :id="movieId" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">{{ movie.title }}</h5>
                <font-awesome-icon icon="heart" id="like-button" class="mt-1 ml-2" v-bind:style="{color: likeColor}"
                @click="like"/>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <img class="img-fluid poster-url" :src="'https://image.tmdb.org/t/p/w185/'+ movie.poster_path " alt="poster-url">
                <hr>
                <!-- <h3 class="badge badge-info">{{ users 평균평점 }}</h3> -->
                <h5 class="text-left text-bold">줄거리</h5>
                <p class="text-left" v-text="movie.overview"></p>
                <hr>
                <h5 class="text-left text-bold">댓글</h5>


                <!-- 댓글리스트 -->
                    
                <div class="commentlistarea">
                <ul class="commentlist form-row" v-for="(comment,index) in comments" :key="comment.id">
                    <div class="col-10"> <li  v-text="comment.content"></li></div>
                    <div class="col-2"><button type="button" class="close" aria-label="Close" v-if="comment.user == currentUser" @click="deleteComment(comment.id,index)"><span aria-hidden="true">&times;</span></button></div>
                    <hr>
                </ul>
                </div>
                <hr>
                <!-- 댓글 작성 -->
                <div class="form-row">
                    <div class="col-9">
                        <input @keypress.enter="createComment" placeholder="Leave a comment here." class="commentinput form-control" type="text" v-model="commentData.content" required>
                    </div>
                    <div class="col-3">
                        <button @click="createComment" class="btn btn btn-outline-light">댓글등록</button>
                    </div>
                </div>
        
            </div>

            <div class="modal-footer">
                <router-link :to="'/moviereview/'+movie.id"
                class="btn btn-outline-light"
                data-dismiss="modal"
                :movie="movie ">리뷰게시판</router-link>
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
const BACKEND_SERVER = 'http://127.0.0.1:8000/'
import axios from 'axios'

export default {
    name: 'MovieListItemModal',
    props: {
        movie: Object,
    },
    data(){
        return {
            commentData: {
                content: null,
                id:Number,
                movie_id:Number,
                user:Number,
            },
            comments: [],
            isLoggedIn: false,
            currentUser: null,
            likeColor: null,
        }
    },
    computed: {
        movieId() {
            return 'movie'+this.movie.id
        },
        dataTarget() {
            return `#movie${this.movie.id}`
        }
    },
    methods: {
        // mouseleave(){
        //     this.removeClass("hover");
        // },
        getComment() {
            axios.get(BACKEND_SERVER + 'movies/get_comments/' + this.movie.id +'/')
            .then(response => {
                this.comments = response.data
            }
        )
        },

        createComment() {
            const config={
                headers:{
                    'Authorization' : `Token ${this.$cookies.get('auth-token')}`
                }
            }
            if (this.isLoggedIn){
                if (this.commentData.content){
                    // 빈 댓글 입력안하기
                    axios.post(BACKEND_SERVER + 'movies/create_comment/' + this.movie.id + '/', this.commentData, config)
                    .then(response => {
                        this.comment = response.data
                        this.comments.unshift(this.comment)
                        // 작성후 없어지게하기
                        this.commentData.content=''
                    })
                }
            }else{
                alert('댓글을 작성하려면 로그인해주세요 :)')

                //모달창이 꺼지지 않은채로 로그인폼으로 이동해버림 ㅠㅠ
                // this.$router.push({name:'Login'}) 
                // this.dataTarget('hide')
                
            }
        },

        deleteComment(commentId,index){
            axios.delete(BACKEND_SERVER + 'movies/delete_comment/' + commentId + '/')
            .then(() => {
                alert('댓글이 삭제되었습니다 :)')
            })
            this.comments.splice(index, 1)
        },
        UserValidation() {
            const config = {
                headers:{
                    'Authorization' : `Token ${this.$cookies.get('auth-token')}`
                }
            }
            axios.get(BACKEND_SERVER + 'rest-auth/user/', config)
            .then(response=>{
                this.currentUser = response.data.id
                this.isLoggedIn = true
                }
            )
        },
        like() {
            const config = {
                headers:{
                    'Authorization' : `Token ${this.$cookies.get('auth-token')}`
                }
            }
            axios.post(BACKEND_SERVER + 'movies/like/' + this.movie.id + '/', null, config)
            .then(response=>{
                console.log(response.data.liked)
                if (response.data.liked === true) {
                    this.likeColor = 'crimson'
                } else {
                    this.likeColor = 'black'
                }
            })
        },
        validateLike() {
            const config = {
                headers:{
                    'Authorization' : `Token ${this.$cookies.get('auth-token')}`
                }
            }
            console.log(config)
            axios.get(BACKEND_SERVER + `movies/checklike/${this.movie.id}/`, config)
            .then(response => {
                console.log(response)
                if (response.data.liked === true) {
                    this.likeColor = 'crimson'
                } else {
                    this.likeColor = 'black'
                }
                
            })
        }
    },
    mounted(){
        this.getComment()
        // this.validateUser()
        this.UserValidation()
    },
    created(){
        // this.UserValidation()
        // this.getComment()
    },
}

</script>

<style scoped>
/* 모달별 스타일링 */
.btn-outline-light{
    border:1px solid #eae8e4;
    color: #eae8e4;
}
.btn-outline-light:hover{
    background-color: #eae8e4;
    color: #3B3632;

}
.modal-content{
    background-color: #313e46d9;
    /* opacity: 0.95; */
    color:white;

}
.modal-body>hr{
    /* background-color:white; */
    /* z-index : 1; */
}
.close{
    color:white;
}

.btn{
    border-radius: 40px;
}
.modalitems{
    margin:10px 10px;
}

.posterimg{
    border-radius: 3px;

}
.scale {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.5s ease-in-out;   /* 부드러운 모션을 위해 추가*/
}


.scale:hover {
  transform: scale(1.1);
  -webkit-transform: scale(1.1);
  -moz-transform: scale(1.1);
  -ms-transform: scale(1.1);
  -o-transform: scale(1.1);
}

.movietitleinfo{
    position:relative;
    top:150px;
    text-align: center;
}
.movietitle{
    font-size: 24px;
    
}

/* 포스터 hover효과 */
@import url(https://fonts.googleapis.com/css?family=Raleway:400,500,700);
.snip1273 {
  font-family: 'Raleway', Arial, sans-serif;
  position: relative;
  /* margin: 10px; */
  min-width: 300px;
  /* max-width: 310px; */
  width: 100%;
  color: #ffffff;
  text-align: left;
  background-color: #000000;
  font-size: 16px;
}
.snip1273 * {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all 0.4s ease-in;
  transition: all 0.4s ease-in;
}
.snip1273 img {
  position: relative;
  max-width: 100%;
  vertical-align: top;
}
.snip1273 figcaption {
  position: absolute;
  top: 0;
  right: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  opacity: 0;
  padding: 20px 30px;
}
.snip1273 figcaption:before,
.snip1273 figcaption:after {
  width: 1px;
  height: 0;
}
.snip1273 figcaption:before {
  right: 0;
  top: 0;
}
.snip1273 figcaption:after {
  left: 0;
  bottom: 0;
}
.snip1273 h3,
.snip1273 p {
  line-height: 1.5em;
}
.snip1273 h3 {
  margin: 0 0 5px;
  font-weight: 700;
  text-transform: uppercase;
}
.snip1273 p {
  font-size: 0.8em;
  font-weight: 500;
  margin: 0 0 15px;
}
.snip1273 a {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  z-index: 1;
}
.snip1273:before,
.snip1273:after,
.snip1273 figcaption:before,
.snip1273 figcaption:after {
  position: absolute;
  content: '';
  background-color: #ffffff;
  z-index: 1;
  -webkit-transition: all 0.4s ease-in;
  transition: all 0.4s ease-in;
  opacity: 0.8;
}
.snip1273:before,
.snip1273:after {
  height: 1px;
  width: 0%;
}
.snip1273:before {
  top: 0;
  left: 0;
}
.snip1273:after {
  bottom: 0;
  right: 0;
}
.snip1273:hover img,
.snip1273.hover img {
  opacity: 0.4;
}
.snip1273:hover figcaption,
.snip1273.hover figcaption {
  opacity: 1;
}
.snip1273:hover figcaption:before,
.snip1273.hover figcaption:before,
.snip1273:hover figcaption:after,
.snip1273.hover figcaption:after {
  height: 100%;
}
.snip1273:hover:before,
.snip1273.hover:before,
.snip1273:hover:after,
.snip1273.hover:after {
  width: 100%;
}
.snip1273:hover:before,
.snip1273.hover:before,
.snip1273:hover:after,
.snip1273.hover:after,
.snip1273:hover figcaption:before,
.snip1273.hover figcaption:before,
.snip1273:hover figcaption:after,
.snip1273.hover figcaption:after {
  opacity: 0.1;
}

/* 댓글기능 */

input::placeholder {
	color: #C3C3C3;
}

.close{
    line-height: 40px;
    vertical-align: middle;
}
.commentinput{
    background-color: #FAFAFA;
    /* width: 360px; */
    border:1.5px #C6C6C6;
}

.commentlist{
    list-style:none;
    text-align: left;
    padding:0px 10px;
    margin:0px;
    line-height: 30px;
    vertical-align: middle;

}
.commentlist>hr{
    border:0;
    height: 2px;
    background:white;
}
.commentlistarea{
    background-color: #4e5c6594;
    opacity: 0.8;
    border-radius: 4px;
    max-height: 200px;
    overflow: scroll;
    

}
</style>