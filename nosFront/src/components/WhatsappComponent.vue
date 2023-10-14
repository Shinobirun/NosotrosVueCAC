<template>      
<div class="whatsapp-button">
    <a href="https://api.whatsapp.com/send?phone=1167126268" target="_blank">
     <img src="../assets/images/icons/Whatsapp_37229.png   " alt="WhatsApp">
    </a>
  </div>
    
</template>



<script>
  export default {
    name: 'WhatsappComponent'

    
  }

  
  </script>


<style scoped>

.whatsapp-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
}

.whatsapp-button img {
  width: 50px; 
}

</style>