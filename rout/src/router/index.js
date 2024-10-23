import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import JobsView from "@/views/jobs/JobsView.vue";
import JobDetails from "@/views/jobs/JobDetails.vue";
import NotFound from "@/views/NotFound.vue";
import SignupView from "@/views/SignupView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
  },
  {
    path: "/jobs",
    name: "jobs",
    component: JobsView,
  },
  {
    path: "/jobs/details/:id?",
    name: "jobdetail",
    component: JobDetails,
    props: true,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignupView,
  },
  {
    path: "/all-jobs",
    redirect: "/jobs",
  },
  //catchall 404
  {
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: NotFound,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
