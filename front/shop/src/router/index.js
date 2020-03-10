import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Cart from '../views/Cart.vue'
import Mine from '../views/Mine.vue'
import Category from '../views/Category.vue'
import Detail from '../views/Detail.vue'
import Search from '../views/Search.vue'
import Personal from '../views/Personal.vue'
import My from '../views/My.vue'
import Total from '../views/Total.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/detail/:id',
    name: 'detail',
    component: Detail
  },
  {
    path: '/cart',
    name: 'cart',
    component: Cart,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/my',
    name: 'my',
    component: My,
  },
  {
    path: '/total',
    name: 'total',
    component: Total,
  },
  {
    path: '/search',
    name: 'search',
    component: Search,
  },
  {
    path: '/personal',
    name: 'personal',
    component: Personal,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/mine',
    name: 'mine',
    component: Mine,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/category/:id',
    name: 'category',
	component: Category,
	meta:{
		tabbar:true
	}
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes,
  // 跳转页面时置顶
  scrollBehavior(){
	  return{
		  x:0,
		  y:0
	  }
  }
})

export default router
