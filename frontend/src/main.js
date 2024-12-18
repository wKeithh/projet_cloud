import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import 'vuetify/dist/vuetify.min.css';
import '@mdi/font/css/materialdesignicons.css';

export const CyberDocTheme = {
    colors: {
      primary: '#007bff', // Blue
      secondary: '#d1e7ff', // Clearer Blue
      accent: '#0056b3', // Darker blue
      error: '#ff1100', // Red
      info: '#7da2ff', // Lighter Blue
      success: '#008000', // Green
      warning: '#ffcc00', // Orange
      background: '#f8f8f8', // Light Gray
      text: '#000000', // Dark Blue
    },
  }

const vuetify = createVuetify({
    components,
    directives,
    theme: {
      defaultTheme: 'CyberDocTheme',
      themes: { CyberDocTheme },
    },
    icons: {
        defaultSet: 'mdi', // Utiliser Material Design Icons
    },
  })


const app = createApp(App)
app.use(router)
app.use(vuetify)
app.mount('#app')
