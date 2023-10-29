<template>
  <section class="offers">
    <div v-for="offer in offers" :key="offer.id" class="offer">
      <img :src="require(`../assets/images/${offer.foto_url}`)" :alt="`Oferta ${offer.id}`">
      <h3>{{ offer.titulo }}</h3>
      <p>{{ offer.informacion }}</p>
      <a :href="`./pages/${offer.tipo.toLowerCase()}.html?id=${offer.id}`">Ver más</a>
    </div>
  </section>
</template>


<script>
import ApiService from '../servicios/apiService'; 

export default {
  name: 'OfferComponent',
  data() {
    return {
      offers: [],
    };
  },
  created() {
    ApiService.get('paquetes/')
      .then(response => {
        this.offers = response.data;
      })
      .catch(error => {
        console.error('Error al obtener ofertas:', error);
      });
  }
}
</script>

<style scoped>
.offers {
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
