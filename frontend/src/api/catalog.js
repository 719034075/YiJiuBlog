import request from '@/utils/request'

export function fetchList(data) {
  return request({
    url: '/catalog/list/all',
    method: 'post',
    data
  })
}

export function fetchCatalogs() {
  return request({
    url: '/catalog/list/all',
    method: 'get',
  })
}

export function fetchCatalog(id) {
  return request({
    url: `/catalog/detail/${id}`,
    method: 'get',
  })
}

export function createCatalog(data) {
  return request({
    url: '/catalog/create',
    method: 'post',
    data
  })
}

export function updateCatalog(data) {
  return request({
    url: '/catalog/update',
    method: 'post',
    data
  })
}

export function deleteCatalog(id){
  return request({
    url: `/catalog/delete/${id}`,
    method: 'get',
  })
}
