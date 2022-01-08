import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [{
  path: '/',
  component: () => import('@/views/login/index'),
  hidden: true
},

{
  path: '/404',
  component: () => import('@/views/404'),
  hidden: true
},

{
  path: '/register',
  component: () => import('@/views/register/index'),
  hidden: true
},

{
  path: '/dashboard',
  component: Layout,
  children: [{
    path: '',
    name: 'dashboard',
    component: () => import('@/views/dashboard/index'),
    meta: {
      title: '首页',
      icon: 'dash-board'
    }
  }]
},

{
  path: '/photo',
  component: Layout,
  children: [{
    path: 'index',
    name: 'Form',
    component: () => import('@/views/photo/index'),
    meta: {
      title: '图片检测',
      icon: 'el-icon-s-help'
    }
  }]

},

{
  path: '/video',
  component: Layout,
  children: [{
    path: 'index',
    name: 'Form',
    component: () => import('@/views/video/index'),
    meta: {
      title: '视频检测',
      icon: 'video'
    }
  }]
},

{
  path: '/camera',
  component: Layout,
  children: [{
    path: 'index',
    name: 'Form',
    component: () => import('@/views/camera/index'),
    meta: {
      title: '监控检测',
      icon: 'camera'
    }
  }]
},

{
  path: '/nested',
  component: Layout,
  redirect: '/nested/menu1',
  name: 'Nested',
  meta: {
    title: '个人中心',
    icon: 'nested'
  },
  children: [{
    path: 'menu1',
    component: () => import('@/views/nested/menu1/index'), // Parent router-view
    name: 'Menu1',
    meta: {
      title: '用户信息'
    }
  },
  {
    path: 'menu2',
    component: () => import('@/views/nested/menu2/index'),
    name: 'Menu2',
    meta: {
      title: '修改密码'
    }
  },
  {
    path: '../',
    name: 'Menu2',
    meta: {
      title: '退出登录'
    }
  }
  ]
},

// {
//   path: 'external-link',
//   component: Layout,
//   children: [
//     {
//       path: 'https://panjiachen.github.io/vue-element-admin-site/#/',
//       meta: { title: 'External Link', icon: 'link' }
//     }
//   ]
// },

// 404 page must be placed at the end !!!
{
  path: '*',
  redirect: '/404',
  hidden: true
}
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({
    y: 0
  }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
