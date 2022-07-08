import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/Index'
import Model from '@/components/Model'

Vue.use(Router)

export default new Router({
    routes: [{
        path: '/',
        name: 'Index',
        component: HelloWorld
    }, {
        path: '/model/:model_type/:model_id/',
        name: 'Model',
        component: Model
    }]
})