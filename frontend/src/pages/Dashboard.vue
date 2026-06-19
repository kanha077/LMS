<template>
  <div>
    
<!-- Side Navigation Shell -->
<aside class="h-screen w-sidebar-width fixed left-0 top-0 bg-primary-container flex flex-col py-lg px-md z-50">
<div class="mb-3xl">
<h1 class="font-headline-md text-headline-md font-bold text-on-primary">Sahayta</h1>
<p class="text-on-primary-container text-label-caps opacity-70">Learning Management</p>
</div>
<nav class="flex-1 space-y-base">
<!-- Dashboard Active -->
<a class="flex items-center px-md py-sm rounded-lg border-l-[3px] border-secondary-container text-secondary-container bg-sidebar-active-bg transition-colors duration-200" href="#">
<span class="material-symbols-outlined mr-md">dashboard</span>
<span class="font-nav-link text-nav-link">Dashboard</span>
</a>
<a class="flex items-center px-md py-sm rounded-lg text-surface-variant opacity-80 hover:bg-sidebar-active-bg hover:text-on-primary transition-colors duration-200" href="#">
<span class="material-symbols-outlined mr-md">school</span>
<span class="font-nav-link text-nav-link">My Courses</span>
</a>
<a class="flex items-center px-md py-sm rounded-lg text-surface-variant opacity-80 hover:bg-sidebar-active-bg hover:text-on-primary transition-colors duration-200" href="#">
<span class="material-symbols-outlined mr-md">group</span>
<span class="font-nav-link text-nav-link">Students</span>
</a>
<a class="flex items-center px-md py-sm rounded-lg text-surface-variant opacity-80 hover:bg-sidebar-active-bg hover:text-on-primary transition-colors duration-200" href="#">
<span class="material-symbols-outlined mr-md">analytics</span>
<span class="font-nav-link text-nav-link">Analytics</span>
</a>
<a class="flex items-center px-md py-sm rounded-lg text-surface-variant opacity-80 hover:bg-sidebar-active-bg hover:text-on-primary transition-colors duration-200" href="#">
<span class="material-symbols-outlined mr-md">assignment</span>
<span class="font-nav-link text-nav-link">Assignments</span>
</a>
<a class="flex items-center px-md py-sm rounded-lg text-surface-variant opacity-80 hover:bg-sidebar-active-bg hover:text-on-primary transition-colors duration-200" href="#">
<span class="material-symbols-outlined mr-md">settings</span>
<span class="font-nav-link text-nav-link">Settings</span>
</a>
</nav>
<div class="mt-auto pt-lg border-t border-white/10 flex items-center gap-md">
<div class="w-10 h-10 rounded-full overflow-hidden border-2 border-secondary-container">
<img class="w-full h-full object-cover" data-alt="A professional headshot of a middle-aged female educator with a warm, confident expression. She is wearing a modern navy blazer against a minimalist soft gray background. The lighting is soft and flattering, emphasizing her role as an academic leader in a corporate yet accessible learning environment." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBYrzU8msQ67ENzcHXpPSIpgx12iryrpJoe2Gly6ofSU1qOLxsZplBfwe-pcSfkviPYSuP-0cyXBLi6Unwf6jmqXvMjUkXi-M8NT76ar_4xsQ3ptZPj9DnhBc-v4oMmgb-1PGK7to1wt0wRj9I-JanyUHaZnPgzDiasDfYRHuGXF38OO4bC2F3uBouesdbwG2-48tIqpIeUYRhgWgRj8KXSYLylJnHR9MREE6PQNb1NAjPEoEyexmklMrZ55uDXJz5KjIs9jYWdILdg"/>
</div>
<div class="flex flex-col">
<span class="text-on-primary text-nav-link font-bold">Priya Sharma</span>
<span class="text-on-primary-container text-[11px] uppercase tracking-wider">Sr. Educator</span>
</div>
</div>
</aside>
<!-- Top Bar -->
<header class="fixed top-0 right-0 left-sidebar-width h-16 bg-surface-container-lowest border-b border-border-soft px-lg flex items-center justify-between z-40">
<h2 class="font-semibold text-xl text-primary-container">Good morning, Priya 👋</h2>
<div class="flex items-center gap-xl">
<div class="relative group">
<span class="material-symbols-outlined absolute left-md top-1/2 -translate-y-1/2 text-on-surface-variant">search</span>
<input class="pl-3xl pr-md py-xs bg-surface-container-low border-none rounded-full w-64 text-body-sm focus:ring-2 focus:ring-secondary-container transition-all" placeholder="Search students, courses..." type="text"/>
</div>
<button class="relative p-xs rounded-full hover:bg-surface-container-high transition-colors">
<span class="material-symbols-outlined text-on-surface-variant">notifications</span>
<span class="absolute top-1 right-1 w-2 h-2 bg-secondary-container rounded-full border-2 border-surface-container-lowest"></span>
</button>
</div>
</header>
<!-- Main Content Canvas -->
<main class="ml-sidebar-width pt-16 min-h-screen">
<div class="p-lg max-w-max-content-width mx-auto">
<!-- Stats Row -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-lg mb-2xl">
<!-- Total Students -->
<div class="bg-surface-container-lowest p-lg rounded-xl border border-border-soft shadow-[0_1px_4px_rgba(30,27,75,0.08)]">
<div class="flex items-center justify-between mb-sm">
<span class="text-on-surface-variant text-label-caps">Total Students</span>
<span class="material-symbols-outlined text-primary-container opacity-20">group</span>
</div>
<div class="flex items-end justify-between">
<span class="font-display-hero text-headline-lg text-primary">5,240</span>
<div class="flex items-center text-on-tertiary-container bg-tertiary-fixed/30 px-xs py-1 rounded-full text-xs font-semibold">
<span class="material-symbols-outlined text-sm mr-1">trending_up</span>
                            12%
                        </div>
</div>
</div>
<!-- Active Courses -->
<div class="bg-surface-container-lowest p-lg rounded-xl border border-border-soft shadow-[0_1px_4px_rgba(30,27,75,0.08)]">
<div class="flex items-center justify-between mb-sm">
<span class="text-on-surface-variant text-label-caps">Active Courses</span>
<span class="material-symbols-outlined text-primary-container opacity-20">school</span>
</div>
<div class="flex items-end justify-between">
<span class="font-display-hero text-headline-lg text-primary">12</span>
<div class="flex items-center text-on-tertiary-container bg-tertiary-fixed/30 px-xs py-1 rounded-full text-xs font-semibold">
<span class="material-symbols-outlined text-sm mr-1">trending_up</span>
                            4%
                        </div>
</div>
</div>
<!-- Avg Completion -->
<div class="bg-surface-container-lowest p-lg rounded-xl border border-border-soft shadow-[0_1px_4px_rgba(30,27,75,0.08)]">
<div class="flex items-center justify-between mb-sm">
<span class="text-on-surface-variant text-label-caps">Avg. Completion Rate</span>
<span class="material-symbols-outlined text-primary-container opacity-20">verified</span>
</div>
<div class="flex items-end justify-between">
<span class="font-display-hero text-headline-lg text-primary">84%</span>
<div class="flex items-center text-on-tertiary-container bg-tertiary-fixed/30 px-xs py-1 rounded-full text-xs font-semibold">
<span class="material-symbols-outlined text-sm mr-1">trending_up</span>
                            8%
                        </div>
</div>
</div>
<!-- Pending Assignments -->
<div class="bg-surface-container-lowest p-lg rounded-xl border border-border-soft shadow-[0_1px_4px_rgba(30,27,75,0.08)]">
<div class="flex items-center justify-between mb-sm">
<span class="text-on-surface-variant text-label-caps">Pending Assignments</span>
<span class="material-symbols-outlined text-primary-container opacity-20">assignment_late</span>
</div>
<div class="flex items-end justify-between">
<span class="font-display-hero text-headline-lg text-primary">28</span>
<div class="flex items-center text-on-tertiary-container bg-tertiary-fixed/30 px-xs py-1 rounded-full text-xs font-semibold">
<span class="material-symbols-outlined text-sm mr-1">priority_high</span>
                            New
                        </div>
</div>
</div>
</div>
<!-- Dashboard Content Layout -->
<div class="grid grid-cols-1 lg:grid-cols-3 gap-2xl">
<!-- Courses Grid (Left/Center) -->
<div class="lg:col-span-2">
<div class="flex items-center justify-between mb-lg">
<h3 class="font-title-card text-title-card text-primary-container font-bold">Your Courses</h3>
<a class="text-secondary-container font-button-text flex items-center hover:underline" href="#">
                            View All <span class="material-symbols-outlined text-sm ml-1">arrow_forward</span>
</a>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-lg">
<!-- Course Card 1 -->
<div class="bg-surface-container-lowest rounded-xl border border-border-soft overflow-hidden hover:shadow-lg transition-shadow group">
<div class="h-40 overflow-hidden">
<img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" data-alt="A clean, conceptual 3D illustration representing Advanced Data Science. It features floating glowing nodes, binary sequences, and sleek abstract network paths. The color scheme is dominated by deep indigo and bright saffron yellow accents, set against a pristine white studio background with soft ambient shadows." src="https://lh3.googleusercontent.com/aida-public/AB6AXuC93otTp6A6aHK03MJK4RBxskhh0pBlQNbWoGx7XrNzDXlIIAg8ztccdu6U30QcqdGpuaUnXWpNgjDXdkMaJ_Z1MXaTvoR753z5UBKZ9oRStItyVuEF0FHyGxs5oi-3nlabuL3z0_mqwPCjpDebmZnfBQhksZtis4SiRjABBjE6Wexekjy9S1GoGTgS6Q0wh9wqFNGDOF8vMEnr8YS2PSCBx_2gYIOFWIebOWuJUWb0sUsagQeVgJJk9Aq_ck7ij6i136xF-9YCj5gK"/>
</div>
<div class="p-md">
<div class="flex justify-between items-start mb-xs">
<h4 class="font-bold text-primary-container">Advanced Data Science</h4>
<span class="text-xs bg-surface-container text-on-surface-variant px-2 py-0.5 rounded">Fall 2024</span>
</div>
<p class="text-body-sm text-on-surface-variant mb-md">1,240 Students enrolled</p>
<div class="space-y-xs">
<div class="flex justify-between text-xs font-semibold">
<span>Course Progress</span>
<span class="text-secondary-container">65%</span>
</div>
<div class="w-full h-2 bg-border-soft rounded-full overflow-hidden">
<div class="h-full bg-secondary-container rounded-full progress-bar-fill" style="width: 65%;"></div>
</div>
</div>
</div>
</div>
<!-- Course Card 2 -->
<div class="bg-surface-container-lowest rounded-xl border border-border-soft overflow-hidden hover:shadow-lg transition-shadow group">
<div class="h-40 overflow-hidden">
<img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" data-alt="A minimalist architectural photograph of a modern library facade with repetitive geometric patterns. The image emphasizes light and shadow, featuring a clean blue sky and sharp structural lines. The aesthetic is professional and corporate, using a palette of cool grays and a dash of warm wood tones for a high-end educational feel." src="https://lh3.googleusercontent.com/aida-public/AB6AXuB90P5_KJv37cWBH6khLpXBBXMbCsqK61R3MGHr-W3Svs-u67ko_Xi2qrpWl4iObSyJTGgiZiO1zsmYCq54ZG5wZ_ryT2MzwP1KxGFgJy6sddkCISVZ9jP2-Ki-L8_AG6p8kHqNL8Ii5gogMi37SjWXNZePV6I6sgnIAeSnXFBPPyn_Ri7SkFrXf5GO-fWxX3Mr6W-V2viIbcoFKLyvxcgXPYrSpLKy59hjc0f5HztVB30OpSLFZ6Q8dR-GeJDbGtac8XMnsZqkmtvp"/>
</div>
<div class="p-md">
<div class="flex justify-between items-start mb-xs">
<h4 class="font-bold text-primary-container">Intro to UX Design</h4>
<span class="text-xs bg-surface-container text-on-surface-variant px-2 py-0.5 rounded">Summer 2024</span>
</div>
<p class="text-body-sm text-on-surface-variant mb-md">842 Students enrolled</p>
<div class="space-y-xs">
<div class="flex justify-between text-xs font-semibold">
<span>Course Progress</span>
<span class="text-secondary-container">42%</span>
</div>
<div class="w-full h-2 bg-border-soft rounded-full overflow-hidden">
<div class="h-full bg-secondary-container rounded-full progress-bar-fill" style="width: 42%;"></div>
</div>
</div>
</div>
</div>
</div>
</div>
<!-- Right Side Notifications/Activity -->
<div class="space-y-lg">
<h3 class="font-title-card text-title-card text-primary-container font-bold">Upcoming Events</h3>
<div class="space-y-md">
<div class="flex gap-md bg-surface-container-lowest p-md rounded-xl border border-border-soft">
<div class="flex flex-col items-center justify-center bg-primary-container text-on-primary w-14 h-14 rounded-lg shrink-0">
<span class="text-xs font-bold uppercase">Oct</span>
<span class="text-lg font-bold">12</span>
</div>
<div>
<h5 class="font-bold text-sm text-primary-container">Faculty Review Meeting</h5>
<p class="text-xs text-on-surface-variant">10:00 AM - Boardroom A</p>
</div>
</div>
<div class="flex gap-md bg-surface-container-lowest p-md rounded-xl border border-border-soft">
<div class="flex flex-col items-center justify-center bg-secondary-container text-primary-container w-14 h-14 rounded-lg shrink-0">
<span class="text-xs font-bold uppercase">Oct</span>
<span class="text-lg font-bold">15</span>
</div>
<div>
<h5 class="font-bold text-sm text-primary-container">Assignment Deadline</h5>
<p class="text-xs text-on-surface-variant">UX Module 3 Submissions</p>
</div>
</div>
</div>
<div class="bg-primary-container rounded-xl p-lg text-on-primary relative overflow-hidden">
<div class="relative z-10">
<h4 class="font-bold mb-xs">Pro Tip: New Feature</h4>
<p class="text-xs text-on-primary-container opacity-80 mb-md">Try the new AI-powered student sentiment analysis tool to identify students at risk early.</p>
<button class="bg-secondary-container text-primary-container px-md py-xs rounded-full text-xs font-bold hover:bg-accent-hover transition-colors">Learn More</button>
</div>
<div class="absolute -right-4 -bottom-4 opacity-10">
<span class="material-symbols-outlined text-[100px]">lightbulb</span>
</div>
</div>
</div>
</div>
<!-- Student Activity Table Section -->
<section class="mt-2xl">
<div class="flex items-center justify-between mb-lg">
<h3 class="font-title-card text-title-card text-primary-container font-bold">Recent Student Activity</h3>
<div class="flex gap-sm">
<button class="px-md py-xs rounded-full border border-border-soft bg-surface-container-lowest text-xs font-semibold hover:bg-surface-container transition-colors">Export CSV</button>
<button class="px-md py-xs rounded-full border border-border-soft bg-surface-container-lowest text-xs font-semibold hover:bg-surface-container transition-colors">Filters</button>
</div>
</div>
<div class="bg-surface-container-lowest rounded-xl border border-border-soft shadow-[0_1px_4px_rgba(30,27,75,0.08)] overflow-hidden">
<table class="w-full text-left border-collapse">
<thead class="bg-surface-container-low">
<tr>
<th class="px-lg py-md text-label-caps text-on-surface-variant">Student Name</th>
<th class="px-lg py-md text-label-caps text-on-surface-variant">Course</th>
<th class="px-lg py-md text-label-caps text-on-surface-variant">Last Active</th>
<th class="px-lg py-md text-label-caps text-on-surface-variant">Progress</th>
<th class="px-lg py-md text-label-caps text-on-surface-variant">Status</th>
</tr>
</thead>
<tbody class="divide-y divide-border-soft">
<!-- Row 1 -->
<tr class="hover:bg-surface-container-low/50 transition-colors cursor-pointer group">
<td class="px-lg py-md">
<div class="flex items-center gap-md">
<div class="w-8 h-8 rounded-full bg-primary-fixed flex items-center justify-center text-primary text-xs font-bold">AK</div>
<div>
<p class="font-bold text-sm text-primary-container">Arjun Kumar</p>
<p class="text-[11px] text-on-surface-variant">arjun.k@university.edu</p>
</div>
</div>
</td>
<td class="px-lg py-md text-sm">Advanced Data Science</td>
<td class="px-lg py-md text-sm text-on-surface-variant">2 mins ago</td>
<td class="px-lg py-md">
<div class="flex items-center gap-sm">
<div class="flex-1 h-1.5 bg-border-soft rounded-full overflow-hidden max-w-[100px]">
<div class="h-full bg-on-tertiary-container" style="width: 92%;"></div>
</div>
<span class="text-xs font-bold">92%</span>
</div>
</td>
<td class="px-lg py-md">
<span class="px-3 py-1 rounded-full text-[11px] font-bold bg-tertiary-fixed/30 text-on-tertiary-container">Completed</span>
</td>
</tr>
<!-- Row 2 -->
<tr class="hover:bg-surface-container-low/50 transition-colors cursor-pointer group">
<td class="px-lg py-md">
<div class="flex items-center gap-md">
<div class="w-8 h-8 rounded-full bg-secondary-fixed flex items-center justify-center text-on-secondary-fixed text-xs font-bold">SR</div>
<div>
<p class="font-bold text-sm text-primary-container">Sarah Reed</p>
<p class="text-[11px] text-on-surface-variant">s.reed@university.edu</p>
</div>
</div>
</td>
<td class="px-lg py-md text-sm">Intro to UX Design</td>
<td class="px-lg py-md text-sm text-on-surface-variant">45 mins ago</td>
<td class="px-lg py-md">
<div class="flex items-center gap-sm">
<div class="flex-1 h-1.5 bg-border-soft rounded-full overflow-hidden max-w-[100px]">
<div class="h-full bg-secondary-container" style="width: 45%;"></div>
</div>
<span class="text-xs font-bold">45%</span>
</div>
</td>
<td class="px-lg py-md">
<span class="px-3 py-1 rounded-full text-[11px] font-bold bg-secondary-fixed/50 text-on-secondary-container">On Track</span>
</td>
</tr>
<!-- Row 3 -->
<tr class="hover:bg-surface-container-low/50 transition-colors cursor-pointer group">
<td class="px-lg py-md">
<div class="flex items-center gap-md">
<div class="w-8 h-8 rounded-full bg-error-container flex items-center justify-center text-error text-xs font-bold">MW</div>
<div>
<p class="font-bold text-sm text-primary-container">Marcus Wright</p>
<p class="text-[11px] text-on-surface-variant">m.wright@university.edu</p>
</div>
</div>
</td>
<td class="px-lg py-md text-sm">Advanced Data Science</td>
<td class="px-lg py-md text-sm text-on-surface-variant">2 days ago</td>
<td class="px-lg py-md">
<div class="flex items-center gap-sm">
<div class="flex-1 h-1.5 bg-border-soft rounded-full overflow-hidden max-w-[100px]">
<div class="h-full bg-error" style="width: 12%;"></div>
</div>
<span class="text-xs font-bold">12%</span>
</div>
</td>
<td class="px-lg py-md">
<span class="px-3 py-1 rounded-full text-[11px] font-bold bg-error-container text-on-error-container">At Risk</span>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</main>
<!-- Contextual FAB (Only on Dashboard) -->
<button class="fixed bottom-lg right-lg w-14 h-14 bg-secondary-container text-primary-container rounded-full shadow-lg hover:shadow-xl hover:scale-110 transition-all flex items-center justify-center group">
<span class="material-symbols-outlined text-2xl group-hover:rotate-90 transition-transform">add</span>
</button>


  </div>
</template>

<script setup>
</script>

<style scoped>
/* Copy any specific styles if needed, or rely on global Tailwind classes */
</style>
