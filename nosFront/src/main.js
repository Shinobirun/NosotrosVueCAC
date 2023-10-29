import { createApp } from 'vue';
import App from './App.vue';
import router from './router/routes.js'; 
import '@/assets/css/Variables.css';
import axios from 'axios';

const app = createApp(App);

app.use(router); // Usa el enrutador

app.config.globalProperties.$axios = axios;

app.mount('#app');