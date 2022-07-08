// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

// 简单store模式（小项目没必要用vuex）
import store from './store/index.js';
Vue.prototype.$store = store;


import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import i18n from '@/assets/i18n/i18n'
// import VueI18n from 'vue-i18n'

import axios from 'axios';
Vue.prototype.$axios = axios;



Vue.config.productionTip = false
Vue.use(ElementUI)

// Vue.use(Element, { i18n: (key, value) => i18n.t(key, value), size: globalComponentSize });


/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    // store,
    i18n,
    components: { App },
    template: '<App/>'
})