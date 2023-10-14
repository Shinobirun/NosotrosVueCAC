<template>
  <div class="body">
    <HeaderComponent />
    <main>
      <BannerComponent />
      <OffertComponent @ver-detalles="mostrarDetalles" />
      <DetailsComponent v-if="mostrarDetalles" :ofertaSeleccionada="ofertaSeleccionada" @volver="ocultarDetalles" />
      <WhatsappComponent></WhatsappComponent>
    </main>
    <FooterComponent />
  </div>
</template>


<script>  
import HeaderComponent from '@/components/HeaderComponent.vue'
import BannerComponent from '@/components/BannerComponent.vue'
import OffertComponent from '@/components/OffertsComponent.vue'
import FooterComponent from '@/components/FooterComponent.vue'
import DetailsComponent from '@/components/DetailsComponent.vue'
import WhatsappComponent from '@/components/WhatsappComponent.vue'

export default {
name: 'HomeView',
components: {
  HeaderComponent,
  BannerComponent,
  OffertComponent,
  WhatsappComponent,
  FooterComponent,
  DetailsComponent
},

data() {
    return {
      mensaje: 'Componente Turismo',
      mostrarDetalles: false,
      ofertaSeleccionada: null
    };
  },
  methods: {
    mostrarDetails(oferta) {
      this.mostrarDetalles = true;  
      this.ofertaSeleccionada = oferta;
    },
    ocultarDetalles() {
      this.mostrarDetalles = false;
      this.ofertaSeleccionada = null;
    }
  }
}
</script>

<style scoped>
/* Estilos específicos de la página de inicio */
.body {

font-family: 'Roboto', sans-serif;
margin: 0;
padding: 0;
background-image: url('../assets/images/playaMuelle.jpg');
background-size: cover; /* Ajusta la imagen al tamaño del viewport */
background-attachment: fixed; /* Fija la imagen de fondo para que no se desplace con el contenido */
}
</style>