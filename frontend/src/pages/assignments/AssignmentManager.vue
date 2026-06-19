<template>
  <div class="flex h-screen bg-surface-offwhite dark:bg-surface-bgDark font-sans transition-colors duration-200">
    <Sidebar />
    <div class="flex-1 flex flex-col overflow-hidden">
      <Navbar />
      <main class="flex-1 overflow-y-auto p-6 lg:p-8">
        <div class="mb-8 flex items-center justify-between gap-4">
          <div class="flex items-center gap-4">
            <h1 class="text-[24px] font-semibold text-ink-dark dark:text-surface-light">Assignment Manager</h1>
          </div>
          <BaseButton variant="primary">New Assignment</BaseButton>
        </div>
        
        <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid overflow-hidden">
          <div class="px-6 py-4 border-b border-ink-lightest dark:border-ink-mid flex flex-wrap gap-4 items-center justify-between bg-surface-offwhite dark:bg-surface-dark">
            <div class="flex gap-4 w-full sm:w-auto">
              <BaseInput v-model="searchQuery" placeholder="Search assignments..." class="w-full sm:w-64" />
              <select class="px-3 py-2 text-[14px] rounded-md border border-ink-lightest dark:border-ink-mid bg-surface-light text-ink-dark dark:bg-surface-dark dark:text-ink-lightest outline-none">
                <option value="">All Courses</option>
                <option value="cs101">CS101 - Intro to CS</option>
              </select>
            </div>
          </div>
          
          <div class="overflow-x-auto">
            <table class="w-full text-left text-[14px]">
              <thead class="bg-surface-offwhite dark:bg-surface-dark text-ink-light dark:text-ink-mutedDark border-b border-ink-lightest dark:border-ink-mid">
                <tr>
                  <th class="px-6 py-4 font-medium uppercase tracking-wider text-[12px]">Title</th>
                  <th class="px-6 py-4 font-medium uppercase tracking-wider text-[12px]">Course</th>
                  <th class="px-6 py-4 font-medium uppercase tracking-wider text-[12px]">Due Date</th>
                  <th class="px-6 py-4 font-medium uppercase tracking-wider text-[12px]">Submissions</th>
                  <th class="px-6 py-4 font-medium uppercase tracking-wider text-[12px] text-right">Actions</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-ink-lightest dark:divide-ink-mid text-ink-dark dark:text-surface-light">
                <tr v-for="a in assignments" :key="a.id" class="hover:bg-surface-offwhite dark:hover:bg-ink-dark transition-colors even:bg-surface-offwhite/50 dark:even:bg-surface-dark">
                  <td class="px-6 py-4 whitespace-nowrap font-medium">{{ a.title }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-ink-mid dark:text-ink-mutedDark">{{ a.course }}</td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <span :class="{'text-alert-error font-medium': a.isOverdue}">{{ a.dueDate }}</span>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-center gap-2">
                      <div class="w-full bg-ink-lightest dark:bg-ink-mid rounded-full h-1.5 w-24">
                        <div class="bg-brand-accent h-1.5 rounded-full" :style="{ width: (a.submitted/a.total)*100 + '%' }"></div>
                      </div>
                      <span class="text-[12px]">{{ a.submitted }}/{{ a.total }}</span>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-right space-x-2">
                    <BaseButton variant="outline" size="sm" @click="$router.push('/gradebook')">Grade</BaseButton>
                    <BaseButton variant="secondary" size="sm">Edit</BaseButton>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import Navbar from '../../components/Navbar.vue';
import Sidebar from '../../components/Sidebar.vue';
import BaseInput from '../../components/ui/BaseInput.vue';
import BaseButton from '../../components/ui/BaseButton.vue';

const searchQuery = ref('');

const assignments = ref([
  { id: 1, title: 'Homework 1: Hello World', course: 'CS101', dueDate: 'Tomorrow, 11:59 PM', submitted: 45, total: 60, isOverdue: false },
  { id: 2, title: 'Midterm Essay', course: 'ENG202', dueDate: 'Yesterday', submitted: 28, total: 30, isOverdue: true },
]);
</script>
