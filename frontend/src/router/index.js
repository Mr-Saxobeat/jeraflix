import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Watchlist from "../views/Watchlist.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/watchlist/",
    name: "Watchlist",
    component: Watchlist
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
