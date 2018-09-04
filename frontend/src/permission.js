import router from './router'
import store from './store'
import NProgress from 'nprogress' // Progress 进度条
import 'nprogress/nprogress.css'// Progress 进度条样式
import { Message } from 'element-ui'
import { getToken } from '@/utils/auth' // 验权

function hasPermission(roles, permissionRoles) {
    if (roles.indexOf('superuser') >= 0) return true;
    if (!permissionRoles) return true;
    return roles.some(role => permissionRoles.indexOf(role) >= 0);
}


const whiteList = ['/homepage','/blog','/login']; // 不重定向白名单
router.beforeEach((to, from, next) => {
    NProgress.start();
    if (getToken()) {
        if (to.path === '/login') {
            next({ path: '/dashboard' });
            NProgress.done() // if current page is dashboard will not trigger	afterEach hook, so manually handle it
        } else {
            if (store.getters.roles.length === 0) {
                store.dispatch('GetInfo').then(res => { // 拉取用户信息
                    const roles = res.data.roles;
                    store.dispatch('GenerateRoutes', { roles }).then(() => { // 根据roles权限生成可访问的路由表
                        router.addRoutes(store.getters.addRouters); // 动态添加可访问路由表
                        next({ ...to, replace: true }) // hack方法 确保addRoutes已完成 ,set the replace: true so the navigation will not leave a history record
                    })
                }).catch(() => {
                    store.dispatch('FedLogOut').then(() => {
                        Message.error('验证失败,请重新登录');
                        next({ path: '/login' })
                    })
                })
            } else {
                next()
            }
        }
    } else {
        if (whiteList.indexOf(to.path) !== -1) {
            next()
        } else {
            next('/homepage');
            NProgress.done()
        }
    }
});

router.afterEach(() => {
    NProgress.done() // 结束Progress
});
