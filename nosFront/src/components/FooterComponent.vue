<template>
  <footer>
    <div class="foot">
      <div>
        <h3 class="title">¡Síguenos en las redes sociales!</h3>
        
        <ul>
          <li>
            <a href="#"><img src="../assets/images/icons/fac.png" alt="Facebook">  Facebook</a>
          </li>
          <li>
            <a href="#"><img src="../assets/images/icons/inst.png" alt="Intagram">  Instagram</a>
          </li>
          <li>
            <a href="#"><img src="../assets/images/icons/tiktok.png" alt="Tik Tok">  Tik Tok</a>
          </li>
          <li>
            <a href="#"><img src="../assets/images/icons/twit.png" alt="X">  X</a>
          </li>
        </ul>
      </div>
      <div>
        <h3 class="title">Contacto</h3>
        <p>
          <img src="../assets/images/icons/phone.png" alt="Telefono"> Teléfono: 11-4546-7849
        </p>
        <p>
          <img src="../assets/images/icons/mail.png" alt="Mail"> Correo electrónico: info@tudominio.com
        </p>
        
      </div>
    </div>
    <div class="copy-right">
      <p>&copy; 2023 Nosotros Turismo. Todos los derechos reservados.</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterComponent',
  data() {
    return {
      colorPrimary: '#bbb737f8',
    };
  },
}
</script>

<style scoped>
/* Estilos específicos del pie de página */
footer {
  background-color: #524438;
  color: #ffff;
  padding: 10px 5px;
  padding-left: 5%;
  padding-right: 5%;
}

.foot {
  display: flex;
  flex-wrap: wrap; /* Añadido para permitir envolver en dispositivos pequeños */
  justify-content: space-between;
  align-items: center;
}

ul {
  list-style-type: none;
  padding: 0;
  display: flex; /* Cambiado para flexbox */
}

ul li {
  margin-right: 10px; /* Añadido espacio entre elementos */
  margin-bottom: 10px;
}

a {
  text-decoration: none;
  color: #ffff;
  opacity: 1;
}

.icon {
  margin-right: 5px; /* Espacio entre el icono y el texto */
  font-size: 1.1em; /* Tamaño del icono */
}

.copy-right {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 5px;
}

a img, p img {
  vertical-align: middle;
  margin-bottom: 4px;
}

img {
  height: 25px;
}

/* Media queries para dispositivos de diferentes tamaños */

@media (max-width: 767px) {
  ul {
    flex-direction: column; /* Cambiar a columna en dispositivos pequeños */
    align-items: flex-start; /* Alinear a la izquierda */
  }

  ul li {
    margin-right: 0; /* Eliminar espacio entre elementos */
  }
}
</style>