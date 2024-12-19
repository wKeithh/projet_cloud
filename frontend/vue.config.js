// vue.config.js
module.exports = {
  transpileDependencies: [], // Il doit être un tableau (vide si aucune dépendance à transpiler)

  devServer: {
    port: 8080,
    proxy: {
      '/api': {
        target: process.env.VUE_APP_API_BASE_URL || 'http://127.0.0.1:8000', // Backend IP
        changeOrigin: true,
        secure: false,
      },
    },
  },

  configureWebpack: {
    plugins: [],
  },
};
