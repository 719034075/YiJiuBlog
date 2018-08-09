import request from '@/utils/request'

export function fetchList(data) {
    return request({
        url: '/blog/find-by-conditions',
        method: 'post',
        data
    })
}

export function fetchArticle(id) {
    return request({
        url: `/blog/find-by-id/${id}`,
        method: 'get',
    })
}

export function fetchPv(pv) {
    return request({
        url: '/article/pv',
        method: 'get',
        params: { pv }
    })
}

export function createArticle(data) {
    return request({
        url: '/blog/create',
        method: 'post',
        data
    })
}

export function updateArticle(data) {
    return request({
        url: '/blog/edit',
        method: 'post',
        data
    })
}
