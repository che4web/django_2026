import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const BACKEND_HOST = 'http://127.0.0.1:8000'
const BACKEND_HOST2 = '127.0.0.1:8000'

function proxyBypass(req) {
  if (req.headers && req.headers.referer) {
    req.headers.referer = req.headers.referer.replace('http://127.0.0.1:8080', BACKEND_HOST)
  }
  req.headers.host = req.headers.host.replace('127.0.0.1:8080', BACKEND_HOST2)
}

const proxyOptions = {
  target: BACKEND_HOST,
  ws: true,
  changeOrigin: true,
  bypass: proxyBypass,
}

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 8080,
    host: '127.0.0.1',
    proxy: {
        '^/api': proxyOptions,
        '^/admin': proxyOptions,
        '^/media': proxyOptions,
        '^/static': proxyOptions,
        '^/accounts': proxyOptions,

    },
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})
