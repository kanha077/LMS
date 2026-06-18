<template>
  <div class="flex h-screen bg-gray-50 font-sans">
    <Sidebar />
    <div class="flex-1 flex flex-col overflow-hidden">
      <Navbar />
      <main class="flex-1 overflow-y-auto p-6 lg:p-8">
        <h1 class="text-2xl font-semibold text-gray-900 mb-8 capitalize">{{ role }} Dashboard</h1>
        
        <StudentDashboard v-if="role === 'student'" />
        <TeacherDashboard v-else-if="role === 'teacher'" />
        <AdminDashboard v-else-if="role === 'admin'" />
      </main>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useAuthStore } from '../../stores/auth';
import Navbar from '../../components/Navbar.vue';
import Sidebar from '../../components/Sidebar.vue';
import StudentDashboard from './StudentDashboard.vue';
import TeacherDashboard from './TeacherDashboard.vue';
import AdminDashboard from './AdminDashboard.vue';

const authStore = useAuthStore();
const role = computed(() => authStore.role);
</script>
