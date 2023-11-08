<template>
  <div class="contenedor">
    <div class="formulario">
      <h2>Contactános</h2>
      <form @submit.prevent="enviarConsulta">
        <div>
          <input type="text" v-model="nombre" required placeholder="Tu nombre" />
        </div>
        <div>
          <input type="email" v-model="email" required placeholder="Correo Electrónico" />
        </div>
        <div>
          <textarea v-model="mensaje" required placeholder="Dejanos aca tu consulta, saludo, o comentario."></textarea>
        </div>
        <button type="submit">Enviar Consulta</button>
      </form>
    </div>

    <div class="iframe">
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.8253499187767!2d-58.423588810360314!3d-34.58328548669217!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcb581f543de5d%3A0x192f65363601ef13!2sAv.%20Sta.%20Fe%203954-3902%2C%20C1425BHB%20CABA!5e0!3m2!1ses-419!2sar!4v1695125649356!5m2!1ses-419!2sar"
        width="600"
        height="450"
        style="border:0;"
        allowfullscreen=""
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
      ></iframe>
    </div>

    <div>
      <WhatsappComponent></WhatsappComponent>
    </div>
  </div>
</template>

<script>
import WhatsappComponent from './WhatsappComponent.vue';
import { enviarCorreo } from '@/services/mailerService'; 

export default {
  components: {
    WhatsappComponent
  },
  data() {
    return {
      nombre: '',
      email: '',
      mensaje: ''
    };
  },
  
  methods: {
    enviarConsulta() {
      const consulta = {
        nombre: this.nombre,
        email: this.email,
        mensaje: this.mensaje
      };
      enviarCorreo(consulta)
        .then(response => {
          console.log('Correo enviado:', response);
          // Puedes manejar la respuesta del backend aquí
        })
        .catch(error => {
          console.error('Error al enviar el correo:', error);
        });
    }
  }
}

</script>

<style scoped>
.contenedor {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.formulario {
  background-color: var(--color-backForm1);
  color: var(--color-text1);
  width: 80%;
  padding: 30px;
}

.iframe {
  background-color: var(--color-backForm1);
  width: 98.5%;
  padding: 10px;
}

.iframe iframe {
  width: 100%;
}

button {
  background-color: var(--color-primary);
  color: var(--color-text1);
  height: 40px;
  width: 100%;
  margin: 10px 0;
}

button:hover {
  background-color: var(--color-secondary);
}

input:hover,
textarea:hover {
  filter: brightness(1.1);
  color: var(--color-text1);
  padding: 10px;
  border: 1px solid var(--color-border1);
  border-radius: 5px;
  padding-left: 10px;
  background-color: var(--color-accent);
  opacity: 0.3;
}

input,
textarea {
  width: calc(100% - 20px);
  padding: 10px;
  margin: 10px 0;
  font-size: 16px;
  transition: filter 0.3s;
  color: black;
  opacity: 1;
}

h2 {
  margin: 20px 0;
  text-align: center;
  color: var();
}

.whatsapp-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
}

.whatsapp-button img {
  width: 50px;
}
</style>
