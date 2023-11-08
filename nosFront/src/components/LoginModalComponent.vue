<template>
    <div class="modal" v-show="mostrarModal">
        <!-- Contenido de inicio de sesión -->
        <div class="modal-content">
            <h2>Iniciar Sesión</h2>
            <!-- Agrega tus campos de inicio de sesión aquí -->
            <input type="text" name="email" placeholder="Correo electrónico">
            <input type="password" placeholder="Contraseña">
            <button @click="iniciarSesion">Iniciar Sesión</button>
            <button @click="cerrarModal">Cerrar</button>
        </div>
    </div>
  </template>
  
  <script>

  import axios from 'axios';


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
    async iniciarSesion() {
      const usuario = document.querySelector('input[type="text"]').value;
      const contrasena = document.querySelector('input[type="password"]').value;
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/iniciar_sesion/', {
          usuario,
          contrasena
        });
        alert(response.data.mensaje);
        // Si el inicio de sesión es exitoso, puedes cerrar el modal o redirigir al usuario a otra página
        if (response.status === 200) {
          this.cerrarModal();
        }
      } catch (error) {
        alert('Error al iniciar sesión. Por favor, verifica tus credenciales.');
      }
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
  background: #f09012;
  padding: 20px;
  border-radius: 8px;
  border-color: blue;
  text-align: center;
}

  </style>