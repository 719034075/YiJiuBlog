import Vue from 'vue'
import Router from 'vue-router'

// in development-env not use lazy-loading, because lazy-loading too many pages will cause webpack hot update too slow. so only in production use lazy-loading;
// detail: https://panjiachen.github.io/vue-element-admin-site/#/lazy-loading

Vue.use(Router);

/* Layout */
import Layout from '../views/layout/Layout'

/**
 * hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
 *                                if not set alwaysShow, only more than one route under the children
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noredirect           if `redirect:noredirect` will no redirct in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar,
  }
 **/
export const constantRouterMap = [
  {path: '/homepage', component: () => import('@/views/homepage/index'), hidden: true},
  {path: '/blog', component: () => import('@/views/blog/index'), hidden: true},
  {path: '/login', component: () => import('@/views/login/index'), hidden: true},
  {path: '/404', component: () => import('@/views/404'), hidden: true},

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    name: 'Dashboard',
    hidden: true,
    children: [{
      path: 'dashboard',
      component: () => import('@/views/dashboard/index')
    }]
  },


];


export default new Router({
  // mode: 'history', //后端支持可开
  scrollBehavior: () => ({y: 0}),
  routes: constantRouterMap
})

export const asyncRouterMap = [
  {
    path: '/catalog',
    component: Layout,
    redirect: '/catalog/list',
    name: 'catalog',
    meta: {
      title: '分类栏',
      icon: 'catalog'
    },
    children: [
      {
        path: 'list',
        component: () => import('@/views/catalog/list'),
        name: 'catalogList',
        meta: {title: '分类栏', icon: 'catalog'}
      }
    ]
  },
  {
    path: '/article',
    component: Layout,
    redirect: '/article/list',
    name: 'article',
    meta: {
      title: '文章栏',
      icon: 'article'
    },
    children: [
      {
        path: 'create',
        component: () => import('@/views/article/create'),
        name: 'createArticle',
        meta: {title: '创建文章', icon: 'edit'}
      },
      {
        path: 'edit/:id',
        component: () => import('@/views/article/edit'),
        name: 'editArticle',
        meta: {title: '编辑文章', noCache: true},
        hidden: true
      },
      {
        path: 'list',
        component: () => import('@/views/article/list'),
        name: 'articleList',
        meta: {title: '文章列表', icon: 'list'}
      },
      {
        path: 'view/:id',
        component: () => import('@/views/article/view'),
        name: 'viewArticle',
        meta: {title: '查看文章', noCache: true},
        hidden: true
      },
    ]
  },
  {path: '*', redirect: '/404', hidden: true}

];
