<template>
  <div class="w-64 bg-gray-900 min-h-screen text-white flex flex-col shadow-xl">
    <div class="h-16 flex items-center px-6 border-b border-gray-800">
      <span class="text-sm font-semibold tracking-wider text-gray-400 uppercase">{{ role }} Panel</span>
    </div>
    <div class="flex-1 px-4 py-6 space-y-2">
      <router-link to="/dashboard" class="block px-4 py-2.5 rounded-lg hover:bg-gray-800 transition-colors" active-class="bg-blue-600 hover:bg-blue-600 font-medium shadow-md">Dashboard</router-link>
      <router-link to="/courses" class="block px-4 py-2.5 rounded-lg hover:bg-gray-800 transition-colors" active-class="bg-blue-600 hover:bg-blue-600 font-medium shadow-md">Courses</router-link>
      <router-link to="/assignments" class="block px-4 py-2.5 rounded-lg hover:bg-gray-800 transition-colors" active-class="bg-blue-600 hover:bg-blue-600 font-medium shadow-md">Assignments</router-link>
      <router-link v-if="role === 'admin'" to="/users" class="block px-4 py-2.5 rounded-lg hover:bg-gray-800 transition-colors" active-class="bg-blue-600 hover:bg-blue-600 font-medium shadow-md">Users</router-link>
      <router-link v-if="role === 'admin'" to="/settings" class="block px-4 py-2.5 rounded-lg hover:bg-gray-800 transition-colors" active-class="bg-blue-600 hover:bg-blue-600 font-medium shadow-md">Settings</router-link>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useAuthStore } from '../stores/auth';

const authStore = useAuthStore();
const role = computed(() => authStore.role);
</script>
