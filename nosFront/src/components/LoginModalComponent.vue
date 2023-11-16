<template>
  <div class="modal" v-show="mostrarModal">
    <!-- Contenido de inicio de sesión -->
    <div class="modal-content">
      <h2>Iniciar Sesión</h2>
      <form @submit.prevent="iniciarSesion">
        <input v-model="username" type="text" name="username" placeholder="Nombre de usuario">
        <input v-model="password" type="password" placeholder="Contraseña">
        <button type="submit">Iniciar Sesión</button>
      </form>
      <button @click="cerrarModal">Cerrar</button>
    </div>
  </div>
</template>

<script>
import axiosInstance from '@/services/interceptorService';

export default {
  name: 'LoginModalComponent',
  data() {
    return {
      mostrarModal: false,
      username: '',
      password: ''
    };
  },
  methods: {
    cerrarModal() {
      this.$emit('close');
    },
    async iniciarSesion() {
      try {
        const response = await axiosInstance.post('api/accounts/login/', {
          username: this.username,
          password: this.password
        });

        console.log('Datos de inicio de sesión:', this.username, this.password);
        console.log('Respuesta del servidor:', response.data);

        if (response.status === 200) {
          // El inicio de sesión fue exitoso, puedes realizar acciones necesarias
          console.log('Inicio de sesión exitoso:', response.data);
          this.cerrarModal();
        }
      } catch (error) {
        console.error('Error en la respuesta:', error.response);

        if (error.response && error.response.status === 400) {
          alert(`Error: ${error.response.data.mensaje || 'Nombre de usuario o contraseña incorrectos.'}`);
        } else {
          alert('Error al iniciar sesión. Por favor, inténtalo de nuevo.');
        }
      }
    }
  }
};
</script>

<style scoped>
/* Estilos para el modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
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

form {
  margin-bottom: 20px;
}
</style>
