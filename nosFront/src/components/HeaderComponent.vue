<template>
    <header>
        <div class="logo">
            <img src="../assets/images/logo5.png" alt="Logo de Nosotros">
        </div>
        <nav>
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
        mostrarModal: false 
        };
    },
    methods: {
        abrirModal() {
        this.mostrarModal = true;
        console.log(this.mostrarModal);
        },
        cerrarModal() {
        this.mostrarModal = false;
        console.log(this.mostrarModal);
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
  </style>