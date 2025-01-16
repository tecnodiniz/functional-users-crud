import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue'; // Exemplo de importação de uma página
import UserDetailPage from '../views/UserDetailPage.vue'; // Exemplo de importação de uma página

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
    props: true, // Permite passar parâmetros para o componente
  },
];

const router = createRouter({
  history: createWebHistory(), // Usando o histórico de navegação com hash
  routes, // Registrando as rotas
});

export default router;
