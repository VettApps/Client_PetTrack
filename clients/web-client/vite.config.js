import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    host: true, // Permite acceso desde fuera del contenedor
    port: 8080, // Cambiar a 8080 para coincidir con docker-compose
    strictPort: true, // Evita que Vite cambie el puerto si está ocupado
    proxy: {
      '/api': {
        target: 'http://auth-service:8000', // Correcto - usa nombre de servicio Docker
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
        secure: false // Necesario para desarrollo
      }
    }
  }
})