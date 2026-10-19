import { defineConfig } from 'vite'
import { react } from '@vitejs/plugin-react'

// https://vitejs.dev
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    host: true
  }
})
