<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-2 border-right text-left">
        <h4 id="head">관리자 메뉴</h4><hr class="bg-white">
        <router-link id="menu" v-bind:to="{ name: 'CreateMovie' }">영화 생성</router-link><br>
        <router-link id="menu" v-bind:to="{ name: 'ModifyMovie' }">영화 수정</router-link><br>
        <router-link id="menu" v-bind:to="{ name: 'DeleteMovie' }">영화 삭제</router-link>
      </div>
      <div class="col-10 border p-3 bg-dark">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>

export default {
    name: 'AdminPage',

}
</script>

<style>
#menu {
  font-family: 'Jua', sans-serif;
  font-size: 20px;
  color: white;
}

#head {
  font-family: 'Jua', sans-serif;
  color: white;
}

</style>