<template>
  <div class="detalles">
    <h2>{{ ofertaSeleccionada.titulo }}</h2>
    <img :src="ofertaSeleccionada.imagen" :alt="ofertaSeleccionada.titulo">
    <p>{{ ofertaSeleccionada.descripcion }}</p>
    <button @click="volver">Volver</button>
  </div>
</template>

<script>
export default {
  name: 'DetailsComponent',
  props: {
    ofertaSeleccionada: {
      type: Object,
      required: true
    },
    tipoDePaquete: {
      type: String,
      required: true
    }
  },
  methods: {
  volver() {
    // Obtiene la posición de la oferta seleccionada
    const posicionOferta = this.ofertaSeleccionada.posicion;

    // Mapa de posiciones a tipos de paquete
    const mapaPosiciones = {
      1: 'aventura',
      2: 'relax',
      3: 'aventura',
      4: 'romantico',
      5: 'playa',
      6: 'arqueologico'
    };

    // Determina el tipo de paquete al que debe volver
    const tipoVolver = mapaPosiciones[posicionOferta];

    // Emite el evento con el tipo de paquete y la ruta al que debe volver
    this.$emit('volver', { tipo: tipoVolver, ruta: 'home' });
    console.log(tipoVolver);
  }
}

  
}
</script>

  
  <style scoped>

  </style>
  