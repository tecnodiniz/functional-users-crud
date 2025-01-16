import { createApp } from 'vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';

// Vuetify
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

// Router
import router from './router'; // Importando o Vue Router

// Components
import App from './App.vue';

// Criar Vuetify
const vuetify = createVuetify({
  components,
  directives,
});

// Criando e montando a aplicação Vue
createApp(App)
  .use(vuetify)   // Registrando Vuetify
  .use(router)    // Registrando o Vue Router
  .mount('#app');
