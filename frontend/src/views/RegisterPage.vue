<template>
  <div class="register-container">
    <h1>Inscription</h1>
    <form @submit.prevent="register">
      <div class="input-group">
        <label for="username">Nom d'utilisateur:</label>
        <input
          type="text"
          id="username"
          v-model="username"
          @blur="checkUsername"
          required
        />
        <span v-if="usernameTaken" class="error">Ce nom d'utilisateur est déjà pris.</span>
      </div>

      <div class="input-group">
        <label for="password">Mot de passe:</label>
        <input
          type="password"
          id="password"
          v-model="password"
          required
        />
      </div>

      <div class="input-group">
        <label for="confirmPassword">Confirmer le mot de passe:</label>
        <input
          type="password"
          id="confirmPassword"
          v-model="confirmPassword"
          required
        />
        <span v-if="passwordMismatch" class="error">Les mots de passe ne correspondent pas.</span>
      </div>

      <button type="submit" :disabled="isSubmitDisabled">S'enregistrer</button>

      <div class="form-footer">
        <p>Vous avez déjà un compte ? <router-link to="/login">Se connecter</router-link></p>
      </div>
    </form>
  </div>
</template>

<script>
//import axios from "axios"; // Assure-toi que le chemin est correct
import api from '@/services/api'; // '@' fait référence au dossier src

export default {
  data() {
    return {
      username: "",
      password: "",
      confirmPassword: "",
      usernameTaken: false, // Pour vérifier si le nom d'utilisateur existe déjà
      passwordMismatch: false, // Pour vérifier si les mots de passe correspondent
    };
  },
  computed: {
    isSubmitDisabled() {
      // Désactive le bouton si les mots de passe ne correspondent pas ou si le nom d'utilisateur existe déjà
      return this.password !== this.confirmPassword || this.usernameTaken;
    },
  },
  methods: {
    // Vérification si le mot de passe et la confirmation sont les mêmes
    validatePassword() {
      this.passwordMismatch = this.password !== this.confirmPassword;
    },

    // Vérification si l'utilisateur existe déjà
    async checkUsername() {
      if (this.username.trim() === "") {
        this.usernameTaken = false;
        return;
      }

      try {
        const response = await api.get(`api/check-username/${this.username}`);
        this.usernameTaken = response.data.exists; // On suppose que l'API renvoie un objet { exists: true/false }
      } catch (error) {
        console.error("Erreur lors de la vérification du nom d'utilisateur", error);
      }
    },

    // Méthode d'inscription
    async register() {
      if (this.password !== this.confirmPassword) {
        this.passwordMismatch = true;
        return;
      }

      // Vérification avant d'envoyer l'inscription
      if (this.usernameTaken) {
        console.error("Nom d'utilisateur déjà pris.");
        return;
      }

      try {
        const response = await api.post("/api/register/", {
          username: this.username,
          password: this.password,
        });
        console.log("Utilisateur inscrit avec succès", response.data);
        this.$router.push("/login"); // Redirige vers la page de connexion après l'inscription
      } catch (error) {
        console.error("Erreur lors de l'inscription", error);
      }
    },
  },

  watch: {
    // Quand le mot de passe change, on vérifie si les mots de passe correspondent
    password() {
      this.validatePassword();
    },
    confirmPassword() {
      this.validatePassword();
    },
  },
};
</script>

<style scoped>
.register-container {
  width: 300px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f7f7f7;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
}

.input-group {
  margin-bottom: 15px;
}

.input-group label {
  display: block;
  font-weight: bold;
}

.input-group input {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.error {
  color: red;
  font-size: 0.9em;
}

.form-footer {
  text-align: center;
  margin-top: 10px;
}

.form-footer p {
  font-size: 14px;
}

.form-footer a {
  color: #007bff;
  text-decoration: none;
}
</style>
