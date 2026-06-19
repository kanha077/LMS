<template>
  <div class="space-y-6">
    <!-- KPI Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid">
        <h3 class="text-[13px] font-medium text-ink-light dark:text-ink-mutedDark uppercase tracking-widest">Active Classes</h3>
        <div class="mt-2 flex items-baseline gap-2">
          <p class="text-3xl font-bold text-ink-dark dark:text-surface-light">4</p>
        </div>
      </div>
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid">
        <h3 class="text-[13px] font-medium text-ink-light dark:text-ink-mutedDark uppercase tracking-widest">To Grade</h3>
        <div class="mt-2 flex items-baseline gap-2">
          <p class="text-3xl font-bold text-alert-error dark:text-red-400">12</p>
          <span class="text-[12px] text-ink-mid dark:text-ink-mutedDark font-medium">pending</span>
        </div>
      </div>
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid">
        <h3 class="text-[13px] font-medium text-ink-light dark:text-ink-mutedDark uppercase tracking-widest">Total Students</h3>
        <div class="mt-2 flex items-baseline gap-2">
          <p class="text-3xl font-bold text-brand-accent dark:text-blue-400">128</p>
        </div>
      </div>
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid">
        <h3 class="text-[13px] font-medium text-ink-light dark:text-ink-mutedDark uppercase tracking-widest">Avg Attendance</h3>
        <div class="mt-2 flex items-baseline gap-2">
          <p class="text-3xl font-bold text-alert-success dark:text-green-400">92%</p>
        </div>
      </div>
    </div>

    <!-- Quick Actions -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2 bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid flex flex-col justify-center">
        <h3 class="text-[15px] font-medium text-ink-dark dark:text-surface-light mb-4">Quick Actions</h3>
        <div class="flex flex-wrap gap-4">
          <BaseButton variant="primary" @click="$router.push('/courses/create')">
            <span class="flex items-center gap-2">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
              Build New Course
            </span>
          </BaseButton>
          <BaseButton variant="secondary" @click="$router.push('/quizzes/create')">Create Quiz</BaseButton>
          <BaseButton variant="secondary" @click="$router.push('/assignments/manage')">Manage Assignments</BaseButton>
        </div>
      </div>
      
      <!-- Recent Submissions Preview -->
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid overflow-hidden flex flex-col">
        <div class="px-6 py-4 border-b border-ink-lightest dark:border-ink-mid bg-surface-offwhite dark:bg-surface-dark flex justify-between items-center">
          <h2 class="text-[15px] font-medium text-ink-dark dark:text-surface-light">Needs Grading</h2>
          <button class="text-brand-accent hover:text-brand-accentHover text-[13px] font-medium" @click="$router.push('/gradebook')">Grade All</button>
        </div>
        <div class="p-0 overflow-y-auto max-h-64">
           <div class="divide-y divide-ink-lightest dark:divide-ink-mid">
             <div class="p-4 hover:bg-surface-offwhite dark:hover:bg-ink-dark transition-colors flex justify-between items-center">
               <div>
                 <p class="text-[14px] font-medium text-ink-dark dark:text-surface-light">Homework 1</p>
                 <p class="text-[12px] text-ink-light dark:text-ink-mutedDark">CS101 • Alice Student</p>
               </div>
               <span class="text-[11px] font-bold text-alert-error uppercase tracking-wider">Pending</span>
             </div>
             <div class="p-4 hover:bg-surface-offwhite dark:hover:bg-ink-dark transition-colors flex justify-between items-center">
               <div>
                 <p class="text-[14px] font-medium text-ink-dark dark:text-surface-light">Midterm Essay</p>
                 <p class="text-[12px] text-ink-light dark:text-ink-mutedDark">ENG202 • Bob Smith</p>
               </div>
               <span class="text-[11px] font-bold text-alert-error uppercase tracking-wider">Pending</span>
             </div>
           </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import BaseButton from '../../components/ui/BaseButton.vue';
</script>
