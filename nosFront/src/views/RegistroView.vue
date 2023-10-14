<template>
  <div>
    <HeaderComponent />
    <main>
      <RegistroFormComponent />
      <WhatsappComponent></WhatsappComponent>
    </main>
    <FooterComponent />
  </div>
</template>
  
<script>
  import HeaderComponent from '@/components/HeaderComponent.vue';
  import RegistroFormComponent from '@/components/FormRegistroComponent.vue'; 
  import FooterComponent from '@/components/FooterComponent.vue'; 
  import WhatsappComponent from '@/components/WhatsappComponent.vue';

  export default {
    components: {
      HeaderComponent,
      RegistroFormComponent,
      WhatsappComponent,
      FooterComponent
    }
  }
</script>

<style scoped>
/* Estilos específicos de la página de inicio */
 div    {

  font-family: 'Roboto', sans-serif;
  margin: 0;
  padding: 0;
  background-image: url('../assets/images/registro/amanecerLago.jpg');
  background-size: cover; /* Ajusta la imagen al tamaño del viewport */
  background-attachment: fixed; /* Fija la imagen de fondo para que no se desplace con el contenido */
 }

 main {
  height: 58vh;
 }
</style>