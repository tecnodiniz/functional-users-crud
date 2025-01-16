import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue'; 
import UserDetailPage from '../views/UserDetailPage.vue'; 

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/user/:id',
    name: 'UserDetail',
    component: UserDetailPage,
    props: true, 
  },
];

const router = createRouter({
  history: createWebHistory(), 
  routes, 
});

export default router;
