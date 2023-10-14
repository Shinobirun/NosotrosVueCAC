<template>
    <div class="modal" v-show="mostrarModal">
        <!-- Contenido de inicio de sesión -->
        <div class="modal-content">
            <h2>Iniciar Sesión</h2>
            <!-- Agrega tus campos de inicio de sesión aquí -->
            <input type="text" placeholder="Usuario">
            <input type="password" placeholder="Contraseña">
            <button @click="iniciarSesion">Iniciar Sesión</button>
            <button @click="cerrarModal">Cerrar</button>
        </div>
    </div>
  </template>
  
  <script>
  export default {
  name: 'LoginModalComponent',
  data() {
    return {
      mostrarModal: false
    };
  },
  methods: {
    cerrarModal() {
      this.$emit('close');
    },
    iniciarSesion() {
      // Agregar la lógica para autenticar al usuario
      // enviar una solicitud HTTP a tu backend
      // y manejar la respuesta
      alert('Iniciando sesión...');
    }
  }
}
  
  </script>
  
  <style scoped>
  /* Estilos para el modal */
  .modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%; /* Aprovecha todo el ancho del viewport */
  height: 100%; /* Aprovecha toda la altura del viewport */
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center; /* Centra horizontalmente */
  align-items: center; /* Centra verticalmente */
}

.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}

  </style>