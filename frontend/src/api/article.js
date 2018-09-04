import request from '@/utils/request'

export function fetchList(data) {
    return request({
        url: '/article/list/all',
        method: 'post',
        data
    })
}

export function fetchArticle(id) {
    return request({
        url: `/article/detail/${id}`,
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
        url: '/article/create',
        method: 'post',
        data
    })
}

export function updateArticle(data) {
    return request({
        url: '/article/update',
        method: 'post',
        data
    })
}

export function deleteArticle(id){
  return request({
    url: `/article/delete/${id}`,
    method: 'get',
  })
}

export function fetchPublishedList(data) {
    return request({
        url: '/article/list/published',
        method: 'post',
        data
    })
}