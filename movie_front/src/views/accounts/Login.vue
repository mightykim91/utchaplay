<template>

<!-- <div class="login"> -->
  <div class="loginform">
      <h3>로그인</h3>
          <div >
            <label  for="username"></label>
            <input class="user_input" v-model="loginData.username" type="text" id="username" placeholder="아이디를 입력하세요">
          </div>
          <div >
            <label  for="password"></label>
            <input @keypress.enter="login" class="password_input" v-model="loginData.password" type="password" id="password" placeholder="비밀번호를 입력하세요">
          </div>
          <button class="login_btn" @click="login">로그인</button>
  </div>
<!-- </div> -->

</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            loginData: {
                username: null,
                password: null,
            }
        }
    },
    methods: {
        login() {
            this.$emit('save-login-data', this.loginData)
        }
    }

}
</script>

<style scoped>
/* .form{
  text-align: left;
  margin: 20px auto;
  width:50%;
} */

h3{
  color:white;
  text-align: left;
}


.loginform{
  position:absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.login_btn{
  background-color: rgb(252, 66, 106);
  color: rgb(255, 255, 255);
  font-weight: 700;
  letter-spacing: -0.1px;
  text-align: center;
  width: 450px;
  font-size: 16px;
  line-height: 47px;
  height: 48px;
  border-radius: 40px;
  border:none;
  height: 80px;
  margin-top: 20px;
}
.user_input{
  font-weight: 400;
  width: 450px;
  padding: 10px 10px 10px 14px;
  border-radius: 7px 7px 0px 0px;
  border: none;
  height: 80px;


}
.password_input{
  font-weight: 400;
  width: 450px;
  padding: 10px 10px 10px 14px;
  border-radius: 0px 0px 7px 7px;
  height: 80px;
  /* border: none; */
  border-top: 1px #C7C7C7;
  border-bottom: none;
  border-right: none;
  border-left: none;
  

}
</style>