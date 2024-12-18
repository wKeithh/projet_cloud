<template>
    <v-container>
      <v-text-field label="Title" v-model="document.title"></v-text-field>
      <v-textarea label="Content" v-model="document.content"></v-textarea>
      <v-btn color="primary" @click="saveDocument">Save</v-btn>
    </v-container>
  </template>

  <script>
  import api from "../services/api";

  export default {
    data() {
      return {
        document: {
          title: "",
          content: "",
        },
      };
    },
    async created() {
      await this.fetchDocument();
    },
    methods: {
      async fetchDocument() {
        const id = this.$route.params.id;
        const response = await api.get(`/documents/${id}/`);
        this.document = response.data;
      },
      async saveDocument() {
        try {
          const id = this.$route.params.id;
          await api.put(`/documents/${id}/`, this.document);
          alert("Document saved successfully!");
        } catch (error) {
          alert("Failed to save document");
        }
      },
    },
  };
  </script>
