<template>
  <div class="space-y-6">
    <!-- Welcome & Gamification Header -->
    <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid flex flex-col md:flex-row justify-between items-center gap-6">
      <div>
        <h2 class="text-[22px] font-semibold text-ink-dark dark:text-surface-light">Welcome back, Alice!</h2>
        <p class="text-[14px] text-ink-mid dark:text-ink-mutedDark mt-1">You are doing great. Keep up the momentum!</p>
      </div>
      <div class="flex gap-6 items-center">
        <div class="text-center">
          <p class="text-[12px] font-medium text-ink-light uppercase tracking-widest">Total Points</p>
          <p class="text-[24px] font-bold text-brand-accent">1,250</p>
        </div>
        <div class="h-10 w-px bg-ink-lightest dark:bg-ink-mid"></div>
        <div class="text-center">
          <p class="text-[12px] font-medium text-ink-light uppercase tracking-widest">Global Rank</p>
          <p class="text-[24px] font-bold text-ink-dark dark:text-surface-light">#42</p>
        </div>
        <div class="flex -space-x-2">
          <div class="w-10 h-10 rounded-full bg-brand-accent/20 border-2 border-surface-light dark:border-surface-dark flex items-center justify-center text-[18px]" title="Quick Learner">🚀</div>
          <div class="w-10 h-10 rounded-full bg-alert-success/20 border-2 border-surface-light dark:border-surface-dark flex items-center justify-center text-[18px]" title="Perfect Score">💯</div>
          <div class="w-10 h-10 rounded-full bg-alert-warning/20 border-2 border-surface-light dark:border-surface-dark flex items-center justify-center text-[18px]" title="7 Day Streak">🔥</div>
        </div>
      </div>
    </div>

    <!-- KPI Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid">
        <h3 class="text-[13px] font-medium text-ink-light dark:text-ink-mutedDark uppercase tracking-widest">Enrolled Courses</h3>
        <p class="mt-2 text-3xl font-bold text-ink-dark dark:text-surface-light">4</p>
      </div>
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid">
        <h3 class="text-[13px] font-medium text-ink-light dark:text-ink-mutedDark uppercase tracking-widest">Pending Assignments</h3>
        <p class="mt-2 text-3xl font-bold text-alert-warning dark:text-yellow-400">2</p>
      </div>
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid p-6 border border-ink-lightest dark:border-ink-mid">
        <h3 class="text-[13px] font-medium text-ink-light dark:text-ink-mutedDark uppercase tracking-widest">Overall GPA</h3>
        <p class="mt-2 text-3xl font-bold text-alert-success dark:text-green-400">3.8</p>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Course Progress Tracker -->
      <div class="lg:col-span-2 bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid overflow-hidden">
        <div class="px-6 py-4 border-b border-ink-lightest dark:border-ink-mid bg-surface-offwhite dark:bg-surface-dark flex justify-between items-center">
          <h2 class="text-[15px] font-medium text-ink-dark dark:text-surface-light">My Courses</h2>
          <button class="text-brand-accent hover:text-brand-accentHover text-[13px] font-medium" @click="$router.push('/courses')">View All</button>
        </div>
        <div class="p-6 space-y-6">
          <div>
            <div class="flex justify-between items-end mb-2">
              <div>
                <p class="text-[14px] font-medium text-ink-dark dark:text-surface-light">CS101: Intro to Computer Science</p>
                <p class="text-[12px] text-ink-light dark:text-ink-mutedDark">Module 3: Control Structures</p>
              </div>
              <span class="text-[13px] font-bold text-brand-accent">45%</span>
            </div>
            <div class="w-full bg-ink-lightest dark:bg-ink-mid rounded-full h-2">
              <div class="bg-brand-accent h-2 rounded-full" style="width: 45%"></div>
            </div>
          </div>
          <div>
            <div class="flex justify-between items-end mb-2">
              <div>
                <p class="text-[14px] font-medium text-ink-dark dark:text-surface-light">ENG202: Advanced Literature</p>
                <p class="text-[12px] text-ink-light dark:text-ink-mutedDark">Module 8: Final Essay Draft</p>
              </div>
              <span class="text-[13px] font-bold text-alert-success">85%</span>
            </div>
            <div class="w-full bg-ink-lightest dark:bg-ink-mid rounded-full h-2">
              <div class="bg-alert-success h-2 rounded-full" style="width: 85%"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Upcoming Deadlines -->
      <div class="bg-surface-light dark:bg-surface-dark rounded-xl shadow-solid border border-ink-lightest dark:border-ink-mid overflow-hidden flex flex-col">
        <div class="px-6 py-4 border-b border-ink-lightest dark:border-ink-mid bg-surface-offwhite dark:bg-surface-dark">
          <h2 class="text-[15px] font-medium text-ink-dark dark:text-surface-light">Upcoming Deadlines</h2>
        </div>
        <div class="p-0 overflow-y-auto max-h-64">
           <div class="divide-y divide-ink-lightest dark:divide-ink-mid">
             <div class="p-4 hover:bg-surface-offwhite dark:hover:bg-ink-dark transition-colors">
               <p class="text-[14px] font-medium text-ink-dark dark:text-surface-light">Homework 1: Hello World</p>
               <div class="flex justify-between mt-1 items-center">
                 <p class="text-[12px] text-ink-light dark:text-ink-mutedDark">CS101</p>
                 <span class="text-[11px] font-bold text-alert-error uppercase tracking-wider">Tomorrow</span>
               </div>
             </div>
             <div class="p-4 hover:bg-surface-offwhite dark:hover:bg-ink-dark transition-colors">
               <p class="text-[14px] font-medium text-ink-dark dark:text-surface-light">Midterm Exam</p>
               <div class="flex justify-between mt-1 items-center">
                 <p class="text-[12px] text-ink-light dark:text-ink-mutedDark">ENG202</p>
                 <span class="text-[11px] font-bold text-alert-warning uppercase tracking-wider">In 3 Days</span>
               </div>
             </div>
           </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
