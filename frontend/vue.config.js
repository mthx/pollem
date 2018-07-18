const djangoBackend = {
  target: 'http://127.0.0.1:8000/',
  changeOrigin: true,
}

module.exports = {
  devServer: {
    proxy: {
      '/api/': djangoBackend,
      '/api-auth/': djangoBackend,
      '/static/rest_framework/': djangoBackend,
    }
  }
}
