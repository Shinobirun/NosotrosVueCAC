<template>
  <section class="offers">
    <div class="loader-container" v-if="loading">
      <LoaderComponet />
    </div>
    <div v-else class="offer-container">
      <div v-for="offer in offers" :key="offer.id" class="offer">
        <img :src="require(`../assets/images/${offer.foto_url}`)" :alt="`Oferta ${offer.id}`">
        <h3>{{ offer.titulo }}</h3>
        <p>{{ offer.informacion }}</p>
        <a :href="`./pages/${offer.tipo.toLowerCase()}.html?id=${offer.id}`">Ver más</a>
      </div>
    </div>
  </section>
</template>

<script>
import ApiService from '../servicios/apiService'; 
import LoaderComponet from './LoaderComponet.vue';

export default {
  name: 'OfferComponent',
  components: {
    LoaderComponet
  },
  data() {
    return {
      offers: [],
      loading: true
    };
  },
  created() {
    const tipoDePaquete = 'tours'; 
    ApiService.getPaquetesPorTipo(tipoDePaquete)
      .then(response => {
        this.offers = response.data;
        this.loading = false;
      })
      .catch(error => {
        console.error('Error al obtener ofertas:', error);
      });
  }
}
</script>

<style scoped>
.offers {
  text-align: center;
}

.loader-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50vh;
}



.offer-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.offer {
  background-color: #f5f5f5;
  padding: 20px;
  margin: 20px;
  border-radius: 10px;
  width: 300px;
  margin-right: 20px;
  margin-bottom: 20px;
}

.offer h3 {
  font-size: 1.5rem;
  margin: 10px 0;
}

.offer p {
  font-size: 1rem;
  margin: 10px 0;
}

.offer img {
  max-width: 100%;
  height: auto;
  width: 100%;
  max-height: 200px;
}

.offer a {
  display: block;
  color: #333;
  text-decoration: none;
  font-weight: bold;
  background-color: #fff;
  border: 1px solid #333;
  padding: 8px 16px;
  border-radius: 4px;
  text-align: center;
  margin-top: 10px;
  transition: background-color 0.3s;
}

.offer a:hover {
  background-color: #333;
  color: #fff;
}
</style>
