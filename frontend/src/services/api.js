import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const get_users = () => api.get('/users')

export const new_user = (data) => api.post('/users/new', data)

export default api
