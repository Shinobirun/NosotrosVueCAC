<template>
  <section class="banner">
    <!-- Contenido del banner -->
    <div class="banner-content">
      <h1>Viaja con Nosotros</h1>
      <p>Aprovecha nuestras ofertas y únete a la comunidad de viajeros VIP</p>
    </div>
  </section>
</template>

<script>
export default {
  name: 'BannerComponent'
}
</script>

<style scoped>
/* Estilos específicos del banner */
.banner {
  text-align: center;
  padding: 100px 0;
  background-color: #f8f8f8; /* Color de fondo suave */
  border-bottom: 1px solid #e0e0e0; /* Línea divisoria */
}

.banner-content {
  max-width: 800px;
  margin: 0 auto;
}

.banner h1 {
  font-size: 2.5em;
  margin-bottom: 20px;
}

.banner p {
  font-size: 1.2em;
  color: #555;
}
</style>
