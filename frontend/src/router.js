import { createRouter, createWebHistory } from 'vue-router';

// Dummy components for now
const Login = () => import('./pages/auth/Login.vue');
const Register = () => import('./pages/auth/Register.vue');
const Dashboard = () => import('./pages/dashboard/Dashboard.vue');
const CourseList = () => import('./pages/courses/CourseList.vue');
const CreateCourse = () => import('./pages/courses/CreateCourse.vue');
const AssignmentList = () => import('./pages/assignments/AssignmentList.vue');
const UsersList = () => import('./pages/admin/UsersList.vue');

const routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/login', name: 'Login', component: Login, meta: { guest: true } },
  { path: '/register', name: 'Register', component: Register, meta: { guest: true } },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/courses', name: 'Courses', component: CourseList, meta: { requiresAuth: true } },
  { path: '/courses/create', name: 'CreateCourse', component: CreateCourse, meta: { requiresAuth: true } },
  { path: '/assignments', name: 'Assignments', component: AssignmentList, meta: { requiresAuth: true } },
  { path: '/users', name: 'Users', component: UsersList, meta: { requiresAuth: true } },
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
