import axios from 'axios';

const BASE_URL = process.env.VUE_APP_API_BASE_URL || 'http://127.0.0.1:8000/api';

const axiosInstance = axios.create({
  baseURL: BASE_URL,
});

axiosInstance.interceptors.request.use(
  (config) => {
    const token = sessionStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    config.headers['Content-Type'] = 'application/json'; // Agrega esta línea
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default axiosInstance;

