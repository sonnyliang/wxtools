import Vue from 'vue'
import App from './App'
import request from "./utils/reqeust"

//引入vuex
import store from './store'
//把vuex定义成全局组件
Vue.prototype.$store = store


// 将封装好的异步函数挂载到vue
Vue.prototype.request=request;

Vue.config.productionTip = false

App.mpType = 'app'

const app = new Vue({
  ...App,
//挂载
  store
})
app.$mount()
