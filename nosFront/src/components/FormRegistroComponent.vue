<template>
  <main>
    <div class="registration-container">
      <div class="registration-form">
        <h2>Forma parte de Nosotros</h2>
        <form @submit="handleSubmit"> <!-- Añadido el evento @submit -->
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" name="nombre" required>

          <label for="apellido">Apellido:</label>
          <input type="text" id="apellido" name="apellido" required>

          <label for="email">Correo Electrónico:</label>
          <input type="email" id="email" name="email" required>

          <label for="password">Contraseña:</label>
          <input type="password" id="password" name="password" required>

          <button type="submit">Registrarse</button>
        </form>
      </div>
      <div class="registration-image">
        <img src="../assets/images/registro/road-trip-4399206_1280.png" alt="Imagen de registro">
      </div>
    </div>
  </main>
</template>

<script>
import axios from 'axios';

const BASE_URL = process.env.VUE_APP_API_BASE_URL || 'http://127.0.0.1:8000/api';

export default {
  methods: {
    async verificarEmailExistente(email) {
      try {
        const response = await axios.get(`${BASE_URL}/verificar-email/?email=${email}`);
        return response.data.existe;
      } catch (error) {
        console.error('Error al verificar el email', error);
        return false;
      }
    },

    async handleSubmit(event) {
      event.preventDefault();

      const nombre = event.target.nombre.value;
      const apellido = event.target.apellido.value;
      const email = event.target.email.value;
      const password = event.target.password.value;

      const emailExistente = await this.verificarEmailExistente(email);

      if (emailExistente) {
        alert('El correo electrónico ya está registrado. Por favor, utiliza otro.');
        return;
      }

      // Si el correo no existe, puedes enviar la solicitud de registro aquí
      try {
        const response = await axios.post(`${BASE_URL}/usuarios/`, {
          nombre,
          apellido,
          mail: email,
          password,
          puntos: 0, // Puedes establecer los puntos inicialmente en 0 o el valor que desees.
          tipo: null, // Puedes establecer el tipo inicialmente en null o el valor que desees.
        });

        console.log('Registro exitoso', response.data);
        alert('Registro exitoso');
      } catch (error) {
        console.error('Error al registrar', error);
        alert('Error al registrar');
      }
    }
  }
}
</script>


  
  <style scoped>
   
  .registration-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 10%;
    margin-bottom: 10%;
  }
  
  .registration-form {
    background-color: var(--color-backForm1);
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px var(--color-shadowForm1);
    width: 50%;
    text-align: center;
    margin-right: 20px;
  }
  
  .registration-image img {
    max-width: 100%;
    height: 310px;
    border-radius: 10px;
    opacity: .8;
  }
  
  .registration-form h2 {
    font-size: 1.5rem;
    margin-bottom: 20px;
  }
  
  form {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    text-align: left;
  }
  
  label {
    font-size: 1rem;
    margin-bottom: 5px;
  }
  
  input[type="text"],
  input[type="email"],
  input[type="password"] {
    width: 90%;
    padding: 10px;
    border: 1px solid var(--color-border1);
    border-radius: 5px;
    padding-left: 10px;
  }
  
  input[type="text"]:hover,
  input[type="email"]:hover,
  input[type="password"]:hover {
    width: 90%;
    padding: 10px;
    border: 1px solid var(--color-border1);
    border-radius: 5px;
    padding-left: 10px;
    background-color: var(--color-accent);
    opacity: .3;
  }
  
  button[type="submit"] {
    grid-column: span 2;
    background-color: var(--color-primary);
    color: var(--color-text1);
    height: 30px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button[type="submit"]:hover {
    background-color: var(--color-secondary);
  }
  </style>