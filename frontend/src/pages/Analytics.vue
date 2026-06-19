<template>
  <div>
    
<!-- Fixed Side Navigation -->
<aside class="fixed left-0 top-0 h-screen w-sidebar-width bg-primary dark:bg-primary-container shadow-sm flex flex-col py-lg z-50">
<div class="px-lg mb-2xl">
<h1 class="font-headline-md text-headline-md font-bold text-secondary-container dark:text-secondary tracking-tight">EduPulse Admin</h1>
<p class="text-on-primary/60 dark:text-on-primary-container/60 text-xs font-label-caps uppercase mt-1">Academic Management</p>
</div>
<nav class="flex-1 px-sm space-y-xs overflow-y-auto">
<a class="group relative flex items-center gap-md px-md py-sm transition-colors duration-200 ease-in-out text-on-primary/70 dark:text-on-primary-container/70 hover:bg-sidebar-active-bg hover:text-on-primary rounded-lg font-nav-link text-nav-link" href="#">
<span class="material-symbols-outlined">dashboard</span>
<span>Overview</span>
</a>
<!-- Active State: Analytics -->
<a class="group relative flex items-center gap-md px-md py-sm transition-colors duration-200 ease-in-out border-l-4 border-secondary-container bg-sidebar-active-bg text-secondary-container font-semibold rounded-r-lg font-nav-link text-nav-link" href="#">
<span class="material-symbols-outlined">analytics</span>
<span>Analytics</span>
</a>
<a class="group relative flex items-center gap-md px-md py-sm transition-colors duration-200 ease-in-out text-on-primary/70 dark:text-on-primary-container/70 hover:bg-sidebar-active-bg hover:text-on-primary rounded-lg font-nav-link text-nav-link" href="#">
<span class="material-symbols-outlined">school</span>
<span>Courses</span>
</a>
<a class="group relative flex items-center gap-md px-md py-sm transition-colors duration-200 ease-in-out text-on-primary/70 dark:text-on-primary-container/70 hover:bg-sidebar-active-bg hover:text-on-primary rounded-lg font-nav-link text-nav-link" href="#">
<span class="material-symbols-outlined">group</span>
<span>Students</span>
</a>
<a class="group relative flex items-center gap-md px-md py-sm transition-colors duration-200 ease-in-out text-on-primary/70 dark:text-on-primary-container/70 hover:bg-sidebar-active-bg hover:text-on-primary rounded-lg font-nav-link text-nav-link" href="#">
<span class="material-symbols-outlined">settings</span>
<span>Settings</span>
</a>
</nav>
<div class="px-lg mt-auto">
<button class="w-full bg-secondary-container text-primary font-button-text text-button-text py-md rounded-full shadow-lg hover:bg-accent-hover transition-colors flex items-center justify-center gap-sm">
<span class="material-symbols-outlined text-[18px]">add_chart</span>
                Generate Report
            </button>
<div class="mt-lg flex items-center gap-md pt-lg border-t border-on-primary/10">
<div class="w-10 h-10 rounded-full bg-surface-container-highest overflow-hidden">
<img class="w-full h-full object-cover" data-alt="A professional headshot of a middle-aged academic administrator with glasses, looking friendly and authoritative. The lighting is soft and studio-quality, reflecting a clean corporate aesthetic with a blurred library background in deep indigo tones." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCyxRz5Qq1MbCtQWVsruYTpbTonZ4mcWRx-NfGeWtqAuqxF3BgIEXwNdrROLvIATPV6uF0ziWHSki0CemjiyhrdXA_u5xwD5eNH3t9IA8-XENq_NBBfiTw8BmXY5UXYr5_2WwfavUZfITWKZQ8VlmUwz6Z7tMe6vxqRJvjTLC8mCJlfBlFu3IxIuhLLH6JoFoSMIFCtJ9iVDZipBuovZ7k6IDTpZBMTo2ERSteoM_nMTOZeSOtBFJJNhDWJ3nwq2ThAxa3qW4jhNet4"/>
</div>
<div class="overflow-hidden">
<p class="text-on-primary font-semibold truncate text-sm">Dr. Sarah Jenkins</p>
<p class="text-on-primary/60 text-xs truncate">Head of Analytics</p>
</div>
</div>
</div>
</aside>
<!-- Main Content Area -->
<main class="ml-sidebar-width min-h-screen">
<!-- Top Nav Bar -->
<header class="flex justify-between items-center w-full px-xl py-md bg-surface border-b border-border-soft sticky top-0 z-40">
<div class="flex items-center gap-xl flex-1">
<div class="relative w-64">
<span class="material-symbols-outlined absolute left-md top-1/2 -translate-y-1/2 text-on-surface-variant/60">search</span>
<input class="w-full pl-3xl pr-md py-xs bg-surface-container-low border border-border-soft rounded-full text-sm focus:ring-2 focus:ring-secondary-container focus:border-secondary-container transition-all outline-none" placeholder="Search analytics..." type="text"/>
</div>
<nav class="hidden md:flex items-center gap-lg">
<a class="font-nav-link text-nav-link text-primary font-bold border-b-2 border-secondary py-1" href="#">Reports</a>
<a class="font-nav-link text-nav-link text-on-surface-variant hover:text-secondary transition-colors" href="#">Schedule</a>
<a class="font-nav-link text-nav-link text-on-surface-variant hover:text-secondary transition-colors" href="#">Alerts</a>
</nav>
</div>
<div class="flex items-center gap-lg">
<button class="flex items-center gap-xs px-md py-xs border border-border-soft rounded-lg text-sm font-medium hover:bg-surface-container-low transition-colors">
<span class="material-symbols-outlined text-[18px]">calendar_today</span>
                    Filter Date
                </button>
<button class="p-xs text-on-surface-variant hover:bg-surface-container-low rounded-full transition-colors relative">
<span class="material-symbols-outlined">notifications</span>
<span class="absolute top-1 right-1 w-2 h-2 bg-error rounded-full"></span>
</button>
<button class="p-xs text-on-surface-variant hover:bg-surface-container-low rounded-full transition-colors">
<span class="material-symbols-outlined">help_outline</span>
</button>
</div>
</header>
<!-- Content Canvas -->
<div class="p-xl max-w-[1400px] mx-auto space-y-xl">
<!-- Page Header -->
<div class="flex flex-col md:flex-row md:items-end justify-between gap-lg">
<div>
<h2 class="font-headline-md text-headline-md font-semibold text-text-primary">Analytics Overview</h2>
<p class="text-on-surface-variant mt-xs">Real-time performance metrics across all academic departments.</p>
</div>
<div class="flex bg-surface-container-low p-base rounded-xl border border-border-soft">
<button class="px-md py-xs text-sm font-medium text-on-surface-variant hover:text-primary transition-colors">Last 7d</button>
<button class="px-md py-xs text-sm font-semibold bg-white shadow-sm rounded-lg text-primary border border-border-soft">Last 30d</button>
<button class="px-md py-xs text-sm font-medium text-on-surface-variant hover:text-primary transition-colors">Custom</button>
</div>
</div>
<!-- KPI Cards Grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-lg">
<!-- Card 1 -->
<div class="bg-white p-lg rounded-xl shadow-[0_1px_4px_rgba(30,27,75,0.08)] border border-border-soft hover:border-secondary-container/30 transition-all duration-300 group">
<div class="flex justify-between items-start mb-md">
<div class="p-sm bg-primary/5 rounded-lg group-hover:bg-primary/10 transition-colors">
<span class="material-symbols-outlined text-primary">person_add</span>
</div>
<span class="flex items-center gap-xs text-on-tertiary-container font-semibold text-xs py-1 px-2 bg-on-tertiary-container/10 rounded-full">
<span class="material-symbols-outlined text-[14px]">trending_up</span> 8%
                        </span>
</div>
<p class="text-on-surface-variant text-sm font-medium">Total Enrollments</p>
<h3 class="font-display-hero text-[32px] text-primary mt-xs">12,840</h3>
</div>
<!-- Card 2 -->
<div class="bg-white p-lg rounded-xl shadow-[0_1px_4px_rgba(30,27,75,0.08)] border border-border-soft hover:border-secondary-container/30 transition-all duration-300 group">
<div class="flex justify-between items-start mb-md">
<div class="p-sm bg-primary/5 rounded-lg group-hover:bg-primary/10 transition-colors">
<span class="material-symbols-outlined text-primary">task_alt</span>
</div>
<span class="flex items-center gap-xs text-on-tertiary-container font-semibold text-xs py-1 px-2 bg-on-tertiary-container/10 rounded-full">
<span class="material-symbols-outlined text-[14px]">trending_up</span> 5%
                        </span>
</div>
<p class="text-on-surface-variant text-sm font-medium">Course Completion</p>
<h3 class="font-display-hero text-[32px] text-primary mt-xs">76.4%</h3>
</div>
<!-- Card 3 -->
<div class="bg-white p-lg rounded-xl shadow-[0_1px_4px_rgba(30,27,75,0.08)] border border-border-soft hover:border-secondary-container/30 transition-all duration-300 group">
<div class="flex justify-between items-start mb-md">
<div class="p-sm bg-primary/5 rounded-lg group-hover:bg-primary/10 transition-colors">
<span class="material-symbols-outlined text-primary">quiz</span>
</div>
<span class="flex items-center gap-xs text-on-tertiary-container font-semibold text-xs py-1 px-2 bg-on-tertiary-container/10 rounded-full">
<span class="material-symbols-outlined text-[14px]">trending_up</span> 2%
                        </span>
</div>
<p class="text-on-surface-variant text-sm font-medium">Avg. Quiz Score</p>
<h3 class="font-display-hero text-[32px] text-primary mt-xs">88%</h3>
</div>
<!-- Card 4 -->
<div class="bg-white p-lg rounded-xl shadow-[0_1px_4px_rgba(30,27,75,0.08)] border border-border-soft hover:border-secondary-container/30 transition-all duration-300 group">
<div class="flex justify-between items-start mb-md">
<div class="p-sm bg-primary/5 rounded-lg group-hover:bg-primary/10 transition-colors">
<span class="material-symbols-outlined text-primary">school</span>
</div>
<span class="flex items-center gap-xs text-on-tertiary-container font-semibold text-xs py-1 px-2 bg-on-tertiary-container/10 rounded-full">
<span class="material-symbols-outlined text-[14px]">trending_up</span> 12%
                        </span>
</div>
<p class="text-on-surface-variant text-sm font-medium">New Students (MTD)</p>
<h3 class="font-display-hero text-[32px] text-primary mt-xs">1,120</h3>
</div>
</div>
<!-- Charts Row -->
<div class="grid grid-cols-1 lg:grid-cols-10 gap-xl">
<!-- Line Chart: Student Activity -->
<div class="lg:col-span-6 bg-white p-xl rounded-xl shadow-[0_1px_4px_rgba(30,27,75,0.08)] border border-border-soft flex flex-col h-[400px]">
<div class="flex justify-between items-center mb-xl">
<div>
<h4 class="font-title-card text-title-card text-primary">Student Activity Over Time</h4>
<p class="text-xs text-on-surface-variant mt-base">Daily active users per sessions</p>
</div>
<select class="text-xs font-medium border-border-soft rounded-lg bg-surface-container-low px-sm py-xs outline-none focus:ring-1 focus:ring-secondary-container">
<option>All Platforms</option>
<option>Mobile App</option>
<option>Web Portal</option>
</select>
</div>
<div class="flex-1 relative mt-md">
<!-- Simulated Chart Visualization -->
<div class="absolute inset-0 flex items-end justify-between gap-base px-base pb-xl">
<div class="w-full h-[40%] bg-primary/5 rounded-t-sm relative group cursor-pointer hover:bg-primary/10 transition-all">
<div class="absolute -top-xs left-1/2 -translate-x-1/2 w-3 h-3 bg-secondary-container rounded-full border-2 border-white scale-0 group-hover:scale-100 transition-transform"></div>
</div>
<div class="w-full h-[55%] bg-primary/5 rounded-t-sm relative group cursor-pointer hover:bg-primary/10 transition-all">
<div class="absolute -top-xs left-1/2 -translate-x-1/2 w-3 h-3 bg-secondary-container rounded-full border-2 border-white scale-0 group-hover:scale-100 transition-transform"></div>
</div>
<div class="w-full h-[75%] bg-primary/5 rounded-t-sm relative group cursor-pointer hover:bg-primary/10 transition-all">
<div class="absolute -top-xs left-1/2 -translate-x-1/2 w-3 h-3 bg-secondary-container rounded-full border-2 border-white scale-0 group-hover:scale-100 transition-transform"></div>
</div>
<div class="w-full h-[45%] bg-primary/5 rounded-t-sm relative group cursor-pointer hover:bg-primary/10 transition-all">
<div class="absolute -top-xs left-1/2 -translate-x-1/2 w-3 h-3 bg-secondary-container rounded-full border-2 border-white scale-0 group-hover:scale-100 transition-transform"></div>
</div>
<div class="w-full h-[90%] bg-primary/10 rounded-t-sm relative group cursor-pointer hover:bg-primary/20 border-t-2 border-primary transition-all">
<div class="absolute -top-xs left-1/2 -translate-x-1/2 w-4 h-4 bg-secondary-container rounded-full border-4 border-white shadow-md z-10"></div>
<div class="absolute -top-lg left-1/2 -translate-x-1/2 bg-primary text-white text-[10px] px-2 py-1 rounded-md opacity-0 group-hover:opacity-100 transition-opacity">8.4k</div>
</div>
<div class="w-full h-[65%] bg-primary/5 rounded-t-sm relative group cursor-pointer hover:bg-primary/10 transition-all">
<div class="absolute -top-xs left-1/2 -translate-x-1/2 w-3 h-3 bg-secondary-container rounded-full border-2 border-white scale-0 group-hover:scale-100 transition-transform"></div>
</div>
<div class="w-full h-[80%] bg-primary/5 rounded-t-sm relative group cursor-pointer hover:bg-primary/10 transition-all">
<div class="absolute -top-xs left-1/2 -translate-x-1/2 w-3 h-3 bg-secondary-container rounded-full border-2 border-white scale-0 group-hover:scale-100 transition-transform"></div>
</div>
</div>
<!-- Axis Labels -->
<div class="absolute bottom-0 left-0 right-0 flex justify-between text-[10px] font-label-caps text-on-surface-variant uppercase pt-sm border-t border-border-soft">
<span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span><span>Sun</span>
</div>
</div>
</div>
<!-- Donut Chart: Completion Breakdown -->
<div class="lg:col-span-4 bg-white p-xl rounded-xl shadow-[0_1px_4px_rgba(30,27,75,0.08)] border border-border-soft flex flex-col h-[400px]">
<h4 class="font-title-card text-title-card text-primary mb-xl">Completion Rate Breakdown</h4>
<div class="flex-1 flex flex-col items-center justify-center relative">
<!-- Custom SVG Donut -->
<div class="relative w-48 h-48">
<svg class="w-full h-full transform -rotate-90" viewbox="0 0 36 36">
<circle cx="18" cy="18" fill="transparent" r="15.915" stroke="#E8E7F5" stroke-width="3"></circle>
<circle cx="18" cy="18" fill="transparent" r="15.915" stroke="#179c6e" stroke-dasharray="76 24" stroke-dashoffset="0" stroke-width="3"></circle>
<circle cx="18" cy="18" fill="transparent" r="15.915" stroke="#fea619" stroke-dasharray="15 85" stroke-dashoffset="-76" stroke-width="3"></circle>
</svg>
<div class="absolute inset-0 flex flex-col items-center justify-center">
<span class="font-headline-md text-headline-md text-primary">76%</span>
<span class="text-[10px] font-label-caps text-on-surface-variant uppercase">Overall</span>
</div>
</div>
<div class="mt-xl w-full grid grid-cols-1 gap-md">
<div class="flex items-center justify-between">
<div class="flex items-center gap-sm">
<span class="w-3 h-3 rounded-full bg-on-tertiary-container"></span>
<span class="text-sm font-medium text-on-surface-variant">Completed</span>
</div>
<span class="text-sm font-semibold text-primary">76.4%</span>
</div>
<div class="flex items-center justify-between">
<div class="flex items-center gap-sm">
<span class="w-3 h-3 rounded-full bg-secondary-container"></span>
<span class="text-sm font-medium text-on-surface-variant">In Progress</span>
</div>
<span class="text-sm font-semibold text-primary">14.8%</span>
</div>
<div class="flex items-center justify-between">
<div class="flex items-center gap-sm">
<span class="w-3 h-3 rounded-full bg-outline-variant"></span>
<span class="text-sm font-medium text-on-surface-variant">Not Started</span>
</div>
<span class="text-sm font-semibold text-primary">8.8%</span>
</div>
</div>
</div>
</div>
</div>
<!-- Course Performance Table -->
<div class="bg-white rounded-xl shadow-[0_1px_4px_rgba(30,27,75,0.08)] border border-border-soft overflow-hidden">
<div class="p-xl border-b border-border-soft flex justify-between items-center bg-surface-container-low/30">
<div>
<h4 class="font-title-card text-title-card text-primary">Course Performance</h4>
<p class="text-xs text-on-surface-variant mt-base">Detailed metrics per active curriculum module</p>
</div>
<button class="p-sm hover:bg-surface-container-low rounded-lg transition-colors border border-border-soft bg-white text-on-surface-variant">
<span class="material-symbols-outlined text-[20px]">filter_list</span>
</button>
</div>
<div class="overflow-x-auto">
<table class="w-full text-left border-collapse">
<thead>
<tr class="bg-surface-container-low/50">
<th class="px-xl py-md text-xs font-label-caps uppercase tracking-wider text-on-surface-variant">Course Name</th>
<th class="px-xl py-md text-xs font-label-caps uppercase tracking-wider text-on-surface-variant">Enrolled</th>
<th class="px-xl py-md text-xs font-label-caps uppercase tracking-wider text-on-surface-variant text-center">Completed</th>
<th class="px-xl py-md text-xs font-label-caps uppercase tracking-wider text-on-surface-variant">Avg. Score</th>
<th class="px-xl py-md text-xs font-label-caps uppercase tracking-wider text-on-surface-variant">Last Updated</th>
<th class="px-xl py-md"></th>
</tr>
</thead>
<tbody class="divide-y divide-border-soft">
<tr class="hover:bg-surface-muted transition-colors group">
<td class="px-xl py-lg">
<div class="flex items-center gap-md">
<div class="w-10 h-10 rounded-lg bg-primary-fixed-dim flex items-center justify-center text-primary">
<span class="material-symbols-outlined">code</span>
</div>
<div>
<p class="font-semibold text-primary text-sm">Advanced Data Structures</p>
<p class="text-xs text-on-surface-variant">Engineering Department</p>
</div>
</div>
</td>
<td class="px-xl py-lg">
<span class="text-sm font-medium text-primary">2,450</span>
</td>
<td class="px-xl py-lg">
<div class="w-full max-w-[120px] mx-auto">
<div class="flex justify-between items-center mb-xs">
<span class="text-[11px] font-bold text-on-tertiary-container">82%</span>
</div>
<div class="h-1.5 w-full bg-border-soft rounded-full overflow-hidden">
<div class="h-full bg-on-tertiary-container rounded-full" style="width: 82%"></div>
</div>
</div>
</td>
<td class="px-xl py-lg">
<span class="px-md py-1 bg-on-tertiary-container/10 text-on-tertiary-container text-xs font-semibold rounded-full">92.4%</span>
</td>
<td class="px-xl py-lg text-sm text-on-surface-variant">Oct 14, 2023</td>
<td class="px-xl py-lg text-right">
<button class="text-on-surface-variant hover:text-primary transition-colors opacity-0 group-hover:opacity-100">
<span class="material-symbols-outlined">more_vert</span>
</button>
</td>
</tr>
<tr class="hover:bg-surface-muted transition-colors group">
<td class="px-xl py-lg">
<div class="flex items-center gap-md">
<div class="w-10 h-10 rounded-lg bg-secondary-fixed flex items-center justify-center text-secondary">
<span class="material-symbols-outlined">history_edu</span>
</div>
<div>
<p class="font-semibold text-primary text-sm">Modern Economics & Policy</p>
<p class="text-xs text-on-surface-variant">Social Sciences</p>
</div>
</div>
</td>
<td class="px-xl py-lg">
<span class="text-sm font-medium text-primary">1,890</span>
</td>
<td class="px-xl py-lg">
<div class="w-full max-w-[120px] mx-auto">
<div class="flex justify-between items-center mb-xs">
<span class="text-[11px] font-bold text-secondary-container">64%</span>
</div>
<div class="h-1.5 w-full bg-border-soft rounded-full overflow-hidden">
<div class="h-full bg-secondary-container rounded-full" style="width: 64%"></div>
</div>
</div>
</td>
<td class="px-xl py-lg">
<span class="px-md py-1 bg-on-tertiary-container/10 text-on-tertiary-container text-xs font-semibold rounded-full">85.1%</span>
</td>
<td class="px-xl py-lg text-sm text-on-surface-variant">Oct 12, 2023</td>
<td class="px-xl py-lg text-right">
<button class="text-on-surface-variant hover:text-primary transition-colors opacity-0 group-hover:opacity-100">
<span class="material-symbols-outlined">more_vert</span>
</button>
</td>
</tr>
<tr class="hover:bg-surface-muted transition-colors group">
<td class="px-xl py-lg">
<div class="flex items-center gap-md">
<div class="w-10 h-10 rounded-lg bg-tertiary-fixed-dim flex items-center justify-center text-on-tertiary-container">
<span class="material-symbols-outlined">palette</span>
</div>
<div>
<p class="font-semibold text-primary text-sm">Design Ethics & UX</p>
<p class="text-xs text-on-surface-variant">Arts & Design</p>
</div>
</div>
</td>
<td class="px-xl py-lg">
<span class="text-sm font-medium text-primary">1,210</span>
</td>
<td class="px-xl py-lg">
<div class="w-full max-w-[120px] mx-auto">
<div class="flex justify-between items-center mb-xs">
<span class="text-[11px] font-bold text-on-tertiary-container">91%</span>
</div>
<div class="h-1.5 w-full bg-border-soft rounded-full overflow-hidden">
<div class="h-full bg-on-tertiary-container rounded-full" style="width: 91%"></div>
</div>
</div>
</td>
<td class="px-xl py-lg">
<span class="px-md py-1 bg-on-tertiary-container/10 text-on-tertiary-container text-xs font-semibold rounded-full">94.8%</span>
</td>
<td class="px-xl py-lg text-sm text-on-surface-variant">Oct 11, 2023</td>
<td class="px-xl py-lg text-right">
<button class="text-on-surface-variant hover:text-primary transition-colors opacity-0 group-hover:opacity-100">
<span class="material-symbols-outlined">more_vert</span>
</button>
</td>
</tr>
<tr class="hover:bg-surface-muted transition-colors group">
<td class="px-xl py-lg">
<div class="flex items-center gap-md">
<div class="w-10 h-10 rounded-lg bg-error-container flex items-center justify-center text-on-error-container">
<span class="material-symbols-outlined">biotech</span>
</div>
<div>
<p class="font-semibold text-primary text-sm">Molecular Biology</p>
<p class="text-xs text-on-surface-variant">Life Sciences</p>
</div>
</div>
</td>
<td class="px-xl py-lg">
<span class="text-sm font-medium text-primary">3,120</span>
</td>
<td class="px-xl py-lg">
<div class="w-full max-w-[120px] mx-auto">
<div class="flex justify-between items-center mb-xs">
<span class="text-[11px] font-bold text-outline-variant">42%</span>
</div>
<div class="h-1.5 w-full bg-border-soft rounded-full overflow-hidden">
<div class="h-full bg-outline-variant rounded-full" style="width: 42%"></div>
</div>
</div>
</td>
<td class="px-xl py-lg">
<span class="px-md py-1 bg-on-secondary-container/10 text-on-secondary-container text-xs font-semibold rounded-full">78.2%</span>
</td>
<td class="px-xl py-lg text-sm text-on-surface-variant">Oct 09, 2023</td>
<td class="px-xl py-lg text-right">
<button class="text-on-surface-variant hover:text-primary transition-colors opacity-0 group-hover:opacity-100">
<span class="material-symbols-outlined">more_vert</span>
</button>
</td>
</tr>
</tbody>
</table>
</div>
<div class="px-xl py-md bg-surface-container-low/30 border-t border-border-soft flex justify-between items-center">
<p class="text-xs text-on-surface-variant font-medium">Showing 4 of 24 courses</p>
<div class="flex items-center gap-base">
<button class="w-8 h-8 flex items-center justify-center rounded-lg border border-border-soft bg-white text-on-surface-variant hover:bg-surface-muted transition-colors">
<span class="material-symbols-outlined text-[18px]">chevron_left</span>
</button>
<button class="w-8 h-8 flex items-center justify-center rounded-lg border border-border-soft bg-white text-on-surface-variant hover:bg-surface-muted transition-colors">
<span class="material-symbols-outlined text-[18px]">chevron_right</span>
</button>
</div>
</div>
</div>
</div>
<footer class="p-xl text-center text-on-surface-variant/40 text-xs font-label-caps mt-xl">
            © 2023 SAHAYTA LMS ANALYTICS ENGINE. ALL RIGHTS RESERVED.
        </footer>
</main>
<!-- FAB Interaction (Subtle contextual action for Reports) -->
<button class="fixed bottom-lg right-lg w-14 h-14 bg-secondary-container text-primary rounded-full shadow-2xl flex items-center justify-center hover:scale-110 active:scale-95 transition-transform z-50 group">
<span class="material-symbols-outlined text-[28px]">download</span>
<span class="absolute right-full mr-md py-1 px-3 bg-primary text-white text-[10px] font-label-caps rounded-md opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none whitespace-nowrap">Export Dashboard</span>
</button>


  </div>
</template>

<script setup>
</script>

<style scoped>
/* Copy any specific styles if needed, or rely on global Tailwind classes */
</style>
