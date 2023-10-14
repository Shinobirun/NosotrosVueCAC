<template>
    <section class="offerts">
        <h2>Tours Románticos</h2>

        <div class="offert">
          <img src="../assets/images/torre.jpg" alt="Francia">
          <h3>Escapada romántica a París, Francia</h3>
          <p>Experimenta una escapada romántica inolvidable en la ciudad del amor, París, Francia, durante 5 días y 4 noches en un hotel boutique con servicios de excelencia y vista a la Torre Eiffel.</p>
          <p>Algunas de las experiencias que podrás disfrutar en este viaje incluyen:</p>
          <ul>
            <li>Cena romántica en un crucero por el río Sena.<br></li>
            <li>Visita a la icónica Torre Eiffel.<br></li>
            <li>Paseo por el encantador barrio de Montmartre.<br></li>
            <li>Degustación de vinos y quesos en una bodega local.<br></li>
            <li>Romántico picnic en los Jardines de Luxemburgo.<br></li>
          </ul>
          <p>Tu escapada romántica a París será una experiencia llena de amor, cultura y momentos inolvidables en la ciudad más romántica y espectacular del mundo.</p>
          <a href="formulario.html">Solicitar Presupuesto</a>
        </div>

        <div class="offert">
          <img src="../assets/images/santoriniGrecia.jpg" alt="Grecia">
          <h3>Aventura en Santorini,<br> Grecia</h3>
          <p>Descubre la emocionante aventura en la hermosa isla de Santorini, Grecia, durante 7 días y 6 noches en una suite con vista al mar en Oia.</p>
          <p>Algunas de las experiencias que podrás disfrutar en este viaje incluyen:</p>
          <ul>
            <li>Tour en velero alrededor de la caldera.<br></li>
            <li>Cata de vinos en encantadores viñedos locales.<br></li>
            <li>Cena en una auténtica taberna griega.<br></li>
            <li>Relajación en las pintorescas playas de arena negra.<br></li>
            <li>Exploración de antiguos sitios arqueológicos griegos.<br></li>
          </ul>
          <p>Tu aventura en Santorini será una experiencia emocionante llena de cultura, belleza natural y momentos inolvidables en esta joya del Mar Egeo.</p>
          <a href="formulario.html">Solicitar Presupuesto</a>
        </div>

        <div class="offert">
          <img src="../assets/images/boraBora.jpg" alt="Polinesia Francesa">
          <h3>Experiencia tropical en Bora Bora, Polinesia Francesa</h3>
          <p>Experimenta la belleza tropical de Bora Bora, Polinesia Francesa, durante 8 días y 7 noches. Disfruta de un alojamiento de lujo en un bungalow sobre el agua en un resort de renombre.</p>
          <p>Algunas de las experiencias que podrás disfrutar en este viaje incluyen:</p>
          <ul>
            <li>Snorkeling en aguas cristalinas.<br></li>
            <li>Cena privada en la playa.<br></li>
            <li>Masajes en pareja en un spa de renombre.<br></li>
            <li>Emocionante excursión en helicóptero.<br></li>
            <li>Kayak en las tranquilas lagunas de Bora Bora.<br></li>
            <li>Exploración de la cultura local y artesanía en mercados.<br></li>
          </ul>
          <p>Tu experiencia en Bora Bora será un viaje inolvidable lleno de aventuras tropicales y momentos románticos en uno de los destinos más hermosos del mundo.</p>
          <a href="formulario.html">Solicitar Presupuesto</a>
        </div>

        <div class="offert">
          <img src="../assets/images/praga.jpg" alt="Praga">
          <h3>Encanto histórico en Praga, República Checa</h3>
          <p>Experimenta el encanto histórico de Praga, República Checa, durante 6 días y 5 noches. Disfruta de un alojamiento de boutique en el casco antiguo de Praga.</p>
          <p>Algunas de las actividades incluidas en este paquete incluyen:</p>
          <ul>
            <li>Visita al castillo de Praga.<br></li>
            <li>Recorrido en carruaje por las calles adoquinadas.<br></li>
            <li>Cena en un restaurante medieval con musica en vivo.<br></li>
            <li>Paseo en barco por el río Moldava.<br></li>
            <li>Exploración de la arquitectura gótica y barroca de la ciudad.<br></li>
            <li>Visitas a museos y galerías de arte.<br></li>
          </ul>
          <p>Tu viaje a Praga te llevará a través de la rica historia y la belleza arquitectónica de esta encantadora ciudad europea.</p>
          <a href="formulario.html">Solicitar Presupuesto</a>
        </div>

      </section>
</template>
  
<script>
export default {
  name: 'RomanticComponent',
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
  
