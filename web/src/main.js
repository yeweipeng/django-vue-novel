import 'babel-polyfill'
import Vue from 'vue'
import App from './App'
import Router from 'vue-router'
import {routes} from './utils/routing-table'
import {load} from './utils/load'
// import from 'vux/'

Vue.use(Router)
load(Vue)

const router = new Router({
  mode: 'history',
  // base: '/service/',
  routes
})


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
