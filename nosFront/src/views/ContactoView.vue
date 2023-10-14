<template>
    <div class="body">
        <HeaderComponent />
    <main>
        <ContactFormComponent ></ContactFormComponent>
    </main>
    <FooterComponent />
    </div>
  </template>
  
<script>
  
  import HeaderComponent from '@/components/HeaderComponent.vue';
  import FooterComponent from '../components/FooterComponent.vue'; 
  import ContactFormComponent from '@/components/ContactFormComponent.vue';


  export default {
    name: 'ToursView',
    components: {
      HeaderComponent,
      ContactFormComponent,
      FooterComponent
    },
    data() {
      return {
        mensaje: 'Componente Contacto'
      };
    },
    methods: {
      irAHome() {
        this.$router.push({ path: '/' });
      }
    }
}
  </script>
  
  <style scoped>
  .body {

font-family: 'Roboto', sans-serif;
margin: 0;
padding: 0;
background-image: url('../assets/images/playaMuelle.jpg');
background-size: cover; /* Ajusta la imagen al tamaño del viewport */
background-attachment: fixed; /* Fija la imagen de fondo para que no se desplace con el contenido */
}
  /* Estilos específicos para este componente */
  </style>