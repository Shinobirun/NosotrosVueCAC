<template>
  <div>
    <form v-if="mode !== 'delete'" @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="titulo">Título:</label>
        <input v-model="formData.titulo" id="titulo" placeholder="Título" required>
      </div>
      <div class="form-group">
        <label for="informacion">Información:</label>
        <textarea v-model="formData.informacion" id="informacion" placeholder="Información" required></textarea>
      </div>
      <div class="form-group">
        <label for="foto_url">Foto URL:</label>
        <input v-model="formData.foto_url" id="foto_url" placeholder="Foto URL" required>
      </div>
      <div class="form-group">
        <label for="precio">Precio:</label>
        <input v-model="formData.precio" type="number" id="precio" placeholder="Precio" required>
      </div>
      <div class="form-group">
        <label for="tipo">Tipo:</label>
        <input v-model="formData.tipo" id="tipo" placeholder="Tipo" required>
      </div>
  
      <button type="submit" v-if="mode === 'add'">Agregar</button>
      <button type="submit" v-else-if="mode === 'edit'">Guardar cambios</button>
    </form>

    <div v-else>
      <button @click="confirmDelete">Confirmar Borrar</button>
      <button @click="switchMode('edit')">Cancelar</button>
    </div>
  </div>
</template>

<script>
import apiService from '@/services/apiService'; // Ajusta la ruta según la ubicación de tu servicio

export default {
  props: {
    mode: {
      type: String,
      required: true,
    },
    selectedPackage: {
      type: Object,
      default: null,
    },
  },
  data() {
    return {
      formData: {
        titulo: '',
        informacion: '',
        foto_url: '',
        precio: 0,
        tipo: '',
      },
    };
  },
  methods: {
    async handleSubmit() {
      try {
        if (this.mode === 'add') {
          await apiService.post('paquetes', this.formData);
        } else if (this.mode === 'edit') {
          // Asumo que hay un campo 'id' en selectedPackage para la edición
          await apiService.put('paquetes', this.selectedPackage.id, this.formData);
        }
        this.resetFormAndSwitchMode('add');
      } catch (error) {
        console.error('Error al procesar la solicitud:', error);
        // Manejar el error de manera adecuada en tu aplicación
      }
    },

    async confirmDelete() {
      try {
        // Asumo que hay un campo 'id' en selectedPackage para la eliminación
        await apiService.delete('paquetes', this.selectedPackage.id);
        this.$emit('deletePackage');
        this.resetFormAndSwitchMode('add');
      } catch (error) {
        console.error('Error al procesar la solicitud de eliminación:', error);
        // Manejar el error de manera adecuada en tu aplicación
      }
    },

    resetForm() {
      this.formData = {
        titulo: '',
        informacion: '',
        foto_url: '',
        precio: 0,
        tipo: '',
      };
    },
    
    resetFormAndSwitchMode(newMode) {
      this.resetForm();
      this.$emit('switchMode', newMode);
    },
  },
};
</script>

<style scoped>
  .form-group {
    margin-bottom: 15px;
  }
</style>