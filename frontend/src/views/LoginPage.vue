<template>
  <div class="login-container">
    <h1>Connexion</h1>
    <form @submit.prevent="login">
      <div class="input-group">
        <label for="username">Nom d'utilisateur:</label>
        <input
          type="text"
          id="username"
          v-model="username"
          placeholder="Entrez votre nom d'utilisateur"
          required
        />
      </div>

      <div class="input-group">
        <label for="password">Mot de passe:</label>
        <input
          type="password"
          id="password"
          v-model="password"
          placeholder="Entrez votre mot de passe"
          required
        />
      </div>

      <button type="submit">Se connecter</button>

      <div class="form-footer">
        <p>Vous n'avez pas de compte ? <router-link to="/register">S'inscrire</router-link></p>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      console.log('Tentative de connexion', this.username, this.password);

      axios.post('http://127.0.0.1:8000/api/login/', {
        username: this.username,
        password: this.password
      }, {
        withCredentials: true
      })
      .then(response => {
        console.log('Connexion réussie', response);
        this.$router.push("/home");
      })
      .catch(error => {
        console.error('Erreur lors de la connexion', error);
      });
    }
  }
};
</script>

<style scoped>
.login-container {
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

button:hover {
  background-color: #0056b3;
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
