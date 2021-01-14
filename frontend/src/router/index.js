import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Watchlist from "../views/Watchlist.vue"
import Watchedlist from "../views/Watchedlist.vue"
import Search from "../views/Search.vue"

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
  },
  {
    path: "/watched/",
    name: "Watchedlist",
    component: Watchedlist
  },
  {
    path: "/search/",
    name: "Search",
    component: Search
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
