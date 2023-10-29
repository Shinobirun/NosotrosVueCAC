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
            <a href="#"><img src="../assets/images/icons/twit.png" alt="Twitter">  Twitter</a>
          </li>
          <li>
            <a href="#"><img src="../assets/images/icons/inst.png" alt="Intagram">  Instagram</a>
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
        <p>
            <a href="#"><img src="../assets/images/icons/inst.png" alt="Intagram">  Tik Tok</a>
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
  background-color: #f8f8f8;
  color: var(--color-primary);
  padding: 10px 5px;
  padding-left: 5%; /* Espacio a la izquierda */
  padding-right: 5%;  

}

.foot {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

ul {
  list-style-type: none;
  padding: 0;
}

ul li {
  margin-bottom: 10px;
}

a {
  text-decoration: none;
  color: var(--color-primary);
  opacity: 1;
}

.icon {
  margin-right: 5px; /* Espacio entre el icono y el texto */
  font-size: 1.2em; /* Tamaño del icono */
}

.copy-right {
  display: flex;
  justify-content: center; /* Esto centra horizontalmente el contenido */
  align-items: center;
  margin-top: 5px; /* Añade espacio entre el contenido y el borde superior del footer */
}

a img, p img {
  vertical-align: middle;
  margin-bottom: 4px; /* Ajusta este valor según sea necesario */
}

img {
  height: 25px;
}
/* Media query para pantallas pequeñas */
@media (max-width: 768px) {
  footer {
    padding: 10px; 
  }
  .foot {
    flex-direction: column; 
  }
  ul li {
    margin-bottom: 0; 
  }
}
/* Media query para pantallas medianas */
@media (min-width: 769px) and (max-width: 1024px) {
  footer {
    padding: 15px; 
  }
  .foot {
    flex-direction: row;
  }
  ul li {
    margin-bottom: 0;
    margin-right: 20px;
  }
}
/* Media query para pantallas grandes */
@media (min-width: 1025px) {
  footer {
    padding: 20px; 
  }
}
</style>