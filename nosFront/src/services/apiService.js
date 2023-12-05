import axios from 'axios';

const BASE_URL = process.env.VUE_APP_API_BASE_URL || 'http://127.0.0.1:8000/api';

export default {
  // Función para hacer una solicitud GET
  get(resource) {
    return axios.get(`${BASE_URL}/${resource}/`);
  },
  
  getPaquetesPorTipo(tipo) {
    return axios.get(`${BASE_URL}/paquetes/`, { params: { tipo: tipo } });
  },
  
  post(resource, data) {
    return axios.post(`${BASE_URL}/${resource}/`, data);
  },
  
  // Modificada para incluir el ID en la URL
  put(resource, id, data) {
    return axios.put(`${BASE_URL}/${resource}/${id}/`, data);
  },
  
  // Modificada para incluir el ID en la URL
  delete(resource, id) {
    return axios.delete(`${BASE_URL}/${resource}/${id}/`);
  },
};
