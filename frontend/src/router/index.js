import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/LoginPage.vue";
import Register from "../views/RegisterPage.vue";
import Home from "../views/HomePage.vue";
import EditDocument from "../views/EditDocument.vue";

const routes = [
  { path: "/", redirect: "/login" },
  { path: "/login", component: Login },
  { path: "/register", component: Register },
  { path: "/home", component: Home },
  { path: "/documents/:id", component: EditDocument },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
