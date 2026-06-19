<template>
  <div class="flex h-screen bg-surface-offwhite dark:bg-surface-bgDark font-sans transition-colors duration-200">
    <Sidebar />
    <div class="flex-1 flex flex-col overflow-hidden">
      <Navbar />
      <main class="flex-1 overflow-y-auto p-6 lg:p-8">
        <div class="mb-8 flex items-center justify-between gap-4">
          <div class="flex items-center gap-4">
            <h1 class="text-[24px] font-semibold text-ink-dark dark:text-surface-light">Gradebook</h1>
          </div>
          <BaseButton variant="outline">Export CSV</BaseButton>
        </div>
        
        <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid overflow-hidden flex flex-col h-[calc(100vh-180px)]">
          <div class="px-6 py-4 border-b border-ink-lightest dark:border-ink-mid flex gap-4 bg-surface-offwhite dark:bg-surface-dark">
            <select class="px-3 py-2 text-[14px] rounded-md border border-ink-lightest dark:border-ink-mid bg-surface-light text-ink-dark dark:bg-surface-dark dark:text-ink-lightest outline-none w-48">
              <option value="cs101">CS101 - Intro to CS</option>
            </select>
          </div>
          
          <div class="overflow-auto flex-1 p-0">
            <table class="w-full text-left text-[14px]">
              <thead class="bg-surface-offwhite dark:bg-surface-dark text-ink-light dark:text-ink-mutedDark border-b border-ink-lightest dark:border-ink-mid sticky top-0 z-10">
                <tr>
                  <th class="px-6 py-3 font-medium uppercase tracking-wider text-[12px] sticky left-0 bg-surface-offwhite dark:bg-surface-dark border-r border-ink-lightest dark:border-ink-mid">Student</th>
                  <th v-for="a in assignments" :key="a.id" class="px-6 py-3 font-medium uppercase tracking-wider text-[12px] min-w-[120px]">
                    {{ a.title }}
                    <span class="block text-[10px] text-brand-accent mt-0.5">{{ a.points }} pts</span>
                  </th>
                  <th class="px-6 py-3 font-medium uppercase tracking-wider text-[12px] bg-ink-lightest/30 dark:bg-ink-mid/30 text-right">Total (%)</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-ink-lightest dark:divide-ink-mid text-ink-dark dark:text-surface-light">
                <tr v-for="s in students" :key="s.id" class="hover:bg-surface-offwhite dark:hover:bg-ink-dark transition-colors">
                  <td class="px-6 py-3 font-medium sticky left-0 bg-surface-light dark:bg-surface-dark border-r border-ink-lightest dark:border-ink-mid shadow-[2px_0_5px_rgba(0,0,0,0.05)] dark:shadow-[2px_0_5px_rgba(0,0,0,0.2)]">{{ s.name }}</td>
                  <td v-for="a in assignments" :key="a.id" class="px-6 py-3">
                    <input type="text" :value="s.grades[a.id]" class="w-16 px-2 py-1 text-center text-[13px] rounded border border-transparent hover:border-ink-lightest dark:hover:border-ink-mid focus:border-brand-accent focus:ring-1 focus:ring-brand-accent outline-none bg-transparent transition-all" placeholder="-" />
                  </td>
                  <td class="px-6 py-3 text-right font-bold bg-ink-lightest/10 dark:bg-ink-mid/10">
                    <span :class="getTotal(s) >= 90 ? 'text-alert-success' : (getTotal(s) < 70 ? 'text-alert-error' : '')">{{ getTotal(s) }}%</span>
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
import BaseButton from '../../components/ui/BaseButton.vue';

const assignments = ref([
  { id: 'hw1', title: 'HW 1', points: 100 },
  { id: 'hw2', title: 'HW 2', points: 100 },
  { id: 'quiz1', title: 'Quiz 1', points: 50 },
  { id: 'midterm', title: 'Midterm', points: 200 },
]);

const students = ref([
  { id: 1, name: 'Alice Student', grades: { hw1: 95, hw2: 90, quiz1: 45, midterm: 180 } },
  { id: 2, name: 'Bob Smith', grades: { hw1: 80, hw2: 85, quiz1: 40, midterm: 150 } },
  { id: 3, name: 'Charlie Davis', grades: { hw1: 60, hw2: 65, quiz1: 25, midterm: 120 } },
  { id: 4, name: 'Diana Prince', grades: { hw1: 100, hw2: 100, quiz1: 50, midterm: 195 } },
]);

const getTotal = (student) => {
  let earned = 0;
  let possible = 0;
  assignments.value.forEach(a => {
    if (student.grades[a.id] !== undefined) {
      earned += Number(student.grades[a.id]);
      possible += a.points;
    }
  });
  if (possible === 0) return 0;
  return Math.round((earned / possible) * 100);
};
</script>
