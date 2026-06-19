<template>
  <nav class="bg-surface-light dark:bg-surface-dark border-b border-ink-lightest dark:border-ink-mid transition-colors duration-200">
    <div class="w-full px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex items-center gap-4">
          <button @click="uiStore.toggleSidebar" class="p-2 rounded-md text-ink-mid hover:bg-surface-offwhite dark:text-ink-mutedDark dark:hover:bg-ink-mid transition-colors">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
          <div class="flex-shrink-0 flex items-center">
            <span class="text-[24px] font-bold text-brand-accent dark:text-surface-light">LMS</span>
          </div>
        </div>
        <div class="flex items-center gap-4">
          <button @click="uiStore.toggleDarkMode" class="p-2 rounded-md text-ink-mid hover:bg-surface-offwhite dark:text-ink-mutedDark dark:hover:bg-ink-mid transition-colors" title="Toggle Dark Mode">
            <svg v-if="uiStore.isDarkMode" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
            </svg>
            <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
            </svg>
          </button>
          <span class="text-[15px] text-ink-mid dark:text-ink-lightest hidden sm:inline-block">Hello, {{ user?.full_name || 'User' }}</span>
          <BaseButton variant="outline" size="sm" @click="handleLogout">Logout</BaseButton>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import { useUIStore } from '../stores/ui';
import BaseButton from './ui/BaseButton.vue';

const router = useRouter();
const authStore = useAuthStore();
const uiStore = useUIStore();

const user = computed(() => authStore.user);

const handleLogout = () => {
  authStore.logout();
  router.push('/login');
};
</script>
