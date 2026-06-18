<template>
  <div class="flex h-screen bg-gray-50 font-sans">
    <Sidebar />
    <div class="flex-1 flex flex-col overflow-hidden">
      <Navbar />
      <main class="flex-1 overflow-y-auto p-6 lg:p-8">
        <div class="flex justify-between items-center mb-8">
          <h1 class="text-2xl font-semibold text-gray-900">Courses</h1>
          <router-link v-if="role === 'teacher' || role === 'admin'" to="/courses/create" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md font-medium text-sm transition-colors shadow-sm">
            + Create Course
          </router-link>
        </div>
        
        <div v-if="loading" class="flex justify-center py-10">
          <p class="text-gray-500 animate-pulse">Loading courses...</p>
        </div>
        
        <div v-else-if="courses.length === 0" class="text-center py-12 bg-white rounded-xl shadow-sm border border-gray-100">
          <p class="text-gray-500 mb-4">No courses found. Get started by creating or enrolling in one!</p>
        </div>

        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="course in courses" :key="course.id" class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-lg transition-all duration-200 transform hover:-translate-y-1">
            <div class="p-6">
              <div class="flex justify-between items-start mb-4">
                <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                  {{ course.code }}
                </span>
                <span v-if="course.semester" class="text-xs text-gray-500 bg-gray-100 px-2 py-0.5 rounded-md">{{ course.semester }}</span>
              </div>
              <h3 class="text-lg font-bold text-gray-900 mb-2 truncate">{{ course.name }}</h3>
              <p class="text-sm text-gray-600 mb-4 line-clamp-2 h-10">{{ course.description || 'No description provided.' }}</p>
              
              <div class="pt-4 border-t border-gray-100 flex justify-end items-center">
                <router-link :to="`/courses/${course.id}`" class="text-blue-600 hover:text-blue-800 font-medium text-sm inline-flex items-center">
                  View Details
                  <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import Navbar from '../../components/Navbar.vue';
import Sidebar from '../../components/Sidebar.vue';
import apiClient from '../../api';

const courses = ref([]);
const loading = ref(true);

const role = computed(() => {
  const userData = localStorage.getItem('user');
  return userData ? JSON.parse(userData).role : 'student';
});

onMounted(async () => {
  try {
    const response = await apiClient.get('/courses');
    courses.value = response.data.data || [];
  } catch (error) {
    console.error("Failed to load courses", error);
  } finally {
    loading.value = false;
  }
});
</script>
