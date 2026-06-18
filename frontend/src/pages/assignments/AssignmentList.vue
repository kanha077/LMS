<template>
  <div class="flex h-screen bg-gray-50 font-sans">
    <Sidebar />
    <div class="flex-1 flex flex-col overflow-hidden">
      <Navbar />
      <main class="flex-1 overflow-y-auto p-6 lg:p-8">
        <div class="flex justify-between items-center mb-8">
          <h1 class="text-2xl font-semibold text-gray-900">Assignments</h1>
          <button v-if="role === 'teacher' || role === 'admin'" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md font-medium text-sm transition-colors shadow-sm">
            + Create Assignment
          </button>
        </div>
        
        <div v-if="loading" class="flex justify-center py-10">
          <p class="text-gray-500 animate-pulse">Loading assignments...</p>
        </div>
        
        <div v-else-if="assignments.length === 0" class="text-center py-12 bg-white rounded-xl shadow-sm border border-gray-100">
          <p class="text-gray-500 mb-4">No assignments found for your courses.</p>
        </div>

        <div v-else class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
          <ul class="divide-y divide-gray-100">
            <li v-for="assignment in assignments" :key="assignment.id" class="p-6 hover:bg-gray-50 transition-colors">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-lg font-medium text-gray-900">{{ assignment.title }}</h3>
                  <p class="text-sm text-gray-500 mt-1 line-clamp-1">{{ assignment.description }}</p>
                  <p class="text-xs text-gray-400 mt-2">Due: {{ new Date(assignment.due_date).toLocaleString() }} &bull; Points: {{ assignment.total_points }}</p>
                </div>
                <div class="flex flex-col items-end gap-2">
                  <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium" :class="assignment.is_published ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'">
                    {{ assignment.is_published ? 'Published' : 'Draft' }}
                  </span>
                  <button class="text-blue-600 hover:text-blue-800 text-sm font-medium inline-flex items-center mt-2">
                    Submit Work &rarr;
                  </button>
                </div>
              </div>
            </li>
          </ul>
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

const assignments = ref([]);
const loading = ref(true);

const role = computed(() => {
  const userData = localStorage.getItem('user');
  return userData ? JSON.parse(userData).role : 'student';
});

onMounted(async () => {
  try {
    const response = await apiClient.get('/assignments');
    assignments.value = response.data.data || [];
  } catch (error) {
    console.error("Failed to load assignments", error);
  } finally {
    loading.value = false;
  }
});
</script>
