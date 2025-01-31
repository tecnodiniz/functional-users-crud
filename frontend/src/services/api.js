import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const get_users = () => api.get('/users')

export const get_user = (id) => api.get(`/users/${id}`)

export const new_user = (data) => api.post('/users/new', data)

export const update_user = (id, data) => api.put(`/users/${id}`, data)

export const user_delete = (id) => api.delete(`/users/${id}`)

export default api
