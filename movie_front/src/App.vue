<template>
  <div id="app">
        <nav class="navbar navbar-expand-sm navbar-dark">
            <router-link to="/" class="logo navbar-brand">읏챠 플레이</router-link>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarNavDropdown">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item active">
                        <router-link class="homebtn nav-link" to="/">Home</router-link> 
                    </li>

                    <li class='nav-item dropdown'>
                        <!-- <a href="#"> -->
                        <button class="btn btn-secondary nav-link dropdown-toggle" type="button" id="#navbarNavDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        장르별 탐색
                        </button>
                        <!-- </a> -->
                        <div class="dropdown-menu" aria-labelledby="navbarNavDropdown">
                            <router-link class="dropdown-item" v-for="genre in genres"
                            v-bind:key="genre.id"
                            :to="{ name: 'MovieListGenre', params: {id: `${genre.id}` } }">{{genre.name}}<br></router-link>
                        </div>
                    </li>
                    <li class='nav-item active' v-if="!isLoggedIn">
                        <router-link style="color:black;" class="nav-link btn btn-light" :to="{ name:'Signup' }">회원가입</router-link> 
                    </li>
                    <li class='nav-item active' v-if="!isLoggedIn">
                        <router-link style="color:black;" class="nav-link btn btn-light" :to="{ name:'Login' }">로그인</router-link>
                    </li>
                    <li class='nav-item active' v-if="isLoggedIn">
                        <router-link  style="color:black;" class="nav-link btn btn-light" to="/accounts/logout" @click.native="logout">로그아웃</router-link>
                    </li>
                </ul>
    </div>
    <router-link class="btn btn-light" style="color:black;" v-if="isAdmin" to="/adminpage/" >관리자 페이지</router-link>  
  </nav>
    <router-view @save-signup-data="signup" @save-login-data="login" />
</div>
    

</template>
<script>
import axios from 'axios'
const BACKEND_URL = "http://127.0.0.1:8000/"

export default {
  
  data() {
    return {
      genres: [
        {
          "id": 28,
          "name": "액션"
        },
        {
          "id": 12,
          "name": "모험"
        },
        {
          "id": 16,
          "name": "애니메이션"
        },
        {
          "id": 35,
          "name": "코미디"
        },
        {
          "id": 80,
          "name": "범죄"
        },
        {
          "id": 99,
          "name": "다큐멘터리"
        },
        {
          "id": 18,
          "name": "드라마"
        },
        {
          "id": 10751,
          "name": "가족"
        },
        {
          "id": 14,
          "name": "판타지"
        },
        {
          "id": 36,
          "name": "역사"
        },
        {
          "id": 27,
          "name": "공포"
        },
        {
          "id": 10402,
          "name": "음악"
        },
        {
          "id": 9648,
          "name": "미스터리"
        },
        {
          "id": 10749,
          "name": "로맨스"
        },
        {
          "id": 878,
          "name": "SF"
        },
        {
          "id": 10770,
          "name": "TV 영화"
        },
        {
          "id": 53,
          "name": "스릴러"
        },
        {
          "id": 10752,
          "name": "전쟁"
        },
        {
          "id": 37,
          "name": "서부"
        }
      ],
      isLoggedIn: false,
      isAdmin: false,
      loginData: null,
        errorMessage:null,
  
    }
  },
  methods:{
    setCookies(token) {
      this.$cookies.set('auth-token', token)
      this.isLoggedIn = true
    },

    signup(signupData) {
      console.log(signupData)
      axios.post(BACKEND_URL + 'rest-auth/signup/', signupData)
      .then(response => {
        console.log(response.data.key)
        this.setCookies(response.data.key)
        this.$router.push({ name: 'Home'})
      
      })
      .catch((err) => {
          this.errorMessage = err.response.data
          console.log(this.errorMessage)
            if(this.errorMessage.username){
                alert('사용자 이름을 확인하세요 :(')
            }if (signupData.password1 !== signupData.password2){
                alert('비밀번호가 일치하지 않습니다 :(')
            }if ((signupData.password1).length < 8) {
                alert('비밀번호는 8자리 이상 입력해주세요 :(')
            }if ((signupData.password1).length >= 8) {
                alert('비밀번호가 너무 일상적입니다 :(')
            }
      })
    },
    login(loginData) {
      axios.post(BACKEND_URL + 'rest-auth/login/', loginData)
      .then(response => {
        this.setCookies(response.data.key)
        this.$router.push({ name: 'Home'})
      })
      .catch(() => {
          alert('아이디와 비밀번호를 확인하세요 :(')
      })
    },
    
    logout() {
      const config = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(BACKEND_URL + 'rest-auth/logout/', null, config)
      .then(() => {
        this.$cookies.remove('auth-token')
        this.isLoggedIn = false
        this.isAdmin = false

        this.$router.push({ name: 'Home' })
      })
      .catch(() => {
        console.log('ERROR')
      })
    }
  },
  mounted() {
    this.isLoggedIn = this.$cookies.isKey('auth-token')
  },

  watch: {
    isLoggedIn: function() {
      if (this.isLoggedIn === true) {
        const config = {
          headers: {
            'Authorization': `Token ${this.$cookies.get('auth-token')}`
          }
        }
        axios.get(BACKEND_URL + "rest-auth/user/", config)
        .then(response => {
          this.isAdmin = response.data.is_staff
        })
      }
    }
  }
}
</script>






<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: 'Jua', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.logo{
    font-weight: 900;
    font-size: 27px;
}
.dropdown-menu>a{
    color:white;
}
nav{
    height: 90px;
}
.homebtn{
    color:white;
    font-weight: 900;
    font-size:40;
}

nav>ul{
    display: flex;
    /* align-items:; */
    justify-content: space-around;
}
nav.navitem{
    text-decoration: none;
    color:white;
    margin:0px 10px;
}
.nav-link.btn{
    margin:0px 5px;
    font-size:40;
}
nav{
    background-color: #000000;
}
.dropdown{
    text-align: right;
}
.dropdown-menu{
    background-color:rgb(20, 21, 23);
    position: absolute;
    /* left: -1px; */
    /* z-index: 999; */
    /* box-sizing: content-box; */
    /* left:20px; */
    width: 70%;
    max-height: 18.75vw;
    border-bottom-right-radius: 2px;
    border-bottom-left-radius: 2px;
    overflow-y: auto;
    /* display: block; */
    border-width: 1px;
    border-style: solid;
    border-color: rgba(255, 255, 255, 0.3);
    /* border-image: initial; */
}
.dropdown-toggle{
    background-color:#2B2B2B;
    text-align: right;
    border:none;
    height:45px;
    /* padding */
    width: 230px;
}
.dropdown-menu{
    background-color:rgb(20, 21, 23);
    width: 230px;
    padding: 10px 15px;
    color:white;
}

.btn-light{
    border-radius: 40px;
}



</style>
