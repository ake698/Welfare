import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      redirect:"/login",
      component: HelloWorld
    },
    {
      path: '/login',
      name: 'Login',
      component: ()=> import('../components/Login'),
      meta:{
        title:'登陆页面'
      }
    },
    {
      path: '/register',
      name: 'Register',
      component: ()=> import('../components/Register'),
      meta:{
        title:'注册页面'
      }
    },
    {
      path: '/home',
      name: 'Home',
      component: ()=> import('../components/Home'),
      meta:{
        "requireAuth":true
      },
      children:[
        {
          path: '/index',
          name: 'index',
          component: ()=> import('../components/Index'),
          meta:{
            "requireAuth":true,
            "title":'公益活动'
          },
        },
        {
          path: '/activity/:id',
          name: 'activity',
          component: ()=> import('../components/ActivityDetail'),
          meta:{
            "requireAuth":true,
            "title":'公益活动详情'
          },
        },
        {
          path: '/applicant',
          name: 'applicant',
          component: ()=> import('../components/Applicant'),
          meta:{
            "requireAuth":true,
            "title":'申请列表'
          },
        },
        {
          path: '/messages',
          name: 'messages',
          component: ()=> import('../components/Messages'),
          meta:{
            "requireAuth":true,
            "title":'留言列表'
          },
        },
        {
          path: '/resource',
          name: 'resource',
          component: ()=> import('../components/Resource'),
          meta:{
            "requireAuth":true,
            "title":'资源列表'
          },
        },
        {
          path:'/activity_add',
          name:'addActivity',
          component: ()=> import('../components/AddActivity'),
          meta:{
            "requireAuth":true,
            "title":'发布活动'
          }
        },
        {
          path: '/user',
          name: 'user',
          component: ()=> import('../components/User'),
          meta:{
            "requireAuth":true,
            "title":'用户管理'
          },
        },
        
      ]
    },
  ]
})
