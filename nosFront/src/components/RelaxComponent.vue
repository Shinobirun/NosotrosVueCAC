
<template>
 <section class="offerts">
        <h2>Tours Relax</h2>

        <div class="offert">
          <img src="../assets/images/maldivas.jpg" alt="Oferta Islas Maldivas">
          <h3>Islas Maldivas</h3>
          <p>Disfruta de unas vacaciones de ensueño en las hermosas Islas Maldivas, conocidas por sus playas de arena blanca, aguas cristalinas y bungalows sobre el agua. Un destino perfecto para relajarse y rejuvenecer durante 7 días y 6 noches en el paraíso.</p>
          <p>Algunas de las experiencias que podrás disfrutar en este increíble viaje incluyen:</p>
          <ul>
            <li>Snorkeling en arrecifes de coral<br></li>
            <li>Masajes relajantes en la playa<br></li>
            <li>Cenas románticas con vistas al océano<br></li>
            <li>Excursiones en barco al atardecer<br></li>
            <li>Buceo en aguas cristalinas:<br></li>
            <li>Visitas a islas locales<br></li>
          </ul>
          <p>¡Tu escapada a las Islas Maldivas será una experiencia inolvidable llena de relajación, aventuras submarinas y momentos románticos!</p>
          <a href="formulario.html">Solicitar Presupuesto</a>
        </div>

        <div class="offert">
          <img src="../assets/images/bali.jpg" alt="Oferta Bali, Indonesia">
          <h3>Bali, Indonesia</h3>
           <p>Sumérgete en la cultura balinesa y la belleza natural de Bali. Este destino ofrece playas, templos antiguos y selvas exuberantes. Es ideal para aquellos que buscan paz y tranquilidad durante 8 días y 7 noches en el paraíso balinés.</p>
          <p>Algunas de las experiencias que podrás disfrutar en este increíble viaje incluyen:</p>
          <ul>
            <li>Clases de yoga al amanecer<br></li>
            <li>Visitas a templos históricos<br></li>
            <li>Masajes balineses tradicionales <br></li>
            <li>Exploración de arrozales en terrazas<br></li>
            <li>Recorridos por las playas locales<br></li>
            <li>Cenas gourmet con vista al océano<br></li>
          </ul>
          <p>Tu viaje a Bali, Indonesia, será una experiencia única llena de cultura, belleza de la naturaleza y relajación total.</p>
          <a href="formulario.html">Solicitar Presupuesto</a>
        </div>

        <div class="offert">
          <img src="../assets/images/CostaAmalfitanaItalia.jpg" alt="Italia">
          <h3>Costa Amalfitana, Italia</h3>
          <p>Experimenta el encanto y la elegancia de la Costa Amalfitana en Italia. Con sus pintorescos pueblos costeros, deliciosa comida y hermosos paisajes, es un destino perfecto para relajarse durante 6 días y 5 noches en la costa italiana.</p>
          <p>Algunas de las experiencias que podrás disfrutar en este viaje incluyen:</p>
          <ul>
            <li>Degustación de vinos locales en las mas encantadores bodegas.<br></li>
            <li>Excursiones en barco a las grutas de la costa.<br></li>
            <li>Disfrute de la cocina italiana auténtica.<br></li>
            <li>Tiempo libre en las playas locales.<br></li>
            <li>Visitas a pintorescos pueblos costeros.<br></li>
            <li>Paseos escénicos por los acantilados.<br></li>
          </ul>
          <p>Tu viaje a la Costa Amalfitana, Italia, será una experiencia de lujo y autenticidad en uno de los destinos más hermosos de Europa.</p>
          <a href="formulario.html">Solicitar Presupuesto</a>
        </div>

        <div class="offert">
          <img src="../assets/images/playaTailandia.jpg" alt="Playas Paradisíacas de Tailandia">
          <h3>Playas Paradisíacas, Tailandia</h3>
          <p>Sumérgete en la belleza tropical de Tailandia con nuestro paquete a las Playas Paradisíacas. Descubre aguas cristalinas, playas de arena blanca y una cultura rica y fascinante durante 7 días y 6 noches en este paraíso tailandés.</p>
          <p>Algunas de las experiencias que podrás disfrutar en este increíble viaje incluyen:</p>
          <ul>
            <li>Exploración de islas cercanas en kayak.<br></li>
            <li>Clases de cocina tailandesa.<br></li>
            <li>Relajación en spa de lujo con masajes tradicionales tailandeses.<br></li>
            <li>Buceo en arrecifes de coral coloridos.<br></li>
            <li>Visitas a mercados locales.<br></li>
            <li>Excursiones a templos budistas impresionantes.<br></li>
          </ul>
          <p>Tu viaje a las Playas Paradisíacas de Tailandia será una experiencia inolvidable llena de relajación, aventuras submarinas y momentos culturales únicos.</p>
          <a href="formulario.html">Solicitar Presupuesto</a>
        </div>

      </section>
</template>
  
<script>
export default {
  name: 'RelaxComponent',
}
</script>
  
<style scoped>
/* Estilos específicos de la oferta */
.offerts {
  text-align: center;
  margin-top: 20px;
}

.offert {
  /*background-color: var(--color-primary);*/
  background: rgb(23, 70, 162);
  background: linear-gradient(90deg, var(--color-primary) 0%, var(--color-secondary) 35%, var(--color-background) 100%);
  color: #fff;
  padding: 20px;
  margin: 20px;
  border-radius: 10px;
  display: inline-block;
  width: calc(33.33% - 40px);
  opacity: .8;

}

.offert h3 {
  font-size: 1.5rem;
  margin: 10px 0;
  animation: cambiaColor 3s linear infinite alternate;
  -webkit-animation: cambiaColor 3s linear infinite alternate;
}

.offert p {
  font-size: 1rem;
  margin: 10px 0;
}

.offert a {
  color: var(--color-accent);
  text-decoration: none;
  font-weight: bold;
}

.logo img {
  max-width: 100px;
  /* Tamaño máximo del logo en píxeles */
  height: auto;

}

/* Estilos para la sección de ofertas */



.offert img {
  max-width: 100%;
  /* Ajusta el ancho máximo al 100% para que todas las imágenes se redimensionen automáticamente */
  height: auto;
  /* Ajusta la altura automáticamente para mantener la proporción */
  width: 100%;
  /* Añade esto para asegurarte de que el ancho sea del 100% del contenedor */
  max-height: 200px;
  /* Establece la altura máxima deseada en píxeles */
}

@keyframes cambiaColor {
  0% {
    color: #0404ff;
  }

  50% {
    color: #fdfdf8
  }

  100% {
    color: #0f0102;
  }
}

/* Aplicar animación de vibración al hacer hover sobre las ofertas */
.offert:hover {
  animation: vibrar 0.3s;
  opacity: 1;
}</style>
  