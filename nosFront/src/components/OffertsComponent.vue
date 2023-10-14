<template>
    <section class="offerts">
      <h2>Ofertas de Paquetes Turísticos</h2>
      <div v-for="(oferta, index) in ofertas" :key="index" class="offert">
        <img :src="oferta.imagen" :alt="'Oferta ' + (index + 1)">
        <h3>{{ oferta.titulo }}</h3>
        <p>{{ oferta.descripcion }}</p>
        <button @click="verDetalles(oferta)">Ver más</button>
      </div>
    </section>
  </template>
  
<script>
   export default {
  name: 'OffertComponent',
  data() {
    return {
      ofertas: [
        {
          titulo: 'Tours Aventura',
          descripcion: 'Descubre la emoción en destinos épicos de todo el mundo con nuestra irresistible oferta de aventura.',
          imagen: require('@/assets/images/turismoavent1.jpg')
        },
        {
          titulo: 'Tours Relax',
          descripcion: 'Relájate y rejuvenece en destinos paradisíacos disfrutando la serenidad de la naturaleza.',
          imagen: require('@/assets/images/relaxplay2.jpg')
        },
        {
          titulo: 'Tours Aventura Plus',
          descripcion: 'Embárcate en emocionantes aventuras alrededor del mundo y descubre lugares asombrosos.',
          imagen: require('@/assets/images/avent2playa.jpg')
        },
        {
          titulo: 'Tours Románticos',
          descripcion: 'Experimenta momentos inolvidables en lugares románticos y déjate abrazar por la magia del amor',
          imagen: require('@/assets/images/romantplaya.jpg')
        },
        {
          titulo: 'Tours Playa',
          descripcion: 'Relájate en las playas más paradisíacas del mundo, donde el sol y el mar te esperan.',
          imagen: require('@/assets/images/playa.jpg')
        },
        {
          titulo: 'Tours Pesca de Altura',
          descripcion: 'Sumérgete en la rica cultura e historia de diversos lugares, explorando fascinantes tradiciones',
          imagen: require('@/assets/images/pesca.jpg')
        }
        
        // Agrega más ofertas según sea necesario
      ]
    };
  },
  methods: {
    verDetalles(oferta) {
      console.log('Ruta de la imagen:', oferta.imagen);
      this.$emit('ver-detalles', oferta);
    }
  }
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
        background: rgb(23,70,162);
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
        height: auto;
        
    }


 
   

    .offert img {
        max-width: 100%;
        height: auto;
        width: 100%; 
        max-height: 200px;

    @keyframes cambiaColor {
        0% {
          color:#0404ff;
        }

        50% {
            color:#fdfdf8
        }
       
        100% {
          color:#0f0102;
        }
      }
    }

  
    .offert:hover {
         
        opacity: 1;
    }

    .offert button {
      color: var(--color-primary);
            text-decoration: none;
            font-weight: bold;
    }

    .offert button :hover {
      color: var(--color-primary);
            text-decoration: none;
            font-weight: bold;
    }
   
  
  </style>