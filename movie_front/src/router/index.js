import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import Signup from '../views/accounts/Signup.vue'
import Login from '../views/accounts/Login.vue'

import MovieListGenre from '../views/MovieListGenre.vue'
import ReviewList from '../views/MovieReview/ReviewList.vue'
import CreateReview from '../views/MovieReview/CreateReview.vue'
import ReviewItemModify from '../views/MovieReview/ReviewItemModify.vue'
import AdminPage from '../views/AdminPage.vue'

//Child for admin page
import CreateMovie from '../components/admin/CreateMovie.vue'
import ModifyMovie from '../components/admin/ModifyMovie.vue'
import DeleteMovie from '../components/admin/DeleteMovie.vue'

import ReviewItemDetail from '../views/MovieReview/ReviewItemDetail.vue'





// import { component } from 'vue/types/umd'

Vue.use(VueRouter)

  const routes = [
// movie
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/genre/:id',
    name: 'MovieListGenre',
    component: MovieListGenre,
    props: route => ({
     id : Number(route.params.id)
    })
  },
  
// accounts
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },

// MovieReview
  {
    path: '/moviereview/:id',
    name: 'ReviewList',
    component: ReviewList,
    props:route => ({
      id: Number(route.params.id)
    })
  },
  {
    path: '/moviereview/create/:id', //영화id
    name: 'CreateReview',
    component: CreateReview,
    props: route => ({
      id : Number(route.params.id)
     })

  },

  //admin page
  {
    path: '/adminpage/',
    name: 'AdminPage',
    component: AdminPage,
    children: [
      {
        path: '',
        name: 'CreateMovie',
        component: CreateMovie
      },
      {
        path: '/modifymovie',
        name: 'ModifyMovie',
        component: ModifyMovie
      },
      {
        path: '/deletemovie',
        name: 'DeleteMovie',
        component: DeleteMovie
      },
    ]
  },
  {
    path: '/moviereview/modify/:id', //영화id
    name: 'ReviewItemModify',
    component: ReviewItemModify,
    props: route => ({
      id : Number(route.params.id)
     })

  },
  {
    path: '/moviereview/detail/:id', //리뷰id 
    name: 'ReviewItemDetail',
    component: ReviewItemDetail,
    props: route => ({
      id : Number(route.params.id)
     })

  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
