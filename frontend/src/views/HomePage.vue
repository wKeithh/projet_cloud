<template>
  <v-card>
    <v-layout>
      <!-- Navigation Drawer -->
      <v-navigation-drawer class="bg-deep-purple" theme="dark" permanent>
        <!-- Titre de l'application -->
        <v-list>
          <v-list-item title="Application Cloud" subtitle="Keith & Rania"></v-list-item>
        </v-list>

        <!-- Bouton Ajouter un document -->
        <div class="pa-2">
          <v-btn block color="primary" @click="createDocument">
            Ajouter un document
          </v-btn>
        </div>

        <!-- Liste des documents avec actions -->
        <div style="flex: 1; overflow-y: auto;">
          <v-list>
            <v-list-item
              v-for="document in filteredDocuments"
              :key="document.id"
              :subtitle="document.subtitle"
              :title="document.title"
              @click="openDocument(document.id)"
            >

                <template v-slot:append>
                  <v-btn variant="plain" icon="mdi-delete" @click="deleteDocument(document.id)" color="red"> </v-btn>
                </template>

            </v-list-item>
          </v-list>
        </div>

        <!-- Bouton Logout -->
        <div class="pa-2">
          <v-btn block color="error" @click="logout">
            Logout
          </v-btn>
        </div>
      </v-navigation-drawer>

      <!-- Main content -->
      <v-main>
        <v-container>
          <!-- Affiche un document sélectionné -->
          <v-card v-if="currentDocument">
            <v-card-title>
              <v-text-field
                v-model="currentDocument.title"
                label="Titre"
                outlined
                dense
              ></v-text-field>
            </v-card-title>
            <v-card-text>
              <p>Créé par : {{ currentDocument.owner }}</p>
              <p>Date de création : {{ currentDocument.created_at }}</p>

              <!-- Champ d'édition -->
              <v-textarea
                v-model="currentDocument.content"
                label="Modifier le contenu"
                rows="10"
                outlined
              ></v-textarea>
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" @click="saveDocument">Enregistrer</v-btn>
              <v-btn color="secondary" @click="cancelEdit">Annuler</v-btn>
            </v-card-actions>
          </v-card>

          <!-- Message si aucun document n'est sélectionné -->
          <v-card v-else>
            <v-card-text>
              <p>Sélectionnez un document pour afficher son contenu.</p>
            </v-card-text>
          </v-card>
        </v-container>
      </v-main>
    </v-layout>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      documents: [], // Tous les documents
      searchQuery: "", // Filtrer les documents
      currentDocument: null, // Document actuellement sélectionné
      originalContent: null, // Sauvegarde temporaire pour annuler les modifications
    };
  },
  computed: {
    filteredDocuments() {
      return this.documents.filter((doc) => {
        return (
          doc.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          doc.owner.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      });
    },
  },
  async created() {
    await this.fetchDocuments();
  },
  methods: {
    async fetchDocuments() {
      try {
        const response = await axios.get("api/documents/");
        this.documents = response.data;
      } catch (error) {
        alert("Échec du chargement des documents");
      }
    },
    async createDocument() {
      try {
        const response = await axios.post("api/documents/", {
          title: "Nouveau Document",
          owner: "Utilisateur actuel",
          created_at: new Date().toISOString(),
          content: "Contenu vide",
        });
        this.documents.push(response.data);
      } catch (error) {
        alert("Échec de la création du document");
      }
    },
    openDocument(id) {
      this.currentDocument = this.documents.find((doc) => doc.id === id);
      this.originalContent = this.currentDocument.content; // Sauvegarde de l'état initial
    },
    async saveDocument() {
      try {
        await axios.put(`api/documents/${this.currentDocument.id}/`, {
          title: this.currentDocument.title,
          content: this.currentDocument.content,
        });
        alert("Document sauvegardé !");
      } catch (error) {
        alert("Échec de la sauvegarde du document");
      }
    },
    cancelEdit() {
      if (this.currentDocument) {
        this.currentDocument.content = this.originalContent; // Rétablit l'état initial
      }
    },
    async deleteDocument(id) {
      try {
        await axios.delete(`api/documents/${id}/`);
        this.documents = this.documents.filter((doc) => doc.id !== id);
        alert("Document supprimé !");
        if (this.currentDocument?.id === id) {
          this.currentDocument = null;
        }
      } catch (error) {
        alert("Échec de la suppression du document");
      }
    },
    renameDocument(document) {
      const newTitle = prompt("Nouveau titre :", document.title);
      if (newTitle && newTitle.trim() !== "") {
        document.title = newTitle.trim();
        this.saveDocument(); // Sauvegarder directement après modification
      }
    },
    logout() {
      console.log("Tentative de déconnexion");

      axios.post('http://127.0.0.1:8000/api/logout/', {}, {
        withCredentials: true
      })
      .then(response => {
        console.log('Déconnexion réussie', response);
        // Rediriger vers la page de connexion ou une autre page appropriée
        this.$router.push("/login");
      })
      .catch(error => {
        console.error('Erreur lors de la déconnexion', error);
      });
    }
  },
};
</script>

<style scoped>
.clickable {
  cursor: pointer;
}
.text-error {
  color: red;
}
</style>
