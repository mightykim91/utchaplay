<template>
    <tbody>
        <tr v-for="(review, index) in reviews" :key="review.id">
            <th scope="row">{{ index + 1 }}</th>
            <td>{{ review.title }}</td>
            <td>{{ review.user.username }}</td>
            <td><button class="btn btn-info" @click="checkDetail(review.id)" :review="review">상세보기</button></td>
        </tr>
    </tbody>
</template>

<script>


export default {
    name:'ReviewListItem',

    props: {
        reviews: Array,
        movieId:Number,
    },
    data(){
        return{
            mId:this.movieId,
        }
    },
    methods:{
        checkDetail(id){
            
            this.$router.push({ name:'ReviewItemDetail', params:{id:id}})
        }
    }
}

</script>

<style>
</style>