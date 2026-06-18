<template>
  <div class="flex h-screen bg-gray-50 font-sans">
    <Sidebar />
    <div class="flex-1 flex flex-col overflow-hidden">
      <Navbar />
      <main class="flex-1 overflow-y-auto p-6 lg:p-8">
        <div class="mb-8 flex items-center gap-4">
          <router-link to="/courses" class="text-gray-500 hover:text-gray-700 bg-white px-3 py-1.5 rounded-md border border-gray-200 shadow-sm transition-colors text-sm font-medium">
            &larr; Back
          </router-link>
          <h1 class="text-2xl font-semibold text-gray-900">Create New Course</h1>
        </div>
        
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 lg:p-8 max-w-3xl">
          <form @submit.prevent="handleCreate" class="space-y-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Course Name *</label>
              <input v-model="form.name" type="text" required class="w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 focus:bg-white transition-all outline-none">
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Course Code *</label>
                <input v-model="form.code" type="text" required placeholder="e.g. CS101" class="w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 focus:bg-white transition-all outline-none">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Semester</label>
                <input v-model="form.semester" type="text" placeholder="e.g. Fall 2026" class="w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 focus:bg-white transition-all outline-none">
              </div>
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
              <textarea v-model="form.description" rows="4" class="w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 focus:bg-white transition-all outline-none"></textarea>
            </div>
            
            <div class="flex justify-end pt-6 mt-6 border-t border-gray-100">
              <button type="submit" :disabled="loading" class="bg-blue-600 hover:bg-blue-700 text-white px-8 py-2.5 rounded-lg font-medium shadow-md transition-all duration-200 hover:-translate-y-0.5 disabled:opacity-50 disabled:transform-none">
                {{ loading ? 'Creating...' : 'Create Course' }}
              </button>
            </div>
          </form>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router';
import Navbar from '../../components/Navbar.vue';
import Sidebar from '../../components/Sidebar.vue';
import apiClient from '../../api';

const router = useRouter();
const loading = ref(false);
const form = reactive({
  name: '',
  code: '',
  description: '',
  semester: ''
});

const handleCreate = async () => {
  loading.value = true;
  try {
    await apiClient.post('/courses', form);
    router.push('/courses');
  } catch (error) {
    alert(error.response?.data?.detail || 'Failed to create course');
  } finally {
    loading.value = false;
  }
};
</script>
