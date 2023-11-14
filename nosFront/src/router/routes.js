import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/HomeView.vue';
import NotFound from '@/views/NotFoundView.vue';
import RegistroView from '@/views/RegistroView.vue';
import ContactoView from '@/views/ContactoView.vue';
import ToursView from '@/views/ToursView.vue';
import RelaxComponent from '../components/RelaxComponent.vue';
import RomanticComponent from '../components/RomanticComponent.vue'
import LoginModalComponent from '../components/LoginModalComponent.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/registro',
    name: 'Registro',
    component: RegistroView 
  },
  {
    path: '/contacto',
    name: 'Contacto',
    component: ContactoView 
  },
  {
    path: '/tours',
    name: 'Tours',
    component: ToursView, 
  },
  {
    path: '/:catchAll(.*)',
    name: 'NotFound',
    component: NotFound,
  },
  {
    path: '/relax',
    name: 'Relax',
    component: RelaxComponent
  
  },
  {
    path: '/romantic',
    name: 'Romantic',
    component: RomanticComponent
  
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginModalComponent 
  },
  
  // Agrega más rutas aquí si es necesario

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;