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
  
      <button class="submit-button" type="submit" v-if="mode === 'add'">Agregar</button>
      <button class="submit-button" type="submit" v-else-if="mode === 'edit'">Guardar cambios</button>
    </form>

    <div v-else>
      <button class="delete-button" @click="confirmDelete">Confirmar Borrar</button>
      <button class="cancel-button" @click="switchMode('edit')">Cancelar</button>
    </div>
  </div>
</template>

<script>
import apiService from '@/services/apiService'; 
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
    switchMode: {
      type: Function, 
      required: true,
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
  watch: {
    selectedPackage: {
      handler: 'updateFormData',
      immediate: true,
    },
  },
  methods: {
    async handleSubmit() {
      try {
        if (this.mode === 'add') {
          await apiService.post('paquetes', this.formData);
        } else if (this.mode === 'edit') {
          
          await apiService.put('paquetes', this.selectedPackage.id, this.formData);
        }
        this.resetFormAndSwitchMode('add');
      } catch (error) {
        console.error('Error al procesar la solicitud:', error);
        
      }
    },

    updateFormData() {
    if (this.selectedPackage) {
      
      if (this.mode === 'edit') {
        this.formData = { ...this.selectedPackage };
      } else {
        
        this.formData = {
          id: this.selectedPackage.id,
          titulo: '',
          informacion: '',
          foto_url: '',
          precio: 0,
          tipo: '',
        };
      }
    }
  },

    async confirmDelete() {
      try {
        
        await apiService.delete('paquetes', this.selectedPackage.id);
        this.$emit('deletePackage');
        this.resetFormAndSwitchMode('add');
      } catch (error) {
        console.error('Error al procesar la solicitud de eliminación:', error);
        
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

  .submit-button,
  .delete-button,
  .cancel-button {
    display: inline-block;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s;
    margin-right:5px ;
    margin-bottom: 5px;
  }

  .submit-button {
    background-color: #4caf50;
    color: white;
    border: none;
  }

  .delete-button {
    background-color: #f44336;
    color: white;
    border: none;
  }

  .cancel-button {
    background-color: #2196f3;
    color: white;
    border: none;
  }

  .submit-button:hover,
  .delete-button:hover,
  .cancel-button:hover {
    background-color: #45a049;
  }
</style>
