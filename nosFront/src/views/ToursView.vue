<template>
  <div class="body">
      <HeaderComponent />
  <main>
      <h1>{{ mensaje }}</h1>
      <button @click="irAHome">Ir a Home</button>
      <RelaxComponent></RelaxComponent> 
      <RomanticComponent></RomanticComponent>
  </main>
  <FooterComponent />
  </div>
</template>

<script>

import HeaderComponent from '../components/HeaderComponent.vue';
import FooterComponent from '../components/FooterComponent.vue'; 
import RelaxComponent from '../components/RelaxComponent.vue';
import RomanticComponent from '../components/RomanticComponent.vue';

export default {
name: 'ToursView',
components: {
  HeaderComponent,
  FooterComponent,
  RelaxComponent,
  RomanticComponent,
},
data() {
  return {
    mensaje: 'Componente Turismo'
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