import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false



//导入api  将api注册进Vue的原型   以后在项目中就可以使用this.$api
import * as api from './api'
Vue.prototype.$api=api


//将js-cookie模块注册到vue原型
import jsCookie from 'js-cookie'
Vue.prototype.$jsCookie=jsCookie


import Vant from 'vant';
import 'vant/lib/index.css';
Vue.use(Vant);


import axios from 'axios';
Vue.prototype.$http=axios;


import vueToTop from 'vue-totop'
Vue.use(vueToTop)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
