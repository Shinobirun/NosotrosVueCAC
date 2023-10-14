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
      }
    },
    methods: {
      volver() {
        this.$emit('volver');
      }
    }
  }
  </script>
  
  <style scoped>

  </style>
  