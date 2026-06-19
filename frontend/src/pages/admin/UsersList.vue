<template>
  <div class="flex h-screen bg-surface-offwhite dark:bg-surface-bgDark font-sans transition-colors duration-200">
    <Sidebar />
    <div class="flex-1 flex flex-col overflow-hidden">
      <Navbar />
      <main class="flex-1 overflow-y-auto p-6 lg:p-8">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-8 gap-4">
          <h1 class="text-[24px] font-semibold text-ink-dark dark:text-surface-light">Global User Management</h1>
          <div class="flex gap-3 w-full sm:w-auto">
            <BaseInput v-model="searchQuery" placeholder="Search users by name or email..." class="w-full sm:w-64" />
            <select v-model="roleFilter" class="px-3 py-2 text-[15px] rounded-md border border-ink-lightest dark:border-ink-mid bg-surface-light text-ink-dark dark:bg-surface-dark dark:text-ink-lightest focus:border-brand-accent focus:ring-2 focus:ring-brand-accent/20 outline-none transition-all duration-150">
              <option value="">All Roles</option>
              <option value="student">Student</option>
              <option value="teacher">Teacher</option>
              <option value="admin">Admin</option>
            </select>
            <BaseButton variant="primary">Add User</BaseButton>
          </div>
        </div>
        
        <div v-if="loading" class="flex justify-center py-10">
          <svg class="animate-spin h-8 w-8 text-brand-accent" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
        </div>
        
        <div v-else class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid overflow-hidden">
          <div class="overflow-x-auto">
            <table class="w-full text-left text-[14px]">
              <thead class="bg-surface-offwhite dark:bg-surface-dark text-ink-light dark:text-ink-mutedDark border-b border-ink-lightest dark:border-ink-mid">
                <tr>
                  <th class="px-6 py-4 font-medium uppercase tracking-wider text-[12px]">Name</th>
                  <th class="px-6 py-4 font-medium uppercase tracking-wider text-[12px]">Email</th>
                  <th class="px-6 py-4 font-medium uppercase tracking-wider text-[12px]">Role</th>
                  <th class="px-6 py-4 font-medium uppercase tracking-wider text-[12px]">Status</th>
                  <th class="px-6 py-4 font-medium uppercase tracking-wider text-[12px] text-right">Actions</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-ink-lightest dark:divide-ink-mid text-ink-dark dark:text-surface-light">
                <!-- Fallback to mock data to show styling since API isn't built yet -->
                <tr v-for="u in filteredUsers" :key="u.id" class="hover:bg-surface-offwhite dark:hover:bg-ink-dark transition-colors even:bg-surface-offwhite/50 dark:even:bg-surface-dark">
                  <td class="px-6 py-4 whitespace-nowrap font-medium">{{ u.full_name }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-ink-mid dark:text-ink-mutedDark">{{ u.email }}</td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <span class="px-2 py-1 rounded text-[12px] font-medium uppercase tracking-wide bg-ink-lightest text-ink-dark dark:bg-ink-mid dark:text-surface-light">
                      {{ u.role }}
                    </span>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <span class="px-2 py-1 rounded text-[12px] font-medium uppercase tracking-wide" :class="u.is_active ? 'bg-alert-success/10 text-alert-success' : 'bg-alert-error/10 text-alert-error'">
                      {{ u.is_active ? 'Active' : 'Suspended' }}
                    </span>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-right space-x-2">
                    <BaseButton variant="outline" size="sm" @click="impersonate(u)">Impersonate</BaseButton>
                    <BaseButton variant="danger" size="sm" @click="resetPassword(u)">Reset Password</BaseButton>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <!-- Pagination Mock -->
          <div class="px-6 py-4 border-t border-ink-lightest dark:border-ink-mid flex items-center justify-between bg-surface-offwhite dark:bg-surface-dark">
            <span class="text-[13px] text-ink-mid dark:text-ink-mutedDark">Showing 1 to {{ filteredUsers.length }} of 1,240 users</span>
            <div class="flex gap-2">
              <BaseButton variant="secondary" size="sm" disabled>Previous</BaseButton>
              <BaseButton variant="secondary" size="sm">Next</BaseButton>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import Navbar from '../../components/Navbar.vue';
import Sidebar from '../../components/Sidebar.vue';
import BaseInput from '../../components/ui/BaseInput.vue';
import BaseButton from '../../components/ui/BaseButton.vue';
import apiClient from '../../api';

const searchQuery = ref('');
const roleFilter = ref('');
const loading = ref(true);

// Mock data since endpoint isn't fully built yet
const users = ref([
  { id: 1, full_name: 'Admin User', email: 'admin@system.com', role: 'admin', is_active: true },
  { id: 2, full_name: 'John Teacher', email: 'john@gtu.edu', role: 'teacher', is_active: true },
  { id: 3, full_name: 'Jane Student', email: 'jane@gtu.edu', role: 'student', is_active: false },
  { id: 4, full_name: 'Mark Student', email: 'mark@gtu.edu', role: 'student', is_active: true },
]);

onMounted(async () => {
  try {
    // const response = await apiClient.get('/admin/users');
    // users.value = response.data.data;
    
    // Simulate network
    setTimeout(() => { loading.value = false; }, 500);
  } catch (error) {
    console.error("Failed to load users", error);
    loading.value = false;
  }
});

const filteredUsers = computed(() => {
  let filtered = users.value;
  if (roleFilter.value) {
    filtered = filtered.filter(u => u.role === roleFilter.value);
  }
  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase();
    filtered = filtered.filter(u => u.full_name.toLowerCase().includes(q) || u.email.toLowerCase().includes(q));
  }
  return filtered;
});

const impersonate = (user) => {
  alert(`Impersonating ${user.full_name}...`);
};

const resetPassword = (user) => {
  alert(`Password reset link sent to ${user.email}`);
};
</script>
