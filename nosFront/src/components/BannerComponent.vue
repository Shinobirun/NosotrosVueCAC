  <template>
    <section class="banner">
      <!-- Contenido del banner -->
      <img src="../assets/images/welcome-aboard-2334166_1280.jpg" alt="Banner de promoción">
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
  }

  .banner img {
      max-width: 100%;
      height: 300px;
  }
  </style>