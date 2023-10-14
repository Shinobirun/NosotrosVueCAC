import { createApp } from 'vue';
import App from './App.vue';
import router from './router/routes.js'; 
import '@/assets/css/Variables.css';

createApp(App)
  .use(router) // Usa el enrutador
  .mount('#app'); // Monta la aplicación en el elemento con ID "app"