<template>
  <div class="container">
    <img src="../assets/images/registro/404not2.jpg" alt="Pagina no encontrada" class="notFound">
    <span class="loader"></span>
  </div>
</template>

<script>
export default {
  name: "NotFound",
  mounted() {
    setTimeout(() => {
      this.$router.push({ name: "Home" }); // Asegúrate de que "Home" sea el nombre correcto de tu ruta de inicio
    }, 3000); // Espera 5 segundos antes de redirigir
  },
};
</script>

<style scoped>

.container {
  position: relative; /* Establece la posición relativa */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh; /* Esto asegura que el contenedor ocupe toda la altura de la pantalla */
}

.notFound{
  max-width: 100%;  
  
}
.loader {
  
  position: absolute; /* Establece la posición absoluta */
  top: 50%; /* Centra verticalmente */
  left: 50%; /* Centra horizontalmente */
  transform: translate(-50%, -50%); /* Centra completamente */
  transform: rotateZ(45deg);
  perspective: 1000px;
  border-radius: 50%;
  width: 48px;
  height: 48px;
  color: #fff;
  z-index: 1;
  background-color:#e9ddc5;


       
     
       
        
        
       
      }
        .loader:before,
        .loader:after {
          content: '';
          display: block;
          position: absolute;
          top: 0;
          left: 0;
          width: inherit;
          height: inherit;
          border-radius: 50%;
          transform: rotateX(70deg);
          animation: 1s spin linear infinite;
        }
        .loader:after {
          color: #FF3D00;
          transform: rotateY(70deg);
          animation-delay: .4s;
        }

      @keyframes rotate {
        0% {
          transform: translate(-50%, -50%) rotateZ(0deg);
        }
        100% {
          transform: translate(-50%, -50%) rotateZ(360deg);
        }
      }

      @keyframes rotateccw {
        0% {
          transform: translate(-50%, -50%) rotate(0deg);
        }
        100% {
          transform: translate(-50%, -50%) rotate(-360deg);
        }
      }

      @keyframes spin {
        0%,
        100% {
          box-shadow: .2em 0px 0 0px currentcolor;
        }
        12% {
          box-shadow: .2em .2em 0 0 currentcolor;
        }
        25% {
          box-shadow: 0 .2em 0 0px currentcolor;
        }
        37% {
          box-shadow: -.2em .2em 0 0 currentcolor;
        }
        50% {
          box-shadow: -.2em 0 0 0 currentcolor;
        }
        62% {
          box-shadow: -.2em -.2em 0 0 currentcolor;
        }
        75% {
          box-shadow: 0px -.2em 0 0 currentcolor;
        }
        87% {
          box-shadow: .2em -.2em 0 0 currentcolor;
        }
      }
   



 
</style>