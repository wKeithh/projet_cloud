import axios from 'axios';

// Déclare l'instance api à l'extérieur de la condition pour qu'elle soit toujours disponible
let api;

// Vérification si la variable d'environnement est définie
if (!process.env.VUE_APP_API_BASE_URL) {
  console.error('Erreur : La variable d\'environnement VUE_APP_API_BASE_URL n\'est pas définie.');
} else {
  api = axios.create({
    baseURL: process.env.VUE_APP_API_BASE_URL,
  });
}

export default api;
