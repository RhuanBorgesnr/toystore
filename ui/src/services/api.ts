import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';
const JWT_TOKEN = process.env.REACT_APP_JWT_TOKEN;

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  if (JWT_TOKEN) {
    console.log('JWT_TOKEN', JWT_TOKEN);
    config.headers.Authorization = `Bearer ${JWT_TOKEN}`;
  }
  return config;
});

export default api; 