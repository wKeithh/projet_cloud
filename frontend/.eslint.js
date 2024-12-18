module.exports = {
  extends: [
    'plugin:vue/vue3-recommended',  // Règles recommandées pour Vue 3
    'eslint:recommended',  // Règles de base pour JavaScript
    'plugin:prettier/recommended',  // Intégration de Prettier
  ],
  parser: '@babel/eslint-parser',  // Utilise Babel pour analyser les fichiers JS
  parserOptions: {
    ecmaVersion: 2020,  // Support des dernières versions de JavaScript
    sourceType: 'module',  // Support des modules ES
  },
  rules: {
    // Ajoute ici tes règles personnalisées si nécessaire
  },
}
