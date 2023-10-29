<template>
    <header>
      <div class="logo">
        <img src="../assets/images/logo5.png" alt="Logo de Nosotros">
      </div>
      <!-- Lista de navegación principal -->
      <nav class="main-nav" v-if="!isSmallScreen">
        <ul>
          <li><a href="/"><img src="../assets/images/icons/travelling_2060284.png" alt="Inicio"> Inicio</a></li>
          <li><a href="/tours"><img src="../assets/images/icons/map_1934285.png" alt="Tours"> Tours</a></li>
          <li><a href="/contacto"><img src="../assets/images/icons/reception_1934306.png" alt="Contacto"> Contacto</a></li>
          <li><a href="/registro"><img src="../assets/images/icons/rating_1934299.png" alt="Registrarse"> Registrarse</a></li>
          <li @click="abrirModal"><a href="#"><img src="../assets/images/icons/luggage_1934282.png" alt="Iniciar sesión"> Iniciar sesión</a></li>
        </ul>
      </nav>
      <!-- Botón del menú hamburguesa solo en pantallas pequeñas -->
      <div class="hamburger-menu" @click="toggleNav" v-if="isSmallScreen">
        <div class="bar" v-for="i in 3" :key="i"></div>
      </div>
      <!-- Lista para el menú hamburguesa :) -->
      <nav class="nav-hamburguer" :class="{ active: showNav }" v-if="isSmallScreen">
        <ul>
          <li><a href="/"><img src="../assets/images/icons/travelling_2060284.png" alt="Inicio"> Inicio</a></li>
          <li><a href="/tours"><img src="../assets/images/icons/map_1934285.png" alt="Tours"> Tours</a></li>
          <li><a href="/contacto"><img src="../assets/images/icons/reception_1934306.png" alt="Contacto"> Contacto</a></li>
          <li><a href="/registro"><img src="../assets/images/icons/rating_1934299.png" alt="Registrarse"> Registrarse</a></li>
          <li @click="abrirModal"><a href="#"><img src="../assets/images/icons/luggage_1934282.png" alt="Iniciar sesión"> Iniciar sesión</a></li>
        </ul>
      </nav>
      <LoginModalComponent v-show="mostrarModal" @close="cerrarModal" />
    </header>
  </template>
  
  <script>
  import LoginModalComponent from './LoginModalComponent.vue';
  
  export default {
    name: 'HeaderComponent',
    components: {
      LoginModalComponent
    },
    data() {
      return {
        mensaje: 'Componente Contacto',
        mostrarModal: false,
        showNav: false,
        isSmallScreen: false
      };
    },
    mounted() {
      
      this.isSmallScreen = window.innerWidth <= 768;
  
      window.addEventListener('resize', this.checkScreenSize);
    },
    beforeUnmount() {
      window.removeEventListener('resize', this.checkScreenSize);
    },
    methods: {
      abrirModal() {
        this.mostrarModal = true;
      },
      cerrarModal() {
        this.mostrarModal = false;
      },
      toggleNav() {
        this.showNav = !this.showNav;
      },
      checkScreenSize() {
        this.isSmallScreen = window.innerWidth <= 768;
      }
    }
  }
  </script>
  
  <style scoped>
  @import '@/assets/css/Variables.css';
  header {
     display: grid;
     grid-template-columns: 1fr auto; /* Divide el espacio en dos columnas, una para el logo y otra para el menú */
     align-items: center; /* Centra verticalmente los elementos en el header */
     background-color: var(--color-accent);
     opacity: 1;
     padding: 10px 0;
    
 }   

 header:hover {
     opacity: .9  ;
 }

 .logo {
     text-align: left; /* Alinea el logo a la izquierda */
     padding-left: 10% ;
     
 }

 nav {
     text-align: right; /* Alinea el menú a la derecha */
 }

 ul {
     list-style: none;
     margin: 0;
     padding: 0;
 }

 li {
     display: inline;
     margin-right: 20px; /* Espacio entre elementos del menú */
     
 }

 a {
     text-decoration: none;
     color: var(--color-primary); /* Color del texto del menú */
     font-weight: bold;
     
 }

 a:hover {
     text-decoration: none;
     color: var(--color-secondary); /* Color del texto del menú */
     font-weight: bold;

 }

 li a img{
     height: 30px;
 }

  
  /* Estilos para el menú de hamburguesa */
  .hamburger-menu {
    display: none;
    cursor: pointer;
  }
  
  .bar {
    width: 25px;
    height: 3px;
    background-color: var(--color-primary);
    margin: 5px auto;
    transition: 0.4s;
  }
  
  /* Media query para mostrar el menú de hamburguesa solo en pantallas pequeñas */
  @media (max-width: 768px) {
    .hamburger-menu {
      display: block;
    }
  
    .nav-hamburguer.active {
      max-height: 800px;
      background-color: var(--color-accent);
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
  
    .nav-hamburguer li {
      display: flex;
      flex-direction: column;
    }
  }
  
  @media (min-width: 769px) {
    .logo img {
      max-width: 80px;
    }
  }
  
  /* Media query para pantallas grandes */
  @media (min-width: 1025px) {
    .logo img {
      max-width: 100px;
    }
  }
  </style>
  