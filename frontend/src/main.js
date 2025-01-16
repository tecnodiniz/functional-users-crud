import { createApp } from 'vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';

// Vuetify
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

// Router
import router from './router';

// Components
import App from './App.vue';

// Creating Vuetify
const vuetify = createVuetify({
  components,
  directives,
});

// CCreating and mouting app
createApp(App)
  .use(vuetify)   //  Vuetify
  .use(router)    //  Vue Router
  .mount('#app');
