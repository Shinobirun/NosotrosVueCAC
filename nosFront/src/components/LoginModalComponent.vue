<template>
  <div class="modal" v-show="mostrarModal">
    <!-- Contenido de inicio de sesión -->
    <div class="modal-content">
      <h2>Iniciar Sesión</h2>
      <form @submit.prevent="iniciarSesion">
        <input v-model="email" type="text" name="email" placeholder="Correo electrónico">
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
      email: '',
      password: ''
    };
  },
  methods: {
    cerrarModal() {
      this.$emit('close');
    },
    async iniciarSesion() {
      try {
        const response = await axiosInstance.post('iniciar_sesion/', {
          email: this.email,
          password: this.password
        });

        console.log(response.data);
        // Si el inicio de sesión es exitoso, puedes cerrar el modal o redirigir al usuario a otra página
        if (response.status === 200) {
          this.cerrarModal();
        }
      } catch (error) {
        if (error.response && error.response.status === 400) {
          alert('Correo electrónico o contraseña incorrectos.');
        } else {
          alert('Error al iniciar sesión. Por favor, inténtalo de nuevo.');
        }
        console.error(error);
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