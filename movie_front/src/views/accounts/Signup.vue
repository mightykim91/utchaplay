<template>

    <div class="signupform">
      <h3>회원가입</h3>
            <div>
                <label for="username"></label>
                <input class="user_input" v-model="signupData.username" type="text" id="username" placeholder="아이디를 입력하세요">
            </div>
            <!-- <div>
                <label for="email">이메일</label>
                <input v-model="signupData.email" type="email" id="email">
            </div> -->
            <div>
                <label for="password1"></label>
                <input class="password_input1" v-model="signupData.password1" type="password" id="password1" placeholder="비밀번호(8자 이상)">
            </div>
            <div>
                <label for="password2"></label>
                <input @keypress.enter="signup" class="password_input2" v-model="signupData.password2" type="password" id="password2" placeholder="비밀번호 확인">
            </div>
            <button class="signup_btn" @click="signup">회원가입</button>

    </div>
</template>

<script>
export default {
    name:'Signup',
    data() {
        return {
            signupData: {
                username: null,
                //email:null,
                password1: null,
                password2: null,
            }
        }
    },
    methods: {
       signup() {
        this.$emit('save-signup-data', this.signupData)
       }
    },
}
</script>

<style scoped>
    .signupform{
    position:absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    }

    h3{
    color:white;
    text-align: left;
    }
    .signup{
    position: fixed;
    top:300px;
    left:400px;

    }
    .signup_btn{
    background-color: rgb(252, 66, 106);
    color: rgb(255, 255, 255);
    font-weight: 700;
    letter-spacing: -0.1px;
    text-align: center;
    width: 500px;
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
    width: 500px;
    padding: 10px 10px 10px 14px;
    border-radius: 7px 7px 0px 0px;
    border: none;
    height: 80px;


    }
    .password_input1{
        font-weight: 400;
        width: 500px;
        padding: 10px 10px 10px 14px;
        border-radius: 0px;
        height: 80px;
        /* border: none; */
        border-top: 1px #C7C7C7;
        border-bottom: none;
        border-right: none;
        border-left: none;
    
    }
    .password_input2{
    font-weight: 400;
    width: 500px;
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