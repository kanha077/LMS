import { createRouter, createWebHistory } from 'vue-router';

const Dashboard = () => import('./pages/Dashboard.vue');
const CourseBuilder = () => import('./pages/CourseBuilder.vue');
const Analytics = () => import('./pages/Analytics.vue');
const StudentView = () => import('./pages/StudentView.vue');
const Login = () => import('./pages/auth/Login.vue');
const Register = () => import('./pages/auth/Register.vue');
const Landing = () => import('./pages/Landing.vue');

const routes = [
  { path: '/', name: 'Landing', component: Landing, meta: { guest: true } },
  { path: '/login', name: 'Login', component: Login, meta: { guest: true } },
  { path: '/register', name: 'Register', component: Register, meta: { guest: true } },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/dashboard/course-builder', name: 'CourseBuilder', component: CourseBuilder, meta: { requiresAuth: true } },
  { path: '/dashboard/analytics', name: 'Analytics', component: Analytics, meta: { requiresAuth: true } },
  { path: '/courses/:id/player', name: 'StudentView', component: StudentView, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('token');
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login');
  } else if (to.meta.guest && isAuthenticated) {
    next('/dashboard');
  } else {
    next();
  }
});

export default router;
