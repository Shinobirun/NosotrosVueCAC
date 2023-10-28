import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/'; // Reemplaza con tu URL base

export default {
  // Función para hacer una solicitud GET
  get(resource) {
    return axios.get(`${BASE_URL}/${resource}`);
  },

  // Función para hacer una solicitud POST
  post(resource, data) {
    return axios.post(`${BASE_URL}/${resource}`, data);
  },

  // Función para hacer una solicitud PUT
  put(resource, data) {
    return axios.put(`${BASE_URL}/${resource}`, data);
  },

  // Función para hacer una solicitud DELETE
  delete(resource) {
    return axios.delete(`${BASE_URL}/${resource}`);
  },
};